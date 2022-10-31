from field import Field


class River(list):

    def __init__(self, initial_field: Field):
        super().__init__([initial_field])

    def get_unchecked_river_elements(self):
        return set(filter(lambda x: not x.checked, self))

    def set_as_checked(self):
        for field in self:
            field.checked = True

    def mark_as_longest(self):
        for field in self:
            field.is_longest_river = True


if __name__ == '__main__':
    river_obj = River(Field(0, 0, False))
    pass
