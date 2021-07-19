import numpy as np
import cv2

from matplotlib import pyplot as plt


def detect_white_frame(image_path:str):
    top_side, bottom_side, left_size, right_size = 0, 0, 0, 0

    img = cv2.imread(image_path)
    height, width, channels = img.shape[:3]
    print("width: " + str(width))
    print("height: " + str(height))

    img_extracted = img[536:716, 1193:1373]

    cv2.imwrite('extracted.png', img_extracted)

    kernel_edit = np.ones((5,5),np.uint8)
    kernel_adjust = np.ones((7, 7),np.uint8)

    # img_dilation = cv2.dilate(img_extracted, kernel_edit, iterations=2)
    # img_erosion = cv2.erode(img_dilation, kernel_edit, iterations=2)
    # img_adjust = cv2.dilate(img_erosion, kernel_adjust, iterations=1)

    # gray = cv2.cvtColor(img_adjust, cv2.COLOR_BGR2GRAY)

    img_adjust = cv2.dilate(img_extracted, kernel_adjust, iterations=3)
    img_adjust = cv2.erode(img_adjust, kernel_adjust, iterations=3)

    gray = cv2.cvtColor(img_adjust, cv2.COLOR_BGR2GRAY)

    invgray = cv2.bitwise_not(gray)

    # replaced = np.where(gray < 100, 100, 0)

    # cv2.imwrite('erosion.png', gray)
    cv2.imwrite('invgray.png', invgray)

    # np.savetxt('test.csv', invgray, fmt='%d')

    test = np.where(invgray < 25, 255, 0)
    cv2.imwrite('test2.png', test)

    # test = np.where(invgray < 200, 0, invgray)

    # print('aaaa:', np.max(test))

    # plt.hist(invgray.ravel(),256,[0,256])
    # plt.show()

    # test = np.where((90 <= invgray) & (invgray <= 110), 255, 0)


    # cv2.imwrite('test.png', test)

    # kernel = np.ones((5,5),np.uint8)

    # cv2.imwrite('gray.jpg', gray)
    
    # closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    # cv2.imwrite('closing.jpg', closing)

    # gray2 = cv2.bitwise_not(gray)

    # edges = cv2.Canny(gray2, 150, 300, L2gradient=True)

    # exit()

    
    

    

    # # edges = cv2.Canny(gray, 50, 150, apertureSize = 3)
    # # edges = cv2.Canny(gray2, 50, 150, apertureSize=3)
    # # minLineLength = 100
    # min_line_length = 200
    # max_line_gap = 100

    # lines = cv2.HoughLinesP(gray2,1,np.pi/180,100,min_line_length,max_line_gap)
    # # lines = cv2.HoughLinesP(gray2, rho=1, theta=np.pi/360, threshold=100, minLineLength=100, maxLineGap=100)

    # print('lines: ', len(lines))
    # print('lines[0]:', lines[0])

    # # for x1, y1, x2, y2 in lines[0]:
    # #     cv2.line(img_extracted, (x1, y1), (x2, y2), (0, 255, 0), 2)
    # #     continue

    # for line in lines:
    #     x1, y1, x2, y2 = line[0]
    #     cv2.line(img_extracted, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # cv2.imwrite('houghlines5.jpg', img_extracted)
    # cv2.imwrite('test.jpg', gray2)

    return 0


def remove_white_frame():
    return 0


def adjust_image():
    return 0


def main():
    return 0


if __name__ == '__main__':
    input_image_path = '../../output/images/cs/000067200.png'
    detect_white_frame(input_image_path)
    print(0)
