class ProgrammingLanguage:
    def __init__(self, name='', typing='', reflection=True, year=1990):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        "{}, {} Typing, Reflection={}, First appeared in {}".format(
            self.name,
            self.typing,
            self.reflection,
            self.year
        )

    def is_dynamic(self):
        return self.typing == 'Dynamic'


if __name__ == 'main':
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]

    print("The dynamic typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)
