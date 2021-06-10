from PIL import Image

MIN_COLOR_VALUE=0
MAX_COLOR_VALUE=255
COLOR_THRESDHOLD = 128

class Saturated:
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
                _r = self.brighness_filter(r)
                _b = self.brighness_filter(b)
                _g = self.brighness_filter(g)
                pixels_new[i,j] = (_r, _g, _b)
        img_new.save(filepath+'output.png')

    def brighness_filter(self, value):
        if (value < COLOR_THRESDHOLD):
            return MIN_COLOR_VALUE
        if (value > COLOR_THRESDHOLD):
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
#             _r = brighness_filter(r)
#             _b = brighness_filter(b)
#             _g = brighness_filter(g)
#             pixels_new[i,j] = (_r, _g, _b)
            
#     img_new.show()