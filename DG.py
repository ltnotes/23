class DGIM:
    def __init__(self, window):
        self.window = window
        self.buckets = []  # (timestamp, size)
        self.time = 0

    def add(self, bit):
        self.time += 1
        if bit == 1:
            self.buckets.insert(0, (self.time, 1))
            self._merge()
        # remove buckets older than window
        while self.buckets and self.buckets[-1][0] <= self.time - self.window:
            self.buckets.pop()

    def _merge(self):
        i = 0
        while i < len(self.buckets) - 2:
            if (self.buckets[i][1] == self.buckets[i + 1][1] ==
                    self.buckets[i + 2][1]):
                # merge two oldest of same size
                t = self.buckets[i + 1][0]
                s = self.buckets[i][1] * 2
                del self.buckets[i + 1:i + 3]
                self.buckets.insert(i + 1, (t, s))
            else:
                i += 1

    def query(self, k):
        cutoff = self.time - k
        total = 0
        for t, s in self.buckets:
            if t > cutoff:
                total += s
            else:
                total += s / 2
                break
        return int(total)


# Example usage
dgim = DGIM(window=100)
stream = [1, 0, 1, 1, 0, 1, 1, 1]
for b in stream:
    dgim.add(b)

print("Approx. 1s in last 5 bits:", dgim.query(5))
