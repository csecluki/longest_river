import csv
import datetime
from itertools import chain
from collections import defaultdict, OrderedDict
import random


from field import Field
from river import River


class Land:
    rivers = []

    def __init__(self, file_path=None):
        self.objects = self.load_from_file(file_path) if file_path else self.generate_random_field_objects()
        self.fields = list(filter(lambda x: x.is_river, self.objects))

    def __str__(self):
        string_builder = ''
        for row in self.create_object_dict():
            for field in row:
                string_builder += str(field)
            string_builder += '\n'
        return string_builder

    @staticmethod
    def generate_random_field_objects():
        x, y = random.randint(1, 50), random.randint(1, 50)
        return [Field(i, j, random.choice((True, False)))
                for j in range(x)
                for i in range(y)]

    def find_longest_river(self):
        while field := self.get_unchecked_field():
            self.rivers.append(river := River(field))
            while unchecked := river.get_unchecked_river_elements():
                river.set_as_checked()
                if not (neighbours := self.get_neighbours(unchecked)):
                    break
                river.extend(neighbours)
        longest_river = self.get_longest_river()
        return len(longest_river), len(self.rivers)

    def get_unchecked_field(self):
        try:
            return next(filter(lambda x: not x.checked, self.fields))
        except StopIteration:
            return None

    def get_neighbours(self, unchecked):
        return set(chain.from_iterable(self.find_field_neighbours(x) for x in unchecked))

    def find_field_neighbours(self, field: Field):
        return filter(lambda neighbour: (((neighbour.x == field.x and abs(field.y - neighbour.y) == 1) or
                                          (neighbour.y == field.y and abs(field.x - neighbour.x) == 1)
                                          ) and not neighbour.checked),
                      self.fields
                      )

    def get_longest_river(self):
        try:
            river = max(self.rivers, key=lambda r: len(r))
        except ValueError:
            return []
        else:
            river.mark_as_longest()
            return river

    @staticmethod
    def load_from_file(file_path):
        with open(file_path) as file:
            data = csv.reader(file)
            obj = []
            for row_id, row in enumerate(data):
                for col_id, river in enumerate(row):
                    obj.append(Field(col_id, row_id, True if river == '1' else False))
        return obj

    def create_object_dict(self):
        d = defaultdict(list)
        for field in self.objects:
            d[field.y].append(field)
        return OrderedDict(sorted(d.items())).values()


if __name__ == '__main__':
    start = datetime.datetime.now()
    land = Land('example_data/small_data.csv')
    length, river_number = land.find_longest_river()
    t = datetime.datetime.now() - start
    print(f"Solved in: {t}", f'Longest river: {length}', river_number, sep='\n')
    print(land)
