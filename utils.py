import cv2
import json


def learn_dance(video_path, json_path):
    with open(json_path) as file:

        cap = cv2.VideoCapture(video_path)

        success, image = cap.read()
        count = 0
        success = True
        while success:
            success, image = cap.read()
            # do something with frame here
            cv2.putText(image, str(count), (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.imshow(video_path, image)

            data = 123
            file.json.load({count: data})

            count += 1
        cap.release()
        cv2.destroyAllWindows()

#
# def webcam2frames():
#     cap = cv2.VideoCapture(0)
#     count = 0
#     while True:
#         success, image = cap.read()
#
#         cv2.putText(image, str(count), (10, 450), cv2.FONT_HERSHEY_SIMPLEX,  3, (0, 255, 0), 2, cv2.LINE_AA)
#         cv2.imshow('WebCam', image)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#         count += 1
#
#     cap.release()
#     cv2.destroyAllWindows()
#
#
# webcam2frames()


def check_frame(count, values, dance):

    return 1