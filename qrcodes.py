import qrcode
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import json

## Variablen
songs = json.load(open("songs.json"))
strFont = "Raleway-ExtraBold.ttf"
strBGcolor = "#ffffff"
strFGcolor = "#1a1a1a"

for song in songs:
    ## Noch mehr Variablen!
    strGuid = song["Guid"]
    strDay = song["Day"]
    strClaim = song["Claim"]

    ## QR-Code erstelen
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=20,
        border=4,
    )

    qr.add_data('https://www.friedersdorf.de/adventskalender/index.php?tag='+strGuid)
    qr.make(fit=True)
    img = qr.make_image(fill_color = strFGcolor, back_color=strBGcolor).convert('RGB')
    imgW, imgH = img.size

    ## Nummer zeichnen
    font = ImageFont.truetype(strFont, 70, encoding="unic")
    W, H = (200,200)
    draw = ImageDraw.Draw(img)
    draw.ellipse((imgW/2-W/2, imgH/2-H/2, imgW/2+W/2, imgH/2+H/2), fill=strBGcolor, outline=strFGcolor, width=10)
    w, h = draw.textsize(strDay, font=font)
    draw.text(((imgW-w)/2,(imgH-h)/2), strDay, fill=strFGcolor, font=font)

    ## Neues Bild erstellen, aber groeßer
    imgNew = Image.new("RGBA", (imgW, imgH+150), strBGcolor)
    imgNew.paste(img, (0,0))

    ## Claim reinschreiben
    draw = ImageDraw.Draw(imgNew)
    font = ImageFont.truetype(strFont, 50, encoding="unic")
    w, h = draw.textsize(strClaim, font=font)
    draw.text(((imgW-w)/2, 1000), strClaim, fill=strFGcolor, font=font)

    imgNew.save("qrcodes/" + strGuid + ".png")
