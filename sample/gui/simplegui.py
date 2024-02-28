from tlib.gui.guibase import *
import tkinter.messagebox as tkm

gm_ref = None
cnt = 0


def btn1_left_clicked(event: tk.Event):
    global gm_ref
    global cnt
    cnt += 1
    ipt = gm_ref.widgets['ipt']
    msg = f"input str is {ipt.get()}. clicked {cnt} times."
    tkm.showinfo("btn1 left evt", msg)
    ipt.delete(0, tk.END)


def main():
    global gm_ref
    gb = GUIManager("takori", 200, 500, 640, 480)
    gb.add_label("l1", "Hello")
    gb.add_label("l2", "Cat")
    gb.add_textbox("ipt")
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
