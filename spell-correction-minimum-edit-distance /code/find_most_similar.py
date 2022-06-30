from similarity import Similarity
import sys

if __name__ == '__main__':
    birkbeck_total_parts = 10000
    birkbeck_page = 0
    if (len(sys.argv)) >= 2:
        birkbeck_total_parts = int(sys.argv[1])
    if (len(sys.argv)) >= 3:
        birkbeck_page = int(sys.argv[2])
    similarity = Similarity(birkbeck_total_parts)
    similarity.find_top_10_most_similar_birkbeck_wordnet_single_process(birkbeck_page)
    print("Done")