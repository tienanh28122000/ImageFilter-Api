from image import Image
import numpy as np

class Transform:
    def __init__(self, f='', filter=''):
        global res
        img = Image(filename=f)
        if filter == 'HighContrast':
            res = self.adjust_contrast(img, 2, 0.5)
        elif filter == 'Electric':
            sobel_x = self.apply_kernel(img, np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]))
            sobel_y = self.apply_kernel(img, np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]]))
            res = self.combine_images(sobel_x, sobel_y)
        elif filter == 'Darkened':
            res = self.brighten(img, 0.3)
        elif filter == 'Censored':
            res = self.blur(img, 15)
        elif filter == 'Vintage':
            res = self.apply_kernel(img, np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]))
        res.write_image('output.png')

    def brighten(self, image, factor):
        # khi ta muon thay doi do tuong phan, ta chi can nhan moi gia tri diem anh voi mot gia tri khong doi 'factor'
        # factor la gia tri > 0, lua chon factor > 1 neu muon tang do tuong phan, factor < 1 neu muon giam do tuong phan
        x_pixels, y_pixels, num_channels = image.array.shape  # dai dien cho chieu rong, chieu cao va so chieu (R,G,B)
        new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  

        # # cach lam su dung vong lap
        # for x in range(x_pixels):
        #     for y in range(y_pixels):
        #         for c in range(num_channels):
        #             new_im.array[x, y, c] = image.array[x, y, c] * factor

        # tan dung ham cua thu vien numpy
        new_im.array = image.array * factor

        return new_im

    def adjust_contrast(self, image, factor, mid):
        # adjust the contrast by increasing the difference from the user-defined midpoint by factor amount
        # dieu chinh do tuong phan bang cach lam tang su khac biet tu diem giua do nguoi dung xac dinh boi gia tri factor
        x_pixels, y_pixels, num_channels = image.array.shape  # dai dien cho chieu rong, chieu cao va so chieu (R,G,B)
        new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  
        for x in range(x_pixels):
            for y in range(y_pixels):
                for c in range(num_channels):
                    new_im.array[x, y, c] = (image.array[x, y, c] - mid) * factor + mid

        return new_im

    def blur(self, image, kernel_size):
        # thay gia tri cua tung pixel boi mot ham cua diem anh va cac diem lan can cua no
        # kernel size is kich thuoc cua ma tran su dung de lam mo anh
        # (vd kernel_size = 3 tuong ung voi ma tran kich thuoc 3x3 voi pixel dang xet la tam) 
        # kernel size luon luon co gia tri le de ma tran co tam la pixel dang xet
        x_pixels, y_pixels, num_channels = image.array.shape  # dai dien cho chieu rong, chieu cao va so chieu (R,G,B)
        new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  
        neighbor_range = kernel_size // 2  # mien gia tri cua cac khoang doi voi diem anh dang xet
        for x in range(x_pixels):
            for y in range(y_pixels):
                for c in range(num_channels):
                    # gan gia tri cua diem anh dang xet voi gia tri trung binh cua ma tran diem anh 
                    total = 0
                    for x_i in range(max(0,x-neighbor_range), min(new_im.x_pixels-1, x+neighbor_range)+1):
                        for y_i in range(max(0,y-neighbor_range), min(new_im.y_pixels-1, y+neighbor_range)+1):
                            total += image.array[x_i, y_i, c]
                    new_im.array[x, y, c] = total / (kernel_size ** 2)
        return new_im

    def apply_kernel(self, image, kernel):
        # kernel la mot ma tran vuong
        # sobel x kernel (xac dinh canh theo chieu doc) co gia tri:
        # [1 0 -1]
        # [2 0 -2]
        # [1 0 -1]
        # sobel y kernel (xac dinh canh theo chieu ngang) co gia tri:
        # [1   2  1]
        # [0   0  0]
        # [-1 -2 -1]
        x_pixels, y_pixels, num_channels = image.array.shape  # dai dien cho chieu rong, chieu cao va so chieu (R,G,B)
        new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  
        neighbor_range = kernel.shape[0] // 2  # mien gia tri cua cac khoang doi voi diem anh dang xet
        for x in range(x_pixels):
            for y in range(y_pixels):
                for c in range(num_channels):
                    total = 0
                    for x_i in range(max(0,x-neighbor_range), min(new_im.x_pixels-1, x+neighbor_range)+1):
                        for y_i in range(max(0,y-neighbor_range), min(new_im.y_pixels-1, y+neighbor_range)+1):
                            x_k = x_i + neighbor_range - x
                            y_k = y_i + neighbor_range - y
                            kernel_val = kernel[x_k, y_k]
                            total += image.array[x_i, y_i, c] * kernel_val
                    new_im.array[x, y, c] = total
        return new_im

    def combine_images(self, image1, image2):
        # combine two images using the squared sum of squares: value = sqrt(value_1**2, value_2**2)
        # ket hop hai anh su dung can bac hai cua tong binh phuong
        x_pixels, y_pixels, num_channels = image1.array.shape  # dai dien cho chieu rong, chieu cao va so chieu (R,G,B)
        new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  
        for x in range(x_pixels):
            for y in range(y_pixels):
                for c in range(num_channels):
                    new_im.array[x, y, c] = (image1.array[x, y, c]**2 + image2.array[x, y, c]**2)**0.5
        return new_im
    
# if __name__ == '__main__':
    # lake = Image(filename='lake.png')
    # city = Image(filename='city.png')

    # # brightening
    # brightened_im = brighten(lake, 1.7)
    # brightened_im.write_image('brightened.png')

    # # darkening
    # darkened_im = brighten(lake, 0.3)
    # darkened_im.write_image('darkened.png')

    # # increase contrast
    # incr_contrast = adjust_contrast(lake, 2, 0.5)
    # incr_contrast.write_image('increased_contrast.png')

    # # decrease contrast
    # decr_contrast = adjust_contrast(lake, 0.5, 0.5)
    # decr_contrast.write_image('decreased_contrast.png')

    # # blur using kernel 3
    # blur_3 = blur(city, 3)
    # blur_3.write_image('blur_k3.png')

    # # blur using kernel size of 15
    # blur_15 = blur(city, 15)
    # blur_15.write_image('blur_k15.png')

    # # let's apply a sobel edge detection kernel on the x and y axis
    # sobel_x = apply_kernel(city, np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]))
    # sobel_x.write_image('edge_x.png')
    # sobel_y = apply_kernel(city, np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]]))
    # sobel_y.write_image('edge_y.png')

    # # let's combine these and make an edge detector!
    # sobel_xy = combine_images(sobel_x, sobel_y)
    # sobel_xy.write_image('edge_xy.png')

