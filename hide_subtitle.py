from tkinter import *

COLOR = "gray"
geometry = {
    "width": 1500,
    "height": 100,
    "x": 200,
    "y": 200
}


def update_geometry():
    root.geometry(f"{geometry['width']}x{geometry['height']}+{geometry['x']}+{geometry['y']}")


root = Tk()
root.overrideredirect(True)
root.wait_visibility(root)
root.attributes("-alpha", 1)
update_geometry()

title_bar = Frame(
    root,
    bg=COLOR,
    background=COLOR,
    highlightbackground=COLOR,
    highlightcolor=COLOR,
    relief="raised",
)
title_bar.pack(fill=BOTH)


def get_pos(event):
    xwin = root.winfo_x()
    ywin = root.winfo_y()
    startx = event.x_root
    starty = event.y_root

    xwin = xwin - startx
    ywin = ywin - starty

    def move_window(event):
        geometry["x"] = event.x_root + xwin
        geometry["y"] = event.y_root + ywin
        update_geometry()

    title_bar.bind("<B1-Motion>", move_window)


title_bar.bind("<Button-1>", get_pos)

close_button = Button(
    title_bar,
    # activebackground=BLACK,
    activeforeground=COLOR,
    borderwidth=0,
    background=COLOR,
    foreground=COLOR,
    highlightbackground=COLOR,
    highlightcolor=COLOR,
    text="x",
    command=root.destroy
)
close_button.pack(side=RIGHT)


def resize_x(event):
    xwin = root.winfo_x()
    difference = (event.x_root - xwin) - root.winfo_width()
    if root.winfo_width() > 100:  # 150 is the minimum width for the window
        pass
    elif difference > 0:  # so the window can't be too small (150x150)
        pass
    else:
        return

    try:
        geometry["width"] = root.winfo_width() + difference
        update_geometry()
    except:
        pass


def resize_y(event):
    ywin = root.winfo_y()
    difference = (event.y_root - ywin) - root.winfo_height()
    if root.winfo_height() > 100:  # 150 is the minimum height for the window
        pass
    elif difference > 0:  # so the window can't be too small (150x150)
        pass
    else:
        return

    try:
        geometry["height"] = root.winfo_height() + difference
        update_geometry()
    except:
        pass


resize_x_widget = Frame(
    root,
    cursor='sb_h_double_arrow',
    bg=COLOR,
    background=COLOR,
    highlightbackground=COLOR,
    highlightcolor=COLOR,
)
resize_x_widget.bind("<B1-Motion>", resize_x)
resize_x_widget.pack(side=RIGHT, ipadx=3.0, fill=Y)

resize_y_widget = Frame(
    root,
    cursor='sb_v_double_arrow',
    bg=COLOR,
    background=COLOR,
    highlightbackground=COLOR,
    highlightcolor=COLOR,
)
resize_y_widget.bind("<B1-Motion>", resize_y)
resize_y_widget.pack(side=BOTTOM, ipady=3.0, fill=X)

window = Canvas(
    root,
    bg=COLOR,
    background=COLOR,
    highlightbackground=COLOR,
    highlightcolor=COLOR
)
window.pack(expand=1, fill=BOTH)

root.mainloop()
