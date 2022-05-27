#create
import pyqrcode

content = 'This QRcode is sample.'
c = pyqrcode.create(content=content, error='H')
c.png(file='C:/Users/NAOKUN/Desktop/Python/QRcode/Create_QRcode/QRcode.png', scale=6)

#read
from pyzbar.pyzbar import decode
from PIL import Image

d = decode(Image.open('file-path'))
print(d[0].data.decode('utf-8'))