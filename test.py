from Tkinter import *
import pyqrcode
from json import dumps
from os import getcwd,path
from time import sleep
import serial
import requests

def listen_stick(port,listen):
	while True:
		try:
			loc = "/dev/tty%s"%(port)
			s = serial.Serial(loc,listen)
			data = None
			li = list()
			go = 1
			while True:
				l = s.readline()
				if go == 1:
					data = None
					li = list()
					if "Start" in l:
						print("strat")
						while True:
							l =s.readline()
							if "End" in l:
								print("end")
								data = dict(li)
								if len(data) == 9:
									go = 0
									break
								go = 1
								break
							try:
								l = l[:-2]
								if l != "":
									li.append(l.split(":"))
							except:
								pass
				elif go == 0:
					return data

def create_qrcode(data):
    s = dumps(data)
    big_code = pyqrcode.create(s, error='L', version=27, mode='binary')
    big_code.png('code.png', scale=2, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
    qr_code_file.configure(file=path.join(getcwd(),"code.png"))
    right_canvas.itemconfig(qrcode, image=qr_code_file)
    

def clicked(event):
    #create_qrcode()
    print("Sai ram")

window = Tk()
window.title("Anapurna")

#top canvas for the screen
top_canvas = Canvas(window,width=700,height=70, bg="red")
top_canvas.grid(row=0,column=0,columnspan=2, sticky=N)
app_name = top_canvas.create_text( (120,30),text="Anapurna", font=("Arial Bold",30))
x_cord = 550
y_cord=15
status_box = top_canvas.create_rectangle(x_cord,y_cord,x_cord+45,y_cord+45, fill="blue")

#left middle for details for screen
left_canvas = Canvas(window, width=300,height=360, bg="pink")
left_canvas.grid(row=1,column=0,rowspan=1, sticky=E)
tile_left = left_canvas.create_text((110,30), text = "Sensor Data", font=("Arial ", 20,"italic"))
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

base_x = 50
base_y = 70
labels["temp"] = left_canvas.create_text((base_x,base_y), text=sensor_labels["temp"], font = ("Arial", 10))
labels["mois"] = left_canvas.create_text((base_x-10,base_y+15), text=sensor_labels["mois"], font = ("Arial", 10))
labels["humi"] = left_canvas.create_text((base_x-10,base_y+30), text=sensor_labels["humi"], font = ("Arial", 10))
labels["tds"] = left_canvas.create_text((base_x-25,base_y+45), text=sensor_labels["tds"], font = ("Arial", 10))
labels["ph"] = left_canvas.create_text((base_x-26,base_y+60), text=sensor_labels["ph"], font = ("Arial", 10))
labels["tubi"] = left_canvas.create_text((base_x-10,base_y+75), text=sensor_labels["tubi"], font = ("Arial", 10))
labels["phos"] = left_canvas.create_text((base_x-3,base_y+90), text=sensor_labels["phos"], font = ("Arial", 10))
labels["pota"] = left_canvas.create_text((base_x-8,base_y+105), text=sensor_labels["pota"], font = ("Arial", 10))
labels["nitro"] = left_canvas.create_text((base_x-9,base_y+120), text=sensor_labels["nitro"], font = ("Arial", 10))


change_label["temp"] = left_canvas.create_text((base_x+120,base_y),text="0.0", font = ("Arial", 10))
change_label["mois"] = left_canvas.create_text((base_x-20+140,base_y+15), text="0.0", font = ("Arial", 10))
change_label["humi"] = left_canvas.create_text((base_x-20+140,base_y+30),text="0.0", font = ("Arial", 10))
change_label["tds"] = left_canvas.create_text((base_x-45+165,base_y+45), text="0.0", font = ("Arial", 10))
change_label["ph"] = left_canvas.create_text((base_x-54+173,base_y+60), text="0.0", font = ("Arial", 10))
change_label["tubi"] = left_canvas.create_text((base_x-20+140,base_y+75), text="0.0", font = ("Arial", 10))
change_label["phos"] = left_canvas.create_text((base_x+127,base_y+90), text="0.0%", font = ("Arial", 10))
change_label["pota"] = left_canvas.create_text((base_x-17+145,base_y+105), text="0.0%", font = ("Arial", 10))
change_label["nitro"] = left_canvas.create_text((base_x-20+147,base_y+120), text="0.0%", font = ("Arial", 10))

button = left_canvas.create_rectangle(20,250,220,280,fill="blue")
click = left_canvas.create_text((130,265),text="Take a Sample", font=("Arial Bold", 10))
left_canvas.tag_bind(button, "<Button-1>", clicked)
left_canvas.tag_bind(click, "<Button-1>", clicked)

#right middle for the details for screen
right_canvas = Canvas(window, width=400,height=360, bg="yellow")
right_canvas.grid(row=1,column=1,rowspan=2,sticky=W)

label_qrcode = right_canvas.create_text((160,30), text = "QR-CODE", font = ("Arial Bold", 20))

qr_code_file = PhotoImage(file=path.join(getcwd(),"code.png"))
qrcode =right_canvas.create_image(150, 190, image=qr_code_file)
window.mainloop()