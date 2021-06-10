# Include some open-source code to help us load the images
from PIL import Image

class HongAnh:
    # Convert to grey tone

    def __init__(self, f='', filter=''):
        f='input/' + f
        filepath='output/'
        global res
        img = Image.open(f)
        if filter=='GreyScale':
            res=self.greyscale(img)
        elif filter=='Sepia':
            res=self.sepia(img)
        elif filter=='Invert':
            res=self.invert(img)
        res.save(filepath+'output.png')

    def greyscale(self, img):
        width, height = img.size
        new_img = img.copy()

        for x in range(width):
            for y in range(height):
                cur_pixel = img.getpixel((x, y))
                average = int(sum(cur_pixel) / 3)
                new_img.putpixel((x, y), (average,) * 3)

        return new_img

    # Convert to sepia tone
    def sepia(self, img):
        width, height = img.size
        new_img = img.copy()

        for x in range(width):
            for y in range(height):
                red, green, blue = img.getpixel((x, y))
                new_val = int(0.3 * red + 0.59 * green + 0.11 * blue)

                new_red = int(new_val * 2)
                if new_red > 255:
                    new_red = 255
                new_green = int(new_val * 1.5)
                if new_green > 255:
                    new_green = 255
                new_blue = int(new_val)
                if new_blue > 255:
                    new_blue = 255

                new_img.putpixel((x, y), (new_red, new_green, new_blue))

        return new_img

    def invert(self, img):
        width, height = img.size
        new_img = img.copy()

        for x in range(width):
            for y in range(height):
                red, green, blue = img.getpixel((x,y))
                new_red = 255 - red
                new_green = 255 - green
                new_blue = 255 - blue
                new_img.putpixel((x,y), (new_red, new_green, new_blue))

        return new_img

# The entry point for our application. This is where the computer will
# begin running our code.

# if __name__ == '__main__':
#     # Open the image file and read in its data so that we can access it
#     img = Image.open('main.jpg')

#     # Run the code for the filter. We should replace filter_name
#     # with the name of our filter.
#     new_img = greyscale(img)
#     new2_img = sepia(img)
#     new3_img = invert(img)

#     # Save the image file so that we can view it
#     new_img.save('color.jpg')
#     new2_img.save('sepia.jpg')
#     new3_img.save('invert.jpg')
