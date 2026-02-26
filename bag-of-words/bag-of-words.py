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
    for a in range(len(vocab)):
        if vocab[a] in mp:
            res[a] = mp[vocab[a]]
    return res
    pass