# -*- coding: utf-8 -*-

def recognize(img):
    import easyocr
    reader = easyocr.Reader(['ch_tra','en']) 
    result = reader.readtext(img, detail = 0)
    return result

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

from flask import Flask, render_template, request, jsonify, flash
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def upload_file():
   return render_template('index.html', host =  request.headers.get('Host'))
	
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file2():
    import cv2
    import numpy 
    if request.method == 'POST':
        f = request.files['file']
        if not (f and allowed_file(f.filename)):
            return jsonify({"error": 1001, "msg": "上傳圖片格式限定為 : png、PNG、jpg、JPG、bmp"})

        #   存圖
        f.save(r'static\upload_img\\' + f.filename)
        img = cv2.imread(r'static\upload_img\\' + f.filename)

        #   不存圖
        # npimg = numpy.fromstring(f.read(), numpy.uint8)
        # img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        #   辨識
        res = recognize(img)
        if res:
            return f'{res}'
        else:
            return '辨識圖片內沒有字元'

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port = 5000)


   