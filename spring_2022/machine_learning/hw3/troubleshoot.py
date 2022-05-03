from tkinter import E
import numpy as np
import pdb

chars = np.array([[216], [69], [302], [60], [393]])
word_len = np.array([[5.68], [4.78], [2.31], [3.16], [4.2]])

chars0 = np.array([[302], [393]])
chars1 = np.array([[216], [69], [60]])
word0 = np.array([[2.31], [4.2]])
word1 = np.array([[5.68], [4.78], [3.16]])

chars_mean = np.mean(chars)
chars_std = np.std(chars)

chars_mean0 = np.mean(chars0)
chars_mean1 = np.mean(chars1)
chars_std0 = np.std(chars0)
chars_std1 = np.std(chars1)

#print(chars_mean, chars_std)

word_mean0 = np.mean(word0)
word_std0 = np.std(word0)
word_mean1 = np.mean(word1)
word_std1 = np.std(word1)

#print(word_mean, word_std)
print(chars_mean0, chars_std0)
print(chars_mean1, chars_std1)
print()
print(word_mean0, word_std0)
print(word_mean1, word_std1)
print()

for i in range(len(chars0)):
    x = chars0[i]
    z = (x-chars_mean0)/chars_std0
    print(z)
print()
for i in range(len(chars1)):
    x = chars1[i]
    z = (x-chars_mean1)/chars_std1
    print(z)

print()
print()
for i in range(len(word0)):
    x = word0[i]
    z = (x-word_mean0)/word_std0
    print(z)
print()
for i in range(len(word1)):
    x = word1[i]
    z = (x-word_mean1)/word_std1
    print(z)
#pdb.set_trace()



'''
print((242-347.5)/45.5)
print((242-115)/71.5122)
print((4.56-3.255)/.945)
print((4.56-4.54)/1.0427)
'''



std = 45.5
x = -2.3186
mu = 347.5
denom = std * np.sqrt(2*np.pi)
exponent = (x-mu)/(2 * (std**2))
e = np.exp(exponent)
Pc = 1/denom * e

print(Pc)

std = .945
x = 1.3809
mu = 3.255
denom = std * np.sqrt(2*np.pi)
exponent = (x-mu)/(2 * (std**2))
e = np.exp(exponent)
Pw = 1/denom * e

print(Pw)
Pa = (3/5) * Pc * Pw

print(Pa)
print()
print()
std = 71.5122
x = 1.7759
mu = 115
denom = std * np.sqrt(2*np.pi)
exponent = (x-mu)/(2 * (std**2))
e = np.exp(exponent)
Pc = 1/denom * e

print(Pc)

std = 1.0427
x = .0191
mu = 4.54
denom = std * np.sqrt(2*np.pi)
exponent = (x-mu)/(2 * (std**2))
e = np.exp(exponent)
Pw = 1/denom * e

print(Pw)
Pna = (2/5) * Pc * Pw

print(Pna)
print(max(Pna, Pa))