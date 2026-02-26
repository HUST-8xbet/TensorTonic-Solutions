import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    mp = dict()
    for word in tokens:
        mp[word] = mp.get(word, 0) + 1
    res = np.zeros(len(vocab), dtype = int)
    for i, word in enumerate(vocab):
        if word in mp:
            res[i] = mp[word]
    return res
    pass