from datetime import datetime
from lzma import LZMACompressor
from bz2 import BZ2Compressor


def wallis(n):
    pi = 2.
    for i in range(1, n):
        left = (2. * i) / (2. * i - 1.)
        right = (2. * i) / (2. * i + 1.)
        pi = pi * left * right
    # print(len(str(pi)), 'decimals')


def fib_range(n):
    def fib(n):
        if n <= 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    for i in range(1, n):
        fib(i)
    # cpus = cpu_count()
    # with ThreadPoolExecutor(max_workers=cpus) as executor:
    #     fibs = [executor.submit(fib, i) for i in range(1, n)]
    #     with total=n) as pbar:
    #         for future in as_completed(fibs):
    #             pbar.update()


def fib_loop(n):
    f = 0
    s = 1
    for x in range(2, n):
        nxt = f + s
        f = s
        s = nxt
    # print(len(str(s)), 'decimals')


def compress(n, c_class, c_args=[]):
    c = c_class(*c_args)
    zero = b"0"
    for i in range(n):
        c.compress(zero * n)
    c.flush()


def benchmnarks():
    print('compressing bz2:')
    start = datetime.now()
    compress(n=2**15, c_class=BZ2Compressor, c_args=[1])
    print('benchmark time bz2:', datetime.now() - start)

    print('compressing lzma:')
    start = datetime.now()
    compress(n=2**15, c_class=LZMACompressor)
    print('benchmark time lzma:', datetime.now() - start)

    print('calculating pi:')
    start = datetime.now()
    wallis(2**25)
    print('benchmark time pi:', datetime.now() - start)

    print('calculating fib recursive:')
    start = datetime.now()
    fib_range(2**5 + 2**2 + 2)
    print('benchmark time fib recursive:', datetime.now() - start)

    print('calculating fib iterative:')
    start = datetime.now()
    fib_loop(2**20)
    print('benchmark time fib iterative:', datetime.now() - start)


def main():
    start = datetime.now()
    benchmnarks()
    end = datetime.now()
    result = end - start
    print('benchmark time:', result)


if __name__ == "__main__":
    main()