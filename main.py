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

        webcam_dim = (image.shape[1], image.shape[0])
        ratio = webcam_dim[1] / webcam_dim[0]

        if not vid_image.shape[0] / vid_image.shape[1] == ratio:
            crop_val = abs(int(vid_image.shape[1] * (1 - ratio) / 2))
            vid_image = vid_image[:, crop_val: -crop_val, :]

        xxx = vid_image.shape
        yyy = image.shape
        vid_image = cv2.resize(vid_image, webcam_dim, interpolation=cv2.INTER_AREA)

        numpy_horizontal_concat = np.concatenate((image, vid_image), axis=1)

        cv2.imshow('WebCam', numpy_horizontal_concat)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        count += 1

    cap.release()
    cv2.destroyAllWindows()

    return score / count


dance = 'thriller'
dance_length = 10
dance_path = '/home/nadav/Downloads/video.mp4'
if __name__ == '__main__':

    main()

