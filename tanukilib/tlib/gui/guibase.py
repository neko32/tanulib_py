import tkinter as tk
from typing import List
from enum import Enum, auto


class GUIEvent(Enum):
    EVT_LEFTCLICK = auto()


def from_GUIEvent_to_str(evt: GUIEvent) -> str:
    if evt == GUIEvent.EVT_LEFTCLICK:
        return "<Button-1>"
    else:
        raise ValueError("not supported")


class EventCallBack:
    def __init__(self, evt: GUIEvent, callback):
        self._evt = evt
        self._callback = callback

    @property
    def event(self) -> GUIEvent:
        return self._evt

    @property
    def callback(self):
        return self._callback


class GUIManager:

    def __init__(
        self,
        title: str,
        x_loc: int,
        y_loc: int,
        width: int,
        height: int
    ) -> None:
        self.title = title
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.width = width
        self.height = height
        self.widgets = {}
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)

    def _to_geometry(self) -> str:
        return f"{self.width}x{self.height}+{self.x_loc}+{self.y_loc}"

    def add_label(
        self,
        name: str,
        text: str
    ) -> None:
        label = tk.Label(self.frame, text=text)
        self.widgets[name] = label

    def add_textbox(
        self,
        name: str,
        default_str: str = ""
    ) -> None:
        stv = tk.StringVar(self.frame, default_str)
        txt = tk.Entry(self.frame, textvariable=stv)
        self.widgets[name] = txt

    def add_button(
        self,
        name: str,
        value: str,
        evt_callbacks: List[EventCallBack]
    ) -> None:
        btn = tk.Button(self.frame, text=value)
        head_evt = evt_callbacks[0]
        btn.bind(from_GUIEvent_to_str(head_evt.event), head_evt.callback)
        for evt in evt_callbacks[1:]:
            btn.bind(from_GUIEvent_to_str(evt.event), evt.callback, '+')
        self.widgets[name] = btn

    def build(self):
        self.root.title(self.title)
        self.root.geometry(self._to_geometry())
        [w.pack() for w in self.widgets.values()]
        return self.root