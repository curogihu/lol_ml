import cv2
import numpy as np
from matplotlib import pyplot as plt

from glob import glob

image_path = '../../output/images/049200.png'
skill_image_paths = sorted(glob('../../input/images/twisted_fate/*.png'))

tmp = cv2.imread(image_path)
print(tmp.shape)

cv2.imwrite('test1.png', tmp[615:637, 38:60, :])
cv2.imwrite('test2.png', tmp[615:637, 63:85, :])
cv2.imwrite('test3.png', tmp[615:637, 88:110, :])
cv2.imwrite('test4.png', tmp[615:637, 113:135, :])

tmp_1 = cv2.imread('test1.png')

tmp_2 = cv2.resize(tmp_1, (64, 64))
cv2.imwrite('test1_1.png', tmp_2)

# main_img = cv2.imread(image_path)
# img2 = main_img.copy()

# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#             'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

# for method_idx, meth in enumerate(methods):
#     for skill_idx, skill_image_path in enumerate(skill_image_paths):
#         img = img2.copy()
#         method = eval(meth)

#         template = cv2.imread(skill_image_path)
#         # print(template.shape[::-1])
#         # exit()
#         _, w, h = template.shape[::-1]

#         # Apply template Matching
#         res = cv2.matchTemplate(img,template,method)
#         min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

#         # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
#         if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#             top_left = min_loc
#         else:
#             top_left = max_loc
#         bottom_right = (top_left[0] + w, top_left[1] + h)

#         cv2.rectangle(img,top_left, bottom_right, 255, 2)

#         plt.subplot(121),plt.imshow(res,cmap = 'gray')
#         plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
#         plt.subplot(122),plt.imshow(img,cmap = 'gray')
#         plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
#         plt.suptitle(meth)

#         # plt.show()
#         plt.savefig(f'{method_idx}_{skill_idx}.png')

