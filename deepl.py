#!/usr/bin/env python3
import argparse
import cv2
import numpy as np


class Argparser:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--image", type=str, help="which image file to use"
        )
        self.args = parser.parse_args()
        if self.args.image is None:
            raise Exception(
                "no image file provided. "
                "please specify an image with --image."
            )


def display(img: np.ndarray) -> None:
    cv2.imshow("asd", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def something(argparse: Argparser) -> None:
    img = cv2.imread(argparse.args.image, flags=cv2.IMREAD_COLOR)
    print(img.shape)
    img = img[:][:][:]
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            img[i][j][2] = 0
    display(img)


def main() -> None:
    argparse = Argparser()
    something(argparse)


if __name__ == "__main__":
    main()
