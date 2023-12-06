# lcg.py
class LCG:
    def __init__(self, seed, a, c, m):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def next(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state / self.m  # Normalize to [0, 1)

    def generate_sequence(self, n):
        sequence = []
        for _ in range(n):
            sequence.append(self.next())
        return sequence
