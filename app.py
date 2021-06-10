#performing flask imports
from flask import Flask,jsonify,send_file,request
from transform import Transform
from filter import HongAnh
from PIL import Image
from flask_cors import CORS
from saturated import Saturated
from brightness import Brightness
import time


app = Flask(__name__) 
CORS(app)


filename = 'output/output.png'
# time = str(int(round(time.time()*1000)))
def resize():
    im = Image.open(filename)
    im.thumbnail((150, 150))
    im.save(filename)

@app.route('/', methods = ['GET'])
def index():
    return jsonify({'greetings' : 'Hello'}) 

@app.route('/get_image', methods = ['GET'])
def get_image():
    return send_file(filename, mimetype='image', attachment_filename='output.png')

@app.route('/post_image/high_contrast', methods = ['POST']) 
def post_image1():
    input_path='input/'
    file = request.files['image']
    file.save(input_path+'im-received.png')
    Transform(f='im-received.png', filter='HighContrast')
    resize()
    return " "

@app.route('/post_image/web/high_contrast', methods = ['POST']) 
def post_image11():
    input_path='input/'
    file = request.files['image']
    file.save(input_path+'im-received.png')
    Transform(f='im-received.png', filter='HighContrast')
    return " "

@app.route('/post_image/electric', methods = ['POST']) 
def post_image2():
    input_path='input/'
    file = request.files['image']
    file.save(input_path+'im-received.png')
    Transform(f='im-received.png', filter='Electric')
    resize()
    return " "

@app.route('/post_image/web/electric', methods = ['POST']) 
def post_image12():
    input_path='input/'
    file = request.files['image']
    file.save(input_path+'im-received.png')
    Transform(f='im-received.png', filter='Electric')
    return " "

@app.route('/post_image/darkened', methods = ['POST']) 
def post_image3():
    input_path='input/'
    file = request.files['image']
    file.save(input_path+'im-received.png')
    Transform(f='im-received.png', filter='Darkened')
    resize()
    return " "

@app.route('/post_image/web/darkened', methods = ['POST']) 
def post_image13():
    input_path='input/'
    file = request.files['image']
    file.save(input_path+'im-received.png')
    Transform(f='im-received.png', filter='Darkened')
    return " "

@app.route('/post_image/censored', methods = ['POST']) 
def post_image4():
    input_path='input/'
    file = request.files['image']
    file.save(input_path+'im-received.png')
    Transform(f='im-received.png', filter='Censored')
    resize()
    return " "

@app.route('/post_image/web/censored', methods = ['POST']) 
def post_image14():
    input_path='input/'
    file = request.files['image']
    file.save(input_path+'im-received.png')
    Transform(f='im-received.png', filter='Censored')
    return " "

@app.route('/post_image/vintage', methods = ['POST']) 
def post_image5():
    input_path='input/'
    file = request.files['image']
    file.save(input_path+'im-received.png')
    Transform(f='im-received.png', filter='Vintage')
    resize()
    return " "

@app.route('/post_image/web/vintage', methods = ['POST']) 
def post_image15():
    input_path='input/'
    file = request.files['image']
    file.save(input_path+'im-received.png')
    Transform(f='im-received.png', filter='Vintage')
    return " "

@app.route('/post_image/grayscale', methods = ['POST']) 
def post_image6():
    input_path='input/'
    file = request.files['image']
    file.save(input_path+'im-received.png')
    image = Image.open(input_path+'im-received.png')
    if image.mode != 'RGB':
        image = image.convert('RGB')
        image.save(input_path+'im-received.png')
    HongAnh(f='im-received.png', filter='GreyScale')
    resize()
    return " "

@app.route('/post_image/web/grayscale', methods = ['POST']) 
def post_image16():
    input_path='input/'
    file = request.files['image']
    file.save(input_path+'im-received.png')
    image = Image.open(input_path+'im-received.png')
    if image.mode != 'RGB':
        image = image.convert('RGB')
        image.save(input_path+'im-received.png')
    HongAnh(f='im-received.png', filter='GreyScale')
    return " "

@app.route('/post_image/sepia', methods = ['POST']) 
def post_image7():
    input_path='input/'
    file = request.files['image']
    file.save(input_path+'im-received.png')
    image = Image.open(input_path+'im-received.png')
    if image.mode != 'RGB':
        image = image.convert('RGB')
        image.save(input_path+'im-received.png')
    HongAnh(f='im-received.png', filter='Sepia')
    resize()
    return " "

@app.route('/post_image/web/sepia', methods = ['POST']) 
def post_image17():
    input_path='input/'
    file = request.files['image']
    file.save(input_path+'im-received.png')
    image = Image.open(input_path+'im-received.png')
    if image.mode != 'RGB':
        image = image.convert('RGB')
        image.save(input_path+'im-received.png')
    HongAnh(f='im-received.png', filter='Sepia')
    return " "

@app.route('/post_image/invert', methods = ['POST']) 
def post_image8():
    input_path='input/'
    file = request.files['image']
    file.save(input_path+'im-received.png')
    image = Image.open(input_path+'im-received.png')
    if image.mode != 'RGB':
        image = image.convert('RGB')
        image.save(input_path+'im-received.png')
    HongAnh(f='im-received.png', filter='Invert')
    resize()
    return " "

@app.route('/post_image/web/invert', methods = ['POST']) 
def post_image18():
    input_path='input/'
    file = request.files['image']
    file.save(input_path+'im-received.png')
    image = Image.open(input_path+'im-received.png')
    if image.mode != 'RGB':
        image = image.convert('RGB')
        image.save(input_path+'im-received.png')
    HongAnh(f='im-received.png', filter='Invert')
    return " "

@app.route('/post_image/brightness', methods = ['POST']) 
def post_image9():
    input_path='input/'
    file = request.files['image']
    file.save(input_path+'im-received.png')
    image = Image.open(input_path+'im-received.png')
    if image.mode != 'RGB':
        image = image.convert('RGB')
        image.save(input_path+'im-received.png')
    Brightness(f='im-received.png')
    resize()
    return " "

@app.route('/post_image/web/brightness', methods = ['POST']) 
def post_image19():
    input_path='input/'
    file = request.files['image']
    file.save(input_path+'im-received.png')
    image = Image.open(input_path+'im-received.png')
    if image.mode != 'RGB':
        image = image.convert('RGB')
        image.save(input_path+'im-received.png')
    Brightness(f='im-received.png')
    return " "

@app.route('/post_image/saturated', methods = ['POST']) 
def post_image10():
    input_path='input/'
    file = request.files['image']
    file.save(input_path+'im-received.png')
    image = Image.open(input_path+'im-received.png')
    if image.mode != 'RGB':
        image = image.convert('RGB')
        image.save(input_path+'im-received.png')
    Saturated(f='im-received.png')
    resize()
    return " "

@app.route('/post_image/web/saturated', methods = ['POST']) 
def post_image20():
    input_path='input/'
    file = request.files['image']
    file.save(input_path+'im-received.png')
    image = Image.open(input_path+'im-received.png')
    if image.mode != 'RGB':
        image = image.convert('RGB')
        image.save(input_path+'im-received.png')
    Saturated(f='im-received.png')
    return " "


if __name__ == "__main__":
    app.run(host='192.168.1.47', debug = True) #debug will allow changes without shutting down the server 

