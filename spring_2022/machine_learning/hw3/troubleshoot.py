import numpy as np

chars = np.array([[216], [69], [302], [60], [393]])
word_len = np.array([[5.68], [4.78], [2.31], [3.16], [4.2]])

chars_mean = np.mean(chars)
chars_std = np.std(chars)

print(chars_mean, chars_std)

word_mean = np.mean(word_len)
word_std = np.std(word_len)

print(word_mean, word_std)

for i in range(len(chars)):
    x = chars[i]
    z = (x-chars_mean)/chars_std
    #print(z)

for i in range(len(word_len)):
    x = word_len[i]
    z = (x-word_mean)/word_std
    print(z)