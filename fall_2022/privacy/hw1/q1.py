import random
import numpy

def random_response(X, gamma):
    Y, rand = get_Y(X, gamma)
    print(f"X: {X}\n\ngamma + 1/2: {gamma+.5}\nrandom value: {rand}\n\nY: {Y}")
    
    
def get_Y(X, gamma):
    random_num = random.random()
    truth_threshold = .5 + gamma
    if random_num >= truth_threshold:
        return X, random_num
    else:
        return 1-X, random_num

def get_gamme():
    return random.uniform(0, .5)

def get_X():
    return random.randint(0, 1)

if __name__ == '__main__':
    X = get_X()
    gamma = get_gamme()
    random_response(X, gamma)

