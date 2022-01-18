# program that is generating a Qrcode for my LinkedIn profile, saving it as image and decoding it.
import cv2
import qrcode

# make qrcode and it as image
img = qrcode.make(" www.linkedin.com/in/juliaxixi-xu")
img.save("linkedinProfile.jpg")

# decode generated qrcode
d = cv2.QRCodeDetector()
res = d.detectAndDecode(cv2.imread("linkedinProfile.jpg"))
print("Decoded qrcode is: ", res)
