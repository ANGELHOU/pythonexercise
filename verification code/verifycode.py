import Image
import ImageDraw
import ImageFont
import StringIO
import sys
import random
import string
from flask import Flask, send_file

app = Flask(__name__)

path = sys.path[0]
IMGLEN = 4
#base = string.digits + string.letters
base=('0','1','2','3','4','5','6','7','8','9',  
      'A','B','C','D','E','F','G','H','I','J',  
      'K','L','M','N','O','P','Q','R','S','T',  
      'U','V','W','X','Y','Z')

@app.route('/code')
def getcode():
    code = ''
    fontimg = Image.open(path + "/font/font.png")
    codeimg = Image.new('RGBA', (19 * IMGLEN, 25))

    for x in range(IMGLEN):
        #ran = random.randint(0, 61)
        ran = random.randint(0, 35)
        code = ''.join((code, base[ran]))
        img_s = fontimg.crop((ran * 19, 0, (ran + 1) * 19, 20))
        img_s = img_s.rotate(random.randint(-30, 30))
        codeimg.paste(img_s, (x * 19, 2))

    out = StringIO.StringIO()
    codeimg.save(out, 'PNG')
    out.seek(0)
    return send_file(out, mimetype='image/png', cache_timeout=0)

if __name__ == "__main__":
    app.run(debug=True)
