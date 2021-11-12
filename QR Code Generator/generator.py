import qrcode
import image


qr = qrcode.QRCode(
    version=15,
    box_size=5,
    border=5,
)


qr.add_data('https://github.com/MeetMulik')  # <-Enter URL Here
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("qrcode.png")
