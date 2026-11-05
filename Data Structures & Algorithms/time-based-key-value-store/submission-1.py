class TimeMap:
    # create a map like {key: [[value, timestamp], []..]}
    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.keyStore.get(key, []) # get all the values of the given key from map
        res = ""
        # binary search on values
        l, r = 0, len(values)-1
        while l<=r:
            m = (l+r) //2
            # check if timestamp of mid value is less or equal to the given timestamp
            if values[m][1] <= timestamp:
                res = values[m][0] # [0]: value & [1]: timestamp
                l = m +1
            else:
                r = m-1
        return res
