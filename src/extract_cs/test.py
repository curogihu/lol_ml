import cv2
import os
import numpy as np

from glob import glob
from tqdm import tqdm
from typing import List


def extract_images(
        video_path:str,
        output_directory_path: str,
        start_frame: int,
        end_frame:int,
        skip_frame:int=30) -> None:

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    # first hard coding and refactoring later
    os.makedirs(output_directory_path, exist_ok=True)
    
    current_frame_num = start_frame

    for current_frame in tqdm(range(start_frame, end_frame + 1, skip_frame)):
        cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame_num)
        ret, frame = cap.read()

        if ret:
            cv2.imwrite(f'{output_directory_path}/{current_frame_num:09d}.png', frame)
            current_frame_num += skip_frame

            # print(current_frame_num)

        else:
            return


# def recognize_cs_amount(image_path:str, template_image_path:str):
#     # img = cv2.imread(image_path)

#     img_gray = cv2.imread(image_path, 0)
#     # img_cs = img_gray[635:656, 578:591]
#     img_cs = img_gray[578:591, 635:656]

#     template_gray_img = cv2.imread(template_image_path, 0)

#     w, h = template_gray_img.shape[::-1]
#     print(w, h)

#     # res = cv2.matchTemplate(img_gray, template_gray_img, cv2.TM_CCOEFF_NORMED)
#     res = cv2.matchTemplate(img_cs, template_gray_img, cv2.TM_CCOEFF_NORMED)

#     # threshold = 0.77
#     threshold = 0.75

#     print(np.max(res))

#     loc = np.where(res >= threshold)

#     # exit()

#     print('loc: ', loc)
#     cv2.imwrite('base.png', img_cs)

#     for idx, pt in enumerate(zip(*loc[::-1])):
#         print(idx, pt)
#         cv2.rectangle(img_cs, pt, (pt[0] + w, pt[1] + h), (100, 255, 100), 2)

#     cv2.imwrite('res_2.png', img_cs)

def recognize_cs_amount_2(image_path:str, template_image_paths:List[str]):

    tmp = []

    for idx, template_image_path in enumerate(template_image_paths):
        coordinates = []

        img_gray = cv2.imread(image_path, 0)

        # 136
        # img_cs = img_gray[578:591, 635:656]

        img_cs = img_gray[652:680, 635:656]

        template_gray_img = cv2.imread(template_image_path, 0)

        w, h = template_gray_img.shape[::-1]
        # print(w, h)

        # res = cv2.matchTemplate(img_gray, template_gray_img, cv2.TM_CCOEFF_NORMED)
        res = cv2.matchTemplate(img_cs, template_gray_img, cv2.TM_CCOEFF_NORMED)

        # threshold = 0.77
        threshold = 0.80

        print(idx, np.max(res))

        loc = np.where(res >= threshold)

        # exit()

        # print('loc: ', loc)
        # cv2.imwrite('base.png', img_cs)

        for pt in zip(*loc[::-1]):
            # print(idx, pt)
            # cv2.rectangle(img_cs, pt, (pt[0] + w, pt[1] + h), (100, 255, 100), 2)
            coordinates.append(pt)

        # cv2.imwrite('res_2.png', img_cs)
        tmp.append({idx: coordinates})

    print(tmp)

    cv2.imwrite('test.png', img_cs)


def main():
    input_video_path = '../../input/movies/11-14_JP1-316783041_02.webm'
    output_directory_path = '../../output/images/cs'

    input_image_path = '../../output/images/cs/000067800.png'
    template_image_path = '../../input/images/digits/1.png'
    template_image_paths = sorted(glob('../../input/images/digits/*.png'))

    extract_images(input_video_path, output_directory_path, 600, 300000, 600)

    # recognize_cs_amount_2(input_image_path, template_image_paths)


if __name__ == '__main__':
    main()