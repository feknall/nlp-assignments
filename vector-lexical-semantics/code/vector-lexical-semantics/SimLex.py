class SimLex:
    simlex_path = '/home/hamid/PycharmProjects/vector-lexical-semantics/SimLex-999.txt'
    word_to_similar = {}

    def __init__(self):
        word1_list, word2_list, similarity_score = self.read_file()
        self.initialize(word1_list, word2_list, similarity_score)
        self.transitivity()
        self.sort()

    def sort(self):
        print("Pre sort similarity:")
        print(self.word_to_similar)
        print("After sort similarity:")
        for word in self.word_to_similar:
            self.word_to_similar[word] = sorted(self.word_to_similar[word], key=lambda x: x[1], reverse=True)
        print(self.word_to_similar)

    def transitivity(self):
        print("\nStart applying the transition rule...\n")
        for word in self.word_to_similar:
            if len(self.word_to_similar[word]) < 10:
                print(f"Word: {word}")
                print(f"Pre: {self.word_to_similar[word]}")
                transition_list = list()
                for similar_pair in self.word_to_similar[word]:
                    if similar_pair[0] in self.word_to_similar:
                        print(f"{similar_pair} -> {self.word_to_similar[similar_pair[0]]}")
                        transition_words = self.word_to_similar[similar_pair[0]]
                        for transition in transition_words:
                            transition_score = (similar_pair[1] + transition[1]) / 2
                            transition_list.append((transition[0], transition_score))
                    else:
                        print(f"{similar_pair} -> ***")
                self.word_to_similar[word] += transition_list
                print(f"Post: {self.word_to_similar[word]}\n")

    def read_file(self):
        word1_list = list()
        word2_list = list()
        similarity_score = list()

        with open(self.simlex_path) as f:
            lines = f.readlines()

        for line in lines[1:]:
            split = line.split()
            word1_list.append(split[0])
            word2_list.append(split[1])
            similarity_score.append(split[-1])

        return word1_list, word2_list, similarity_score

    def initialize(self, word1_list, word2_list, similarity_score):
        for index, word in enumerate(word1_list):
            if word not in self.word_to_similar:
                self.word_to_similar[word] = list()
            self.word_to_similar[word].append((word2_list[index], float(similarity_score[index])))

        print(f"Initial similarity:")
        print(self.word_to_similar)

    def get_top_10(self, words: list):
        output = {}
        for word in words:
            if word in self.word_to_similar:
                output[word] = list()
                for inner_tuple in self.word_to_similar[word]:
                    output[word].append(inner_tuple[0])
        return output