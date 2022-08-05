from itertools import chain


class MyIterList:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        self.item = iter(self.obj)
        return self

    def __next__(self):
        item_nxt = next(self.item)
        if isinstance(item_nxt, list):
            self.item = chain(item_nxt, self.item)
            return next(self.item)
        return item_nxt
