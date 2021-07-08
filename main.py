import time
import utils
import cv2
import openpose
import numpy as np


def main():

    cap = cv2.VideoCapture(0)
    vid_cap = cv2.VideoCapture(dance_path)

    count = 0
    score = 0
    start_time = time.time()
    end_time = start_time + dance_length

    while True and end_time - time.time() > 0:
        success, image = cap.read()

        vid_success, vid_image = vid_cap.read()

        values = openpose.predict_keypts(image)

        score += utils.check_frame(count, values, dance)

        cv2.putText(image, str(count), (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 2, cv2.LINE_AA)
        # cv2.imshow('WebCam', image)

        grey = cv2.cvtColor(vid_image, cv2.COLOR_BGR2GRAY)
        # Make the grey scale image have three channels
        grey_3_channel = cv2.cvtColor(grey, cv2.COLOR_GRAY2BGR)
        h = 0
        w = 0
        grey_3_channel = grey_3_channel[h/2: -h/2 + 1, w/2: -w/2 + 1]

        numpy_horizontal_concat = np.concatenate((image, grey_3_channel), axis=1)

        cv2.imshow('WebCam', numpy_horizontal_concat)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        count += 1

    cap.release()
    cv2.destroyAllWindows()

    return score / count


dance = 'thriller'
dance_length = 10
dance_path = ''
if __name__ == '__main__':

    main()

