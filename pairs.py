import sys
import timeit

def pairs_append_yield(xs):
    buf = []
    for x in xs:
        buf.append(x)
        if len(buf) >= 2:
            yield tuple(buf)
            buf.clear()

def pairs_index_access(xs):
    for i in range(len(xs) // 2):
        yield xs[2 * i], xs[2 * i + 1]

class PairsIterator:
    def __init__(self, xs):
        self.xs = xs
        self.index = 0
        self.max_index = len(xs) // 2

    def __iter__(self):
        return self

    def __next__(self):
        i = self.index
        if i >= self.max_index:
            raise StopIteration()

        value = self.xs[2 * i], self.xs[2 * i + 1]

        self.index += 1
        return value

def pairs_index_access_iter(xs):
    return PairsIterator(xs)

def pairs_slice_copy(xs):
    for _ in range(len(xs) // 2):
        yield tuple(xs[:2])
        xs = xs[2:]

def pairs_even_odd(xs):
    evens = (x for i, x in enumerate(xs) if i % 2 == 0)
    odds = (x for i, x in enumerate(xs) if i % 2 == 1)
    for even, odd in zip(evens, odds):
        yield even, odd

def pairs_grouper(xs):
    args = [iter(xs)] * 2
    return zip(*args)

def benchmark(M):
    N = 10000
    target_functions = [
        'pairs_append_yield',
        'pairs_index_access',
        'pairs_index_access_iter',
        'pairs_slice_copy',
        'pairs_even_odd',
        'pairs_grouper',
    ]
    for funcname in target_functions:
        stmt = f'xs = list(range({M})); list({funcname}(xs))'
        elapsed = timeit.timeit(stmt, number=N, globals=globals())
        print(f'{funcname}\t{elapsed}')

if __name__ == '__main__':
    M = int(sys.argv[1])
    benchmark(M)
