import tkinter as tk
import tkinter.scrolledtext as tksc
from typing import List, Tuple, Optional
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
        self.widgets[f"{name}_val"] = stv

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

    def add_textarea(
        self,
        name: str,
        width: int = 30,
        height: int = 5,
        wrap: str = tk.CHAR,
        with_scrollbar: bool = False,
        default_str: str = ""
    ) -> None:

        txt = tk.Text(
            self.frame,
            width=width,
            height=height,
            wrap=wrap) if not with_scrollbar \
            else \
            tksc.ScrolledText(
                self.frame,
                width=width,
                height=height,
                wrap=wrap
        )

        txt.insert('1.0', default_str)
        self.widgets[name] = txt

    def add_checkbox(
        self,
        name: str,
        text: str,
        default_val: bool = False
    ) -> None:
        bv = tk.BooleanVar(value=default_val)
        chkbox = tk.Checkbutton(
            self.frame,
            text=text,
            variable=bv
        )
        self.widgets[name] = chkbox
        self.widgets[f"{name}_val"] = bv

    def add_radiobutton(
        self,
        name: str,
        text_and_vals: List[Tuple[str, int]],
        default_val: int,
        label_frame_value: Optional[str] = None
    ) -> None:
        n = 0
        vobj_name = f"{name}_val"
        fr = self.frame if label_frame_value is None \
            else tk.LabelFrame(self.frame, text=label_frame_value)

        vobj = tk.IntVar(fr, default_val)
        for text, value in text_and_vals:
            btn_name = f"{name}_{n}"
            btn = tk.Radiobutton(
                fr,
                text=text,
                value=value,
                variable=vobj
            )
            self.widgets[btn_name] = btn
            n += 1
        self.widgets[vobj_name] = vobj
        if label_frame_value is not None:
            self.widgets[f"{name}_labelframe"] = fr

    def build(self):
        self.root.title(self.title)
        self.root.geometry(self._to_geometry())
        [w.pack() for n, w in self.widgets.items() if not n.endswith("_val")]
        return self.root
