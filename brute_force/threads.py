import threading
from hashlib import md5
from itertools import product, tee, islice
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
                print(passwd)
                return passwd


def pairs(iterable):
    items, nexts = tee(iterable, 2)
    nexts = islice(nexts, 1, None)
    
    return zip(items, nexts)

def parralel_brute_force(hash_value, alphabet, length):
    pool = []
    partition = [0, 13, 26]

    for pair in pairs(partition):
        worker = threading.Thread(target=brute_force, args=(hash_value, alphabet, length, pair[0], pair[1]))
        worker.start()

        pool.append(worker)
    
    for worker in pool:
        worker.join()


print(parralel_brute_force(md5('zzzzz'.encode('ascii')).hexdigest(), ascii_lowercase, 5))
