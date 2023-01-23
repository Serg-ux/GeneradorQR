import qrcode
# Crear una instancia de la clase QRCode
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
# Agregar el mensaje a codificar
print("Ingrese el texto a codificar, escribe exit para salir")
data = input()
qr.add_data(data)
qr.make(fit=True)

# Crear la imagen del código QR
img = qr.make_image(fill_color="black", back_color="white")

# Guardar la imagen en disco
img.save("codigo_qr1.png")
