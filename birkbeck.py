import re


class Birkbeck:
    words = None
    misspelled_words = list()
    correct_words = list()
    regex_pattern = "[A-Za-z]"
    pattern = re.compile(regex_pattern)

    def __init__(self):
        self.words = self.read_list_of_misspelled_words()
        self.misspelled_words = [t[0] for t in self.words]
        self.correct_words = [t[1] for t in self.words]

    def get_misspelled_words(self) -> list:
        return self.misspelled_words

    def get_correct_words(self) -> list:
        return self.correct_words

    def read_list_of_misspelled_words(self) -> list:
        with open('./data/EXAMSDAT.643') as f:
            lines = f.readlines()
        valid_lines = list()
        for line in lines:
            split = line.split()
            if len(split) <= 1 or not self.pattern.match(split[1]):
                continue
            valid_lines.append((split[0], split[1]))
        return valid_lines


if __name__ == '__main__':
    birk = Birkbeck()
    miss = birk.get_misspelled_words()
    print(miss[:10])
    corr = birk.get_correct_words()
    print(corr[:10])
