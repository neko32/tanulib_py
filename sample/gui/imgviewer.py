from tlib.gui.guibase import *
import os

gm_ref = None

basedir = os.environ["HOME_TMP_DIR"]


def open_image_file(event: tk.Event):
    global gm_ref
    global basedir
    print("opening an image file..")
    fname, img = get_image_from_file_dialog(
        init_dir=basedir,
        title="Select an image file to load..",
        filetypes=default_file_dialog_file_type_for_image(),
    )
    gm_ref.widgets[fname] = img
    cvs = gm_ref.widgets['imgcanvas']
    cvs.create_image((0, 0), image=img)
    cvs.update_idletasks()


def main():
    global gm_ref
    gb = GUIManager("Image Viewer", 200, 500, 800, 800)
    gb.add_canvas_for_image(
        name="imgcanvas",
        width=700,
        height=700
    )
    gb.add_button(
        "open_image_btn",
        "Open Image",
        [EventCallBack(GUIEvent.EVT_LEFTCLICK, open_image_file)]
    )

    r = gb.build()
    gm_ref = gb
    r.mainloop()


if __name__ == "__main__":
    main()
