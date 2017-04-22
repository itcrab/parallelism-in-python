from hashlib import md5
from itertools import product
from string import ascii_lowercase


def all_words(alphabet, length):
    return (''.join(letters) for letters in product(alphabet, repeat=length))


def is_collision(passwd, hash_value):
    return md5(passwd.encode('ascii')).hexdigest() == hash_value


def brute_force(hash_value, alphabet, length, begin=0, end=None):
    end = len(alphabet) if end is None else end
    for first_letter in alphabet[begin:end]:
        for word in all_words(alphabet, length - 1):
            passwd = first_letter + word
            if is_collision(passwd, hash_value):
                return passwd


print(brute_force(md5('zzzzz'.encode('ascii')).hexdigest(), ascii_lowercase, 5))
