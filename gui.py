from tkinter import *
import pyqrcode
from json import dumps
from os import getcwd,path
from time import sleep

def create_qrcode(data):
    s = dumps(data)
    big_code = pyqrcode.create(s, error='L', version=27, mode='binary')
    big_code.png('code.png', scale=2, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
    qr_code_file.configure(file=path.join(getcwd(),"code.png"))
    right_canvas.itemconfig(qrcode, image=qr_code_file)

def update_content(data):
    pass

def clicked(event):
    pass

window = Tk()
window.title("Anapurna")

#top canvas for the screen
top_canvas = Canvas(window,width=1015,height=100, bg="red")
top_canvas.grid(row=0,column=0,columnspan=2, sticky=N)
app_name = top_canvas.create_text( (220,50),text="Anapurna", font=("Arial Bold",70))
x_cord = 930
y_cord=20
status_box = top_canvas.create_rectangle(x_cord,y_cord,x_cord+60,y_cord+60, fill="blue")

#left middle for details for screen
left_canvas = Canvas(window, width=500,height=400, bg="pink")
left_canvas.grid(row=1,column=0,rowspan=1, sticky=E)

tile_left = left_canvas.create_text((170,30), text = "Sensor Data", font=("Arial ", 45,"italic"))
sensor_labels = {
    "temp":"Temperature",
    "mois":"Moisture",
    "humi":"Humidity",
    "tds":"TDS",
    "ph":"Ph",
    "tubi":"Turbidity",
    "phos":"Phosphorus",
    "pota":"Potasium",
    "nitro":"Nitrogen",
}
labels = {
    "temp":None,
    "mois":None,
    "humi":None,
    "tds":None,
    "ph":None,
    "tubi":None,
    "phos":None,
    "pota":None,
    "nitro":None
}

change_data = {
    "temp":StringVar,
    "mois":StringVar,
    "humi":StringVar,
    "tds":StringVar,
    "ph":StringVar,
    "tubi":StringVar,
    "phos":StringVar,
    "pota":StringVar,
    "nitro":StringVar
}
change_label = {
    "temp":None,
    "mois":None,
    "humi":None,
    "tds":None,
    "ph":None,
    "tubi":None,
    "phos":None,
    "pota":None,
    "nitro":None
}

base_x = 90
base_y = 100
labels["temp"] = left_canvas.create_text((base_x,base_y), text=sensor_labels["temp"], font = ("Arial", 20))
labels["mois"] = left_canvas.create_text((base_x-20,base_y+30), text=sensor_labels["mois"], font = ("Arial", 20))
labels["humi"] = left_canvas.create_text((base_x-20,base_y+60), text=sensor_labels["humi"], font = ("Arial", 20))
labels["tds"] = left_canvas.create_text((base_x-45,base_y+90), text=sensor_labels["tds"], font = ("Arial", 20))
labels["ph"] = left_canvas.create_text((base_x-54,base_y+120), text=sensor_labels["ph"], font = ("Arial", 20))
labels["tubi"] = left_canvas.create_text((base_x-20,base_y+150), text=sensor_labels["tubi"], font = ("Arial", 20))
labels["phos"] = left_canvas.create_text((base_x,base_y+180), text=sensor_labels["phos"], font = ("Arial", 20))
labels["pota"] = left_canvas.create_text((base_x-17,base_y+210), text=sensor_labels["pota"], font = ("Arial", 20))
labels["nitro"] = left_canvas.create_text((base_x-20,base_y+240), text=sensor_labels["nitro"], font = ("Arial", 20))


change_label["temp"] = left_canvas.create_text((base_x+120,base_y), text="0.0", font = ("Arial", 20))
change_label["mois"] = left_canvas.create_text((base_x-20+140,base_y+30), text="0.0", font = ("Arial", 20))
change_label["humi"] = left_canvas.create_text((base_x-20+140,base_y+60), text="0.0", font = ("Arial", 20))
change_label["tds"] = left_canvas.create_text((base_x-45+165,base_y+90), text="0.0", font = ("Arial", 20))
change_label["ph"] = left_canvas.create_text((base_x-54+173,base_y+120), text="0.0", font = ("Arial", 20))
change_label["tubi"] = left_canvas.create_text((base_x-20+140,base_y+150), text="0.0", font = ("Arial", 20))
change_label["phos"] = left_canvas.create_text((base_x+130,base_y+180), text="0.0%", font = ("Arial", 20))
change_label["pota"] = left_canvas.create_text((base_x-17+148,base_y+210), text="0.0%", font = ("Arial", 20))
change_label["nitro"] = left_canvas.create_text((base_x-20+150,base_y+240), text="0.0%", font = ("Arial", 20))


#right middle for the details for screen
right_canvas = Canvas(window, width=515,height=400, bg="yellow")
right_canvas.grid(row=1,column=1,rowspan=1,sticky=W)
label_qrcode = right_canvas.create_text((260,40), text = "QR-CODE", font = ("Arial Bold", 40))
qr_code_file = PhotoImage(file=path.join(getcwd(),"code.png"))
qrcode =right_canvas.create_image(250, 250, image=qr_code_file)

#bottom for the buttom for screen
bottom_canvas = Canvas(window, width=1015,height=60,bg="blue")
bottom_canvas.grid(row=2, column=0,columnspan=2, sticky=S)
button = bottom_canvas.create_rectangle(100,10,920,50,fill="pink")
click = bottom_canvas.create_text((500,30),text="Take a Sample", font=("Arial Bold", 30))
bottom_canvas.tag_bind(button, "<Button-1>", clicked)
bottom_canvas.tag_bind(click, "<Button-1>", clicked)
window.mainloop()


"""
    temp
    potasium
    moisture
    humidity
    nitrogen
    tds
    ph
    turbidity
    phosphorus
"""
