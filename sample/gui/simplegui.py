from tlib.gui.guibase import *
import tkinter.messagebox as tkm

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
    msg = f"input str is {ipt.get()}. clicked {cnt} times. \
        also radio chosen {radv.get()}"
    if chk1.get():
        msg = f"[=^_^=]{msg}"
    tkm.showinfo("?", bbs.get('1.0', tk.END))
    bbs.delete('1.0', tk.END)
    bbs.insert(tk.END, msg)
    ipt.delete(0, tk.END)


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
        default_val=1
    )
    gb.add_button(
        "btn1",
        "click this button",
        [EventCallBack(GUIEvent.EVT_LEFTCLICK, btn1_left_clicked)]
    )
    r = gb.build()
    gm_ref = gb
    r.mainloop()


if __name__ == "__main__":
    main()
