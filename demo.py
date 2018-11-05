from __future__ import print_function

import argparse
import itertools

import cv2 as cv
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class App:
    def __init__(self, video):
        self.cap = cv.VideoCapture(video)
        self.background = cv.imread('images/background.png')

        fourcc = cv.VideoWriter_fourcc(*'MPEG')
        self.out = cv.VideoWriter('video/output.avi', fourcc, 30.0, (544, 960))

    def process(self, frame, frame_idx):
        # bgr_ref = [134, 169, 55]
        lab_ref = [159, 88, 137]
        frame_lab = cv.cvtColor(frame, cv.COLOR_BGR2LAB)
        print(frame_idx)

        dist = np.linalg.norm(frame_lab[:, :, 1:] - lab_ref[1:], axis=2)
        alpha = sigmoid((dist - 30) / 3.)
        alpha = np.expand_dims(alpha, axis=-1)
        vis = alpha * frame + (1.0 - alpha) * self.background

        return vis.astype(np.uint8)

    def run(self):
        frame_idx = 0

        for _ in itertools.repeat(None, frame_idx):
            _, _ = self.cap.read()

        while self.cap.isOpened():
            success, frame = self.cap.read()
            if not success:
                break

            vis = self.process(frame, frame_idx)

            cv.imshow('frame', vis)
            self.out.write(vis)

            frame_idx = frame_idx + 1

            ch = cv.waitKey(1)
            if ch == 27:
                break

        print("Total frames: %d" % frame_idx)

        self.cap.release()
        self.out.release()
        cv.destroyAllWindows()


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", help="path to the video file", default='video/dabao.mp4')
    args = vars(ap.parse_args())

    video = args["video"]

    App(video).run()
