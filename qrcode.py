import pyqrcode
from json import dumps
data = {
    "fullname":"Kumar Asirwad Mishra",
    "phone_no":811490767,
    "hope":"om sai ram"
}
s = dumps(data)
big_code = pyqrcode.create(s, error='L', version=27, mode='binary')
big_code.png('code.png', scale=2, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])