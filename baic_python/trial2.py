import qrcode
data = 'https://gemini.google.com/app/6d6515487c5340b4'
img = qrcode.make(data)
img.save('qrcode.png')