class Solution:
    def maximumGap(self, values):
        n = len(values)

        if n < 2:
            return 0

        min_value = min(values)
        max_value = max(values)

        gap = float(max_value - min_value) / (n - 1)

        if gap == 0:
            return 0

        buckets = [[float('inf'), 0] for __ in xrange(n)]

        for value in values:
            bucket = int((value - min_value) / gap)

            bucket_min = min(buckets[bucket][0], value)
            bucket_max = max(buckets[bucket][1], value)

            buckets[bucket][0] = bucket_min
            buckets[bucket][1] = bucket_max

        max_gap = 0
        prev = min_value

        for bucket_min, bucket_max in buckets:
            if bucket_min == float('inf') and bucket_max == 0:
                continue

            max_gap = max(max_gap, bucket_min - prev)
            prev = bucket_max

        return max_gap
