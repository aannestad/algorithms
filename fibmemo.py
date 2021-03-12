def fibmemo(n,use_memo=False):

    # Speed up fibonacci using memoized recursion

    def fib(n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)

    memo = {}

    def fib_memo(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            if n == 1:
                return 1
            else:
                result = fib_memo(n-1) + fib_memo(n-2)
                memo[n] = result
                return result

    if use_memo == False:
        return fib(n)
    else:
        return fib_memo(n)