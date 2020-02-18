from tkinter import *

class Display:
    "this will render the display of the touch screen"

    def __init__(self):
        self.width  = 835
        self.height = 472
        self.window = Tk()
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.title("Anapurna")
        self.top_canas = Canvas(self.window, width=self.width, height=50, bg="red")
        self.top_cavas_decoration()
        self.left_canvas = Canvas(self.window, width=self.width*0.75, height=300, bg="pink")
        self.left_canvas_decoration()
        self.right_canvas = Canvas(self.window, width=self.width - self.width*0.75, height=300, bg="black")
        self.right_canvas_decoration()
        self.run()
    
    def top_cavas_decoration(self):
        "this will perform the top canvas decoration and all required task"
        self.top_canas.grid(row=0, column=0, columnspan=2, sticky=N)
    
    def right_canvas_decoration(self):
        "this will perform the right canvas decoration and all required task"
        self.right_canvas.grid(row=1, column=1, rowspan=1, sticky=E)

    def left_canvas_decoration(self):
        "this will perform the left canvas decoration and all required task"
        self.left_canvas.grid(row=1, column=0, rowspan=1, sticky=W)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    d = Display()

"""
width = 22.1cm => 835.27559
heigth=12.5cm => 472.440944
"""