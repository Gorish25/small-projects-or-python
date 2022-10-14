import qrcode as qr
img=qr.make("https://www.w3schools.com/python/default.asp")
img.save('w3schools_python_tutorial.png')