class Birkbeck:
    words = list()

    def __init__(self):
        self.words = self.read_list_of_misspelled_words()

    def get_words(self) -> list:
        return self.words

    def read_list_of_misspelled_words(self) -> list:
        with open('./data/MASTERSDAT.643') as f:
            lines = f.readlines()
        return list(map(self.select_first_word, lines))[1:]

    def select_first_word(self, line) -> str:
        return line.split()[0]
