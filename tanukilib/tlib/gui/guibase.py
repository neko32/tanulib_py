import tkinter as tk
from tkinter import filedialog as fdlg
import tkinter.ttk as ttk
import tkinter.scrolledtext as tksc
from typing import List, Tuple, Optional, Any
from enum import Enum, auto


class GUIEvent(Enum):
    EVT_LEFTCLICK = auto()


class SelectMode(Enum):
    BROWSE = "browse"
    SINGLE = "single"
    MULTIPLE = "multiple"
    extended = "extended"


class LayoutType(Enum):
    DEFAULT = "default"
    GRID = "grid"
    ABSOLUTE = "absolute"


class Orient(Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"


class FileDialogFileType:
    def __init__(self, description: str, filter: str):
        self._description = description
        self._filter = filter

    @property
    def description(self) -> str:
        return self._description

    @property
    def filter(self) -> str:
        return self._filter

    def as_tuple(self) -> Tuple[str, str]:
        return (self._description, self._filter)


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


class FrameInfo:
    def __init__(
            self,
            name: str,
            frame: tk.Frame,
            padx: int = 0,
            pady: int = 0
    ):
        self.name = name
        self.frame = frame
        self.padx = padx
        self.pady = pady


class GUIManager:

    def __init__(
        self,
        title: str,
        x_loc: int,
        y_loc: int,
        width: int,
        height: int,
        default_frame_padx: int = 0,
        default_frame_pady: int = 0
    ) -> None:
        self.title = title
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.width = width
        self.height = height
        self.widgets = {}
        self.root = tk.Tk()
        frd = FrameInfo(
            "default",
            tk.Frame(self.root),
            default_frame_padx,
            default_frame_pady
        )
        self.frame = {frd.name: frd}
        self.frame["default"].frame.pack(fill=tk.BOTH, expand=True)
        self.menubar = None
        self.menus = {}
        self.is_grid_enabled = False

    def _to_geometry(self) -> str:
        return f"{self.width}x{self.height}+{self.x_loc}+{self.y_loc}"

    def add_frame(
        self,
        name: str,
        padx: int = 0,
        pady: int = 0
    ) -> None:
        frd = FrameInfo(
            name,
            tk.Frame(self.root),
            padx,
            pady
        )
        self.frame[name] = frd

    def add_label(
        self,
        name: str,
        text: str,
        frame_name: str = "default",
        layout_type: LayoutType = LayoutType.DEFAULT,
        grid_row: int = 0,
        grid_col: int = 0
    ) -> None:
        frm = self.frame[frame_name].frame
        label = tk.Label(frm, text=text)
        if layout_type == LayoutType.GRID:
            label.grid(row=grid_row, column=grid_col)
            self.is_grid_enabled = True
        self.widgets[name] = label

    def add_textbox(
        self,
        name: str,
        default_str: str = "",
        frame_name: str = "default",
        layout_type: LayoutType = LayoutType.DEFAULT,
        grid_row: int = 0,
        grid_col: int = 0
    ) -> None:
        frm = self.frame[frame_name].frame
        stv = tk.StringVar(frm, default_str)
        txt = tk.Entry(frm, textvariable=stv)
        if layout_type == LayoutType.GRID:
            txt.grid(row=grid_row, column=grid_col)
            self.is_grid_enabled = True
        self.widgets[name] = txt
        self.widgets[f"{name}_val"] = stv

    def add_button(
        self,
        name: str,
        value: str,
        evt_callbacks: List[EventCallBack],
        frame_name: str = "default",
        layout_type: LayoutType = LayoutType.DEFAULT,
        grid_row: int = 0,
        grid_col: int = 0
    ) -> None:
        frm = self.frame[frame_name].frame
        btn = tk.Button(frm, text=value)
        if layout_type == LayoutType.GRID:
            btn.grid(row=grid_row, column=grid_col)
            self.is_grid_enabled = True
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
        default_str: str = "",
        frame_name: str = "default",
        layout_type: LayoutType = LayoutType.DEFAULT,
        grid_row: int = 0,
        grid_col: int = 0
    ) -> None:
        frm = self.frame[frame_name].frame
        txt = tk.Text(
            frm,
            width=width,
            height=height,
            wrap=wrap) if not with_scrollbar \
            else \
            tksc.ScrolledText(
                frm,
                width=width,
                height=height,
                wrap=wrap
        )
        if layout_type == LayoutType.GRID:
            txt.grid(row=grid_row, column=grid_col)
            self.is_grid_enabled = True

        txt.insert('1.0', default_str)
        self.widgets[name] = txt

    def add_checkbox(
        self,
        name: str,
        text: str,
        default_val: bool = False,
        frame_name: str = "default",
        layout_type: LayoutType = LayoutType.DEFAULT,
        grid_row: int = 0,
        grid_col: int = 0
    ) -> None:
        frm = self.frame[frame_name].frame
        bv = tk.BooleanVar(value=default_val)
        chkbox = tk.Checkbutton(
            frm,
            text=text,
            variable=bv
        )
        if layout_type == LayoutType.GRID:
            chkbox.grid(row=grid_row, column=grid_col)
            self.is_grid_enabled = True
        self.widgets[name] = chkbox
        self.widgets[f"{name}_val"] = bv

    def add_radiobutton(
        self,
        name: str,
        text_and_vals: List[Tuple[str, int]],
        default_val: int,
        label_frame_value: Optional[str] = None,
        frame_name: str = "default",
        layout_type: LayoutType = LayoutType.DEFAULT,
        grid_row: int = 0,
        grid_col: int = 0
    ) -> None:
        n = 0
        vobj_name = f"{name}_val"
        frm = self.frame[frame_name].frame
        fr = frm if label_frame_value is None \
            else tk.LabelFrame(frm, text=label_frame_value)

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
        if layout_type == LayoutType.GRID:
            fr.grid(row=grid_row, column=grid_col)
            self.is_grid_enabled = True
        self.widgets[vobj_name] = vobj
        if label_frame_value is not None:
            self.widgets[f"{name}_labelframe"] = fr

    def add_listbox(
        self,
        name: str,
        values: List[str],
        select_mode: SelectMode = SelectMode.BROWSE,
        default_value: Optional[str] = None,
        select_callback: Optional[Any] = None,
        frame_name: str = "default",
        layout_type: LayoutType = LayoutType.DEFAULT,
        grid_row: int = 0,
        grid_col: int = 0
    ) -> None:
        frm = self.frame[frame_name].frame
        lv = tk.StringVar(frm, value=values)
        lb = tk.Listbox(
            frm,
            listvariable=lv,
            selectmode=select_mode.value
        )
        if layout_type == LayoutType.GRID:
            lb.grid(row=grid_row, column=grid_col)
            self.is_grid_enabled = True
        if select_callback is not None:
            lb.bind("<<ListboxSelect>>", select_callback)
        if default_value is not None:
            idx = 0
            found = False
            while idx < len(values):
                if default_value == values[idx]:
                    found = True
                    break
                idx += 1
            if found:
                lb.select_set(idx)
        self.widgets[f"{name}_val"] = lv
        self.widgets[name] = lb

    def add_dropdownbox(
        self,
        name: str,
        values: Tuple[str],
        default_value: Optional[str] = None,
        select_callback: Optional[Any] = None,
        frame_name: str = "default",
        layout_type: LayoutType = LayoutType.DEFAULT,
        grid_row: int = 0,
        grid_col: int = 0
    ) -> None:
        frm = self.frame[frame_name].frame
        dbox = ttk.Combobox(
            frm,
            values=values,
            state='readonly'
        )
        if layout_type == LayoutType.GRID:
            dbox.grid(row=grid_row, column=grid_col)
            self.is_grid_enabled = True
        if default_value is not None:
            idx = 0
            found = False
            while idx < len(values):
                if default_value == values[idx]:
                    found = True
                    break
                idx += 1
            if found:
                dbox.current(idx)
        if select_callback is not None:
            dbox.bind("<<ComboboxSelected>>", select_callback)
        self.widgets[name] = dbox

    def add_spinbox(
        self,
        name: str,
        lower_limit: float,
        upper_limit: float,
        increment: float = 1.,
        frame_name: str = "default",
        layout_type: LayoutType = LayoutType.DEFAULT,
        grid_row: int = 0,
        grid_col: int = 0
    ) -> None:
        frm = self.frame[frame_name].frame
        spin = tk.Spinbox(
            frm,
            from_=lower_limit,
            to=upper_limit,
            increment=increment
        )
        if layout_type == LayoutType.GRID:
            spin.grid(row=grid_row, column=grid_col)
            self.is_grid_enabled = True
        self.widgets[name] = spin

    def add_slider(
        self,
        name: str,
        default_val: float,
        lower_limit: float,
        upper_limit: float,
        length: int,
        slide_callback: Any,
        orient: Orient = Orient.HORIZONTAL,
        need_float_precision: bool = True,
        frame_name: str = "default",
        layout_type: LayoutType = LayoutType.DEFAULT,
        grid_row: int = 0,
        grid_col: int = 0
    ) -> None:
        frm = self.frame[frame_name].frame
        scalev = tk.DoubleVar() if need_float_precision else tk.IntVar()
        defv = default_val if default_val >= lower_limit \
            and default_val <= upper_limit else lower_limit
        scalev.set(defv)

        slider = tk.Scale(
            frm,
            from_=lower_limit,
            to=upper_limit,
            variable=scalev,
            orient=orient.value,
            length=length,
            command=slide_callback
        )

        if layout_type == LayoutType.GRID:
            slider.grid(row=grid_row, column=grid_col)
            self.is_grid_enabled = True

        self.widgets[f"{name}_val"] = scalev
        self.widgets[name] = slider

        if slide_callback is not None:
            slider.bind("")

    def add_menu(self, name: str, tear_off: bool = False) -> None:
        if self.menubar is None:
            self.menubar = tk.Menu(self.frame["default"].frame)
        self.menus[name] = tk.Menu(self.menubar, tearoff=False)

    def add_menuitem(
        self,
        target_name: str,
        label: str,
        cmd: Optional[Any]
    ) -> None:
        if self.menubar is None:
            raise Exception("menu must be created")
        if target_name not in self.menus:
            raise Exception(f"menu {target_name} not found")
        self.menus[target_name].add_command(
            label=label,
            command=cmd
        )

    def add_menu_separator(
        self,
        target_name: str
    ) -> None:
        if self.menubar is None:
            raise Exception("menu must be created")
        if target_name not in self.menus:
            raise Exception(f"menu {target_name} not found")
        self.menus[target_name].add_separator()

    def build(self):
        self.root.title(self.title)
        self.root.geometry(self._to_geometry())
        if self.menubar is not None:
            for label, menu in self.menus.items():
                self.menubar.add_cascade(
                    label=label,
                    menu=menu
                )
            self.root["menu"] = self.menubar
        if not self.is_grid_enabled:
            [w.pack() for n, w in self.widgets.items() if not n.endswith("_val")]
        else:
            for _,frame in self.frame.items():
                frame.frame.pack(padx = frame.padx, pady = frame.pady)
        return self.root


def open_file_dialog_for_fpath(
        filetypes: List[FileDialogFileType],
        init_dir: str,
        title: str
) -> str:
    flist = list(map(lambda ftype: ftype.as_tuple(), filetypes))
    return fdlg.askopenfilename(
        initialdir=init_dir,
        filetypes=flist,
        title=title
    )


def open_file_dialog_for_write_fpath(
        filetypes: List[FileDialogFileType],
        init_dir: str,
        title: str
) -> str:
    flist = list(map(lambda ftype: ftype.as_tuple(), filetypes))
    return fdlg.asksaveasfilename(
        initialdir=init_dir,
        filetypes=flist,
        title=title
    )


def open_file_dialog_for_dir(
        init_dir: str,
        title: str
) -> str:
    return fdlg.askdirectory(
        initialdir=init_dir,
        title=title
    )
