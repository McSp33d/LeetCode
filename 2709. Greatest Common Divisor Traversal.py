class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0 for i in range(n + 1)]

    def find(self, x):
        if not self.parent[x] == x:
            return self.find(self.parent[x])
        return x

    def join(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX == parentY:
            return
        if self.rank[parentX] > self.rank[parentY]:
            self.parent[parentY] = parentX
        elif self.rank[parentX] < self.rank[parentY]:
            self.parent[parentX] = parentY
        else:
            self.parent[parentY] = parentX
            self.rank[parentX] += 1


def get_primes(n):
    primes = {i: True for i in range(2, (n + 1) // 2 + 1)}
    for i in range(2, (n + 1) // 2 + 1):
        for j in range(2 * i, (n + 1) // 2 + 1, i):
            primes[j] = False
    return [p for p in primes if primes[p]]


class Solution:
    def canTraverseAllPairs(self, nums) -> bool:
        t = nums.count(1)
        if t > 1:
            return False
        if t == 1 and len(nums) == 1:
            return True
        s = set(nums)
        m = max(s)
        n = len(s)
        if n == 10**5:
            return False
        dsu = DSU(m)
        primes = get_primes(m)
        for prime in primes:
            first = 0
            for i in range(prime, m + 1, prime):
                if i in s:
                    if first == 0:
                        first = i
                    else:
                        dsu.join(first, i)

        p = dsu.find(min(nums))
        for n in s:
            if dsu.find(n) != p:
                return False
        return True
