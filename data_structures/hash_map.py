"""
Hash Map Data Structure implementation with
"""

from typing import Generic, TypeVar, Optional, Tuple

K = TypeVar("K")
V = TypeVar("V")


class HashMap(Generic[K, V]):
    def __init__(self, capacity: int = 16, load_factor: float = 0.75) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")

        self._capacity = capacity
        self._load_factor_threshold = load_factor
        self._size = 0

        # Each slot is a bucket (list) that holds (key, value) pairs
        self._table: list[list[Tuple[K, V]]] = [[] for _ in range(capacity)]

    def _hash(self, key: K) -> int:
        return hash(key) % self._capacity

    def _current_load_factor(self) -> float:
        return self._size / self._capacity

    def _resize(self) -> None:
        old_table = self._table
        self._capacity *= 2
        self._table = [[] for _ in range(self._capacity)]
        self._size = 0

        for bucket in old_table:
            for key, value in bucket:
                self.set(key, value)

    # ---------------- Public API ----------------

    def set(self, key: K, value: V) -> None:
        index = self._hash(key)
        bucket = self._table[index]

        # Update if key already exists
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Otherwise insert new
        bucket.append((key, value))
        self._size += 1

        if self._current_load_factor() > self._load_factor_threshold:
            self._resize()

    def get(self, key: K) -> V:
        index = self._hash(key)
        bucket = self._table[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(key)

    def remove(self, key: K) -> None:
        index = self._hash(key)
        bucket = self._table[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._size -= 1
                return

        raise KeyError(key)

    def __contains__(self, key: K) -> bool:
        index = self._hash(key)
        return any(k == key for k, _ in self._table[index])

    def __len__(self) -> int:
        return self._size


def main():
    hash_map = HashMap[str, Optional[int]]()

    hash_map.set("a", 10)
    hash_map.set("b", 20)
    hash_map.set("c", None)
    hash_map.set("d", 40)

    print(hash_map.get("a"))
    print(hash_map.get("c"))
    print("b" in hash_map)
    print(len(hash_map))

    hash_map.remove("b")
    print("b" in hash_map)

    # Force collisions & resizing
    for i in range(20):
        hash_map.set(f"k{i}", i)

    print("capacity after resize:", hash_map._capacity)
    print("size:", len(hash_map))


if __name__ == "__main__":
    main()
