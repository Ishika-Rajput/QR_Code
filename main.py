import qrcode
from PILTools import Image
qr = qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4)
qr.add_data("https://www.youtube.com/watch?v=-fxA5IAh_ZA")
qr.make(fit=True)
img = qr.make_image(fill_color="white",back_color="black")
img.save("Tum hi ho.png")