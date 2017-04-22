from concurrent.futures import ProcessPoolExecutor
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
                return passwd


def pairs(iterable):
    items, nexts = tee(iterable, 2)
    nexts = islice(nexts, 1, None)

    return zip(items, nexts)


def parralel_brute_force(hash_value, alphabet, length):
    futures = []
    with ProcessPoolExecutor(max_workers=4) as executor:
        partition = range(len(alphabet) + 1)
        for pair in pairs(partition):
            future = executor.submit(brute_force, hash_value, alphabet, length, pair[0], pair[1])
            futures.append(future)

        results = [future.result() for future in futures]
        collisions = [r for r in results if r is not None]
        if collisions:
            return collisions[0]


print(parralel_brute_force(md5('zzzzz'.encode('ascii')).hexdigest(), ascii_lowercase, 5))
