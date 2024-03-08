from tlib.gui.guibase import *
import tkinter.messagebox as tkm
import os

gm_ref = None
cnt = 0


def btn1_left_clicked(event: tk.Event):
    global gm_ref
    global cnt
    cnt += 1
    ipt = gm_ref.widgets['ipt']
    bbs = gm_ref.widgets['bbs']
    chk1 = gm_ref.widgets['chk1_val']
    radv = gm_ref.widgets['myradio_val']
    spin = gm_ref.widgets['myspin']
    msg = f"input str is {ipt.get()}. clicked {cnt} times. \
        also radio chosen {radv.get()} + spin {spin.get()}"
    if chk1.get():
        msg = f"[=^_^=]{msg}"
    tkm.showinfo("?", bbs.get('1.0', tk.END))
    bbs.delete('1.0', tk.END)
    bbs.insert(tk.END, msg)
    ipt.delete(0, tk.END)


def listbox_sel(event: tk.Event):
    global gm_ref
    lv = gm_ref.widgets["mylist"]

    msg = f"{lv.curselection()} is chosen"
    tkm.showinfo("list", msg)


def dropbox_sel(event: tk.Event):
    global gm_ref
    dbox = gm_ref.widgets["mydrop"]
    msg = f"dropdown selected item is {dbox.get()}"
    tkm.showinfo("dropdown!", msg)


def slider_move(event: tk.Event):
    global gm_ref
    variable = gm_ref.widgets['myslide_val']
    print(f"slide:{variable.get()}")


def menu_open_hit():
    fp = [FileDialogFileType("python", "*.py")]
    lib_home = os.environ["TANULIB_HOME"]

    fpath = open_file_dialog_for_fpath(
        filetypes=fp,
        init_dir=lib_home,
        title="open file"
    )
    tkm.showinfo("file opened", f"trying to open {fpath}..")


def menu_dir_hit():
    lib_home = os.environ["TANULIB_HOME"]

    fpath = open_file_dialog_for_dir(
        init_dir=lib_home,
        title="open dir"
    )
    if fpath != "":
        tkm.showinfo("dir opened", f"trying to open {fpath}..")


def menu_save_hit():
    global gm_ref

    bbs = gm_ref.widgets['bbs']

    fp = [FileDialogFileType("text file", "*.txt")]
    lib_home = os.environ["TANULIB_HOME"]

    wpath = open_file_dialog_for_write_fpath(
        filetypes=fp,
        init_dir=lib_home,
        title="書き込む。"
    )
    with open(wpath, "w") as fp:
        bbs_s = bbs.get('1.0', tk.END)
        fp.write(bbs_s)


def menu_close_hit():
    tkm.showwarning("CLOSE", "close!")


def menu_help_hit():
    tkm.showinfo("hint..", "HINT?")


def menu_version_hit():
    tkm.showinfo("VERSION", "0.1.0")


def main():
    global gm_ref
    gb = GUIManager("takori", 200, 500, 640, 480)
    gb.add_label("l1", "Hello")
    gb.add_label("l2", "Cat")
    gb.add_textbox("ipt")
    gb.add_textarea(
        name='bbs',
        width=60,
        height=10,
        wrap=tk.WORD,
        default_str="たこなのか?",
        with_scrollbar=True
    )
    gb.add_checkbox("chk1", "add PREFIX [=^_^=]", True)
    gb.add_radiobutton(
        name="myradio",
        text_and_vals=[("ねこ", 1), ("いぬ", 2)],
        default_val=1,
        label_frame_value="RADIO GRP"
    )
    gb.add_listbox(
        name="mylist",
        values=['tako', 'neko', 'piko'],
        select_mode=SelectMode.SINGLE,
        default_value="piko",
        select_callback=listbox_sel
    )
    gb.add_dropdownbox(
        name="mydrop",
        values=("Sapporo", "Tokyo", "Osaka", "Kyoto"),
        default_value="Tokyo",
        select_callback=dropbox_sel
    )
    gb.add_spinbox(
        name="myspin",
        lower_limit=0,
        upper_limit=10,
        increment=0.5
    )
    gb.add_slider(
        name="myslide",
        default_val=10.,
        lower_limit=0,
        upper_limit=50.,
        length=150,
        slide_callback=slider_move
    )
    gb.add_button(
        "btn1",
        "click this button",
        [EventCallBack(GUIEvent.EVT_LEFTCLICK, btn1_left_clicked)]
    )

    gb.add_menu("File")
    gb.add_menu("Option")
    gb.add_menuitem("File", "Open", menu_open_hit)
    gb.add_menuitem("File", "Save", menu_save_hit)
    gb.add_menuitem("File", "Directory", menu_dir_hit)
    gb.add_menuitem("File", "Close", menu_close_hit)
    gb.add_menuitem("Option", "Help", menu_help_hit)
    gb.add_menu_separator("Option")
    gb.add_menuitem("Option", "Version", menu_version_hit)

    r = gb.build()
    gm_ref = gb
    r.mainloop()


if __name__ == "__main__":
    main()
