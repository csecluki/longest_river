import datetime
from itertools import chain
import random

import numpy as np

from field import Field
from river import River


class Land:
    rivers = []

    def __init__(self, width, height, objects=None):
        self.width = width
        self.height = height
        self.objects = objects or self.generate_field_objects()
        self.fields = list(filter(lambda x: x.is_river, self.objects))

    def generate_field_objects(self):
        return [Field(x, y, random.choice((True, False)))
                for y in range(self.height)
                for x in range(self.width)]

    def find_longest_river(self):
        while field := self.get_unchecked_field():
            self.rivers.append(river := River(field))
            while unchecked := self.get_unchecked_river_elements(river):
                river.set_as_checked()
                if not (neighbours := self.get_neighbours(unchecked)):
                    break
                river.extend(neighbours)
        longest_river = self.get_longest_river()
        return len(longest_river), len(self.rivers)

    def get_unchecked_field(self):
        iterator = iter(self.fields)
        while True:
            try:
                field = next(iterator)
                if not field.checked:
                    return field
            except StopIteration:
                return None

    def get_neighbours(self, unchecked):
        return set(chain.from_iterable(self.find_field_neighbours(x) for x in unchecked))

    def find_field_neighbours(self, field: Field):
        n = filter(lambda neighbour: (((neighbour.x == field.x and abs(field.y - neighbour.y) == 1) or
                                       (neighbour.y == field.y and abs(field.x - neighbour.x) == 1)
                                       ) and not neighbour.checked),
                   self.fields
                   )
        return n

    def convert_to_array(self):
        array = np.empty((self.width, self.height), dtype=Field)
        for element in self.objects:
            array[element.x][element.y] = element
        return array

    def get_longest_river(self):
        try:
            river = max(self.rivers, key=lambda r: len(r))
        except ValueError:
            return []
        else:
            river.mark_as_longest()
            return river

    @staticmethod
    def get_unchecked_river_elements(river):
        return set(filter(lambda x: not x.checked, river))


if __name__ == '__main__':
    np.set_printoptions(linewidth=2000, threshold=100000)
    start = datetime.datetime.now()
    land = Land(15, 15)
    length, river_number = land.find_longest_river()
    t = datetime.datetime.now() - start
    print(f"Solved in: {t}", f'Longest river: {length}', river_number, sep='\n')
    print(land.convert_to_array())
