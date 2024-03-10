from tlib.gui.guibase import *

gm_ref = None


def main():
    global gm_ref
    gb = GUIManager("takori", 200, 500, 640, 480)
    gb.add_frame("lower_section")

    gb.add_checkbox("chk1", "", True,
                    layout_type=LayoutType.GRID,
                    grid_row=0,
                    grid_col=0)
    gb.add_label(
        "l1", "TANU TANUKI",
        layout_type=LayoutType.GRID,
        grid_row=0,
        grid_col=1
    )
    gb.add_textbox(
        "ipt1",
        layout_type=LayoutType.GRID,
        grid_row=0,
        grid_col=2
    )

    gb.add_checkbox(
        "chk2",
        "",
        True,
        layout_type=LayoutType.GRID,
        grid_row=1,
        grid_col=0
    )
    gb.add_label(
        "l2",
        "USHI-CHAN",
        layout_type=LayoutType.GRID,
        grid_row=1,
        grid_col=1
    )
    gb.add_textbox(
        "ipt2",
        layout_type=LayoutType.GRID,
        grid_row=1,
        grid_col=2
    )

    gb.add_label(
        name="f2l1",
        text="たこじゃん..",
        frame_name="lower_section",
        layout_type=LayoutType.GRID,
        grid_row=0,
        grid_col=1
    )
    gb.add_label(
        name="f2l2",
        text="いかです..",
        frame_name="lower_section",
        layout_type=LayoutType.GRID,
        grid_row=0,
        grid_col=2
    )

    r = gb.build()
    gm_ref = gb
    r.mainloop()


if __name__ == "__main__":
    main()
