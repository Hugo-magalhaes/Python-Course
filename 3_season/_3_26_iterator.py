from collections.abc import Sequence  # Iterable, Iterator,


class MyList(Sequence):
    def __init__(self) -> None:
        self._data = {}
        self._index = 0
        self.next_index = 0

    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_index >= self._index:
            self.next_index = 0
            raise StopIteration

        value = self._data[self.next_index]
        self.next_index += 1
        return value

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __len__(self):
        return self._index
