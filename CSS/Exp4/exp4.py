# AIM: TO IMPLEMENT DIFFIE HELLMAN KEY EXCHANGE ALGORITHM

import math
import random


def generate_random_prime():
        prime = [x for x in range(2, 1000) if all(x % y != 0 for y in range(2, int(math.floor(math.sqrt(x))) + 1))]
        return random.choice(prime)


def diffie_hellman(x, y, n, g):
        A = g ** x % n
        B = g ** y % n

        key1 = B ** x % n
        key2 = A ** y % n

        print('Key1: {}'.format(key1))
        print('Key2: {}'.format(key2))


def main():
        n = generate_random_prime()
        g = generate_random_prime()
        x = int(input('Enter x: '))
        y = int(input('Enter y: '))
        diffie_hellman(x, y, n, g)


if __name__ == '__main__':
        main()

'''
OUTPUT:
Enter x: 6
Enter y: 15
Key1: 736
Key2: 736
'''
