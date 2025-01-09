class Statistics:
    def __init__(self,data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.count()

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        middle = n // 2
        if n % 2 == 0:  # Even count
            return (sorted_data[middle - 1] + sorted_data[middle]) / 2
        else:  # Odd count
            return sorted_data[middle]

    def mode(self):
        from collections import Counter
        counts = Counter(self.data)
        max_count = max(counts.values())
        mode = [key for key, value in counts.items() if value == max_count]
        return {'mode': mode, 'count': max_count}

    def var(self):
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / self.count()

    def std(self):
        return self.var() ** 0.5

    def freq_dist(self):
        from collections import Counter
        counts = Counter(self.data)
        return dict(counts)

# Sample data
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

# Create an instance of the Statistics class
data = Statistics(ages)

# Display results
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist())
