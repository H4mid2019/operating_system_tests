from lzma import LZMACompressor
from bz2 import BZ2Compressor
import time


def wallis(n):
    pi = 2.
    for i in range(1, n):
        left = (2. * i) / (2. * i - 1.)
        right = (2. * i) / (2. * i + 1.)
        pi = pi * left * right


def fib_range(n):
    def fib(n):
        if n <= 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    for i in range(1, n):
        fib(i)


def fib_loop(n):
    f = 0
    s = 1
    for x in range(2, n):
        nxt = f + s
        f = s
        s = nxt


def compress(n, c_class, c_args=[]):
    c = c_class(*c_args)
    zero = b"0"
    for i in range(n):
        c.compress(zero * n)
    c.flush()


def benchmnarks():
    benchmarks = [
        ("compressing bz2", compress, (2**15, BZ2Compressor, [1])),
        ("compressing lzma", compress, (2**15, LZMACompressor)),
        ("calculating pi", wallis, [2**25]),
        ("calculating fib recursive", fib_range, [2**5 + 2**2 + 2]),
        ("calculating fib iterative", fib_loop, [2**20])
    ]

    for benchmark in benchmarks:
        name, func, args = benchmark
        print(name + " started")
        t1 = time.perf_counter(), time.process_time()
        func(*args)
        t2 = time.perf_counter(), time.process_time()
        print(name + " finished")
        print(f" Real time: {t2[0] - t1[0]:.2f} seconds\nCPU time: {t2[1] - t1[1]:.2f} seconds")


def main():
    t1 = time.perf_counter(), time.process_time()
    benchmnarks()
    t2 = time.perf_counter(), time.process_time()
    print("All benchmarks finished")
    print(f"Real time: {t2[0] - t1[0]:.2f} seconds\nCPU time: {t2[1] - t1[1]:.2f} seconds")


if __name__ == "__main__":
    main()