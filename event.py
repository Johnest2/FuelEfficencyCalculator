from tkinter import EventType

subscribers=dict()

def subscribe(eventType: str, fn) -> None:
    if not eventType in subscribers:
        subscribers[eventType]=[]
    subscribers[eventType].append(fn)

def postEvent(eventType: str, data) -> None:
    if not eventType in subscribers:
        return
    for fn in subscribers[eventType]:
        fn(data)
