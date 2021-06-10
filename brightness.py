from PIL import Image

MIN_COLOR_VALUE=0
MAX_COLOR_VALUE=255
BRIGHTNESS = 50

class Brightness:
    def __init__(self, f=''):
        f='input/' + f
        filepath='output/'
        img = Image.open(f)
        pixels = img.load()

        img_new = Image.new(img.mode, img.size)
        pixels_new = img_new.load()
        for i in range(img_new.size[0]):
            for j in range(img_new.size[1]):
                r,g,b = pixels[i,j]
                _r = self.brighness_filter(r + BRIGHTNESS)
                _b = self.brighness_filter(b + BRIGHTNESS)
                _g = self.brighness_filter(g + BRIGHTNESS)
                pixels_new[i,j] = (_r, _g, _b)
        img_new.save(filepath+'output.png')


    def brighness_filter(self,value):
        if (value < 0):
            return MIN_COLOR_VALUE
        if (value > 255):
            return MAX_COLOR_VALUE
        return value

# if __name__ == "__main__":
#     img = Image.open('D:/python/anh.png/Long-Bien-Bridge.jpg')
#     pixels = img.load()

#     img_new = Image.new(img.mode, img.size)
#     pixels_new = img_new.load()
    

#     for i in range(img_new.size[0]):
#         for j in range(img_new.size[1]):
#             r,g,b = pixels[i,j]
#             _r = brighness_filter(r + BRIGHTNESS)
#             _b = brighness_filter(b + BRIGHTNESS)
#             _g = brighness_filter(g + BRIGHTNESS)
#             pixels_new[i,j] = (_r, _g, _b)
#     img_new.show()