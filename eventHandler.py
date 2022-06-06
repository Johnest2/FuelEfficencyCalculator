from ast import arg


class Event(object):
    def __init__(self):
        super().__init__()
        self.handlers = set()

    def __call__(self, *args, **kwargs):
        for handlers in self.handlers:
            handlers(*args, **kwargs)
    
    def add(self, listener):
        self.handlers.add(listener)
    
    def remvove(self, listener):
        self.handlers.remove(listener)
