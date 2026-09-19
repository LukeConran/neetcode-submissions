class LRUCache:
    def __init__(self, capacity: int):
        self.d = {}                 # key -> [value, down, up]
        self.capacity = capacity
        self.top = None             # most recently used;   top.up == None
        self.bottom = None          # least recently used;  bottom.down == None

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        self._move_to_top(key)
        return self.d[key][0]

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key][0] = value
            self._move_to_top(key)
            return
        self.d[key] = [value, self.top, None]
        if self.top is not None:
            self.d[self.top][2] = key        # fix #2: old top now has a node above
        self.top = key
        if self.bottom is None:
            self.bottom = key
        if len(self.d) > self.capacity:
            new_bottom = self.d[self.bottom][2]
            self.d.pop(self.bottom)
            self.d[new_bottom][1] = None
            self.bottom = new_bottom

    def _move_to_top(self, key: int) -> None:
        if key == self.top:                  # fix #3: don't relink if already top
            return
        self._unlink(key)
        self.d[key][1] = self.top
        self.d[key][2] = None
        self.d[self.top][2] = key            # fix #2
        self.top = key

    def _unlink(self, key: int) -> None:
        down, up = self.d[key][1], self.d[key][2]
        if key == self.bottom:               # fix #1
            self.d[up][1] = None
            self.bottom = up
        else:
            self.d[down][2] = up
            self.d[up][1] = down