# spell-correction-minimum-edit-distance

1. Use find_most_similar.py to find top 10 words with minimum distance between berkbick and wordnet. In order to make it faster, there are two different options.  The first option is using find_top_5_most_similar_birkbeck_wordnet_multiprocessing method in Similarity class. This method creates different processes to complete them simultaneously and depends on the number of CPU cores available. The second option is submitting different jobs by using find_top_10_most_similar_birkbeck_wordnet_single_process method in Similarity class. This method finds top 10 words with minimum edit distance only by using a subset of birkbeck. Therefore, by submitting different jobs, whole dataset will be covered.
2. Use generated data in step 1 to evaluate s@k using evaluate_success_at.py which uses pytrec_eval
3. Use visualization.ipynb to draw charts and diagram
