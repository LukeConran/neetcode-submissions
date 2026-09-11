from collections import defaultdict
from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.store = defaultdict(lambda: ([], []))  # key -> (timestamps, values)

    def set(self, key: str, value: str, timestamp: int) -> None:
        timestamps, values = self.store[key]
        timestamps.append(timestamp)
        values.append(value)

    def get(self, key: str, timestamp: int) -> str:
        timestamps, values = self.store[key]
        index = bisect_right(timestamps, timestamp)
        return values[index - 1] if index else ""