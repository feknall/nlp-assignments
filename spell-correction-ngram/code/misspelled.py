class Misspelled:
    misspelled_words = list()
    correct_words = list()
    sentences = list()

    size = 0

    def __init__(self):
        self.read_list_of_misspelled_words()

    def get_size(self):
        return self.size

    def get_misspelled_words(self) -> list:
        return self.misspelled_words

    def get_sentences(self) -> list:
        return self.sentences

    def get_correct_words(self) -> list:
        return self.correct_words

    def read_list_of_misspelled_words(self):
        with open('data/APPLING1DAT.643') as f:
            lines = f.readlines()
        for line in lines:
            split = line.split()
            if len(split) <= 1:
                continue
            self.misspelled_words.append(split[0])
            self.correct_words.append(split[1])
            self.sentences.append(' '.join(split[2:]).split('*')[0].split())
        self.size = len(self.misspelled_words)


if __name__ == '__main__':
    miss = Misspelled()
    for i in range(100):
        print(f"{miss.get_sentences()[i]}: {miss.get_misspelled_words()[i]}/{miss.get_correct_words()[i]}")
