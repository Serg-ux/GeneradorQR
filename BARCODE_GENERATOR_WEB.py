import qrcode
#crea el objeto QR
qr = qrcode.QRCode(version=1, box_size=10, border=5)
#agrega la url
qr.add_data("https://github.com/Serg-ux")
#hace que el código QR se dibuje
qr.make(fit=True)
#crea una imagen a partir del codigo
img = qr.make_image(fill_color="black", back_color="white")
#guarda la imagen en el disco
img.save("qr.png")