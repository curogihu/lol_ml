import cv2
import sys
from tqdm import tqdm

def main(movie_path: str):
    cap = cv2.VideoCapture(movie_path)
  
    if not cap.isOpened():
        sys.exit()

    movie_frame_num = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    for frame_per_num in tqdm(range(int(movie_frame_num // 100))):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_per_num * 100)
        ret, frame = cap.read()
        
        if ret:
            # cv2.imshow(window_name, frame)
            cv2.imwrite(f'../../output/images/{frame_per_num * 100:06d}.png', frame)

            # if cv2.waitKey(delay) & 0xFF == ord('q'):
            #     break
        else:
            break

        # frame_per_num = frame_per_num + 1
        # print(frame_per_num)

        # if i > 100:
        #     break

    # cv2.destroyWindow(window_name)



if __name__ == '__main__':
    movie_path = '../../input/movies/11-7_JP1-291722907_01.webm'
    main(movie_path)