import colorama


class Field:
    checked = False
    is_longest_river = False

    def __init__(self, x: int, y: int, is_river: bool):
        self.x = x
        self.y = y
        self.is_river = is_river

    def __repr__(self):
        return f"Field at ({self.x}, {self.y})"

    def __str__(self):
        color = self.get_repr_color()
        return f"{color}{chr(9608)}{chr(9608)}{colorama.Fore.RESET}"

    def get_repr_color(self):
        if not self.is_river:
            return colorama.Fore.RED
        if not self.is_longest_river:
            return colorama.Fore.LIGHTBLUE_EX
        return colorama.Fore.LIGHTGREEN_EX
