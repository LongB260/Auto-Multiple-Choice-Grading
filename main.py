from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import cv2
import numpy as np
import os
import csv
import random

ANSWER_KEY = {
    0: 1,
    1: 2,
    2: 0,
    3: 4,
    4: 3,
}

folder_path = r'D:\Auto multiple-choice grading\images'
# Load list of images and perform edge detection
for filename in os.listdir(folder_path):
    image_path = os.path.join(folder_path, filename)
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 75, 200)

    # Find contours in edge-detected image
    cnts = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    docCnt = None

    # Finding the test contour
    if len(cnts) > 0:
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

        for c in cnts:
            peri = cv2.arcLength(c, closed=True)
            approx = cv2.approxPolyDP(c, epsilon=peri * 0.02, closed=True)

            if len(approx) == 4:
                docCnt = approx
                break

    # Getting the bird's eye view of the test
    paper = four_point_transform(image, docCnt.reshape(4, 2))
    warped = four_point_transform(gray, docCnt.reshape(4, 2))

    # Thresholding the test
    thresh = cv2.threshold(warped, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    # Finding contours in threshold image
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    questionCnts = []

    # Finding the question contours
    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        ar = w / float(h)

        if w >= 20 and h >= 20 and ar >= 0.9 and ar <= 1.1:
            questionCnts.append(c)

    # Sorting the contours according to the question
    questionCnts = contours.sort_contours(questionCnts, method="top-to-bottom")[0]
    correct = 0

    for (q, i) in enumerate(np.arange(0, len(questionCnts), 5)):
        cnts = contours.sort_contours(questionCnts[i:i + 5])[0]
        bubbled = None

        for (j, c) in enumerate(cnts):
            mask = np.zeros(thresh.shape, dtype="uint8")
            cv2.drawContours(mask, [c], -1, 255, -1)
            mask = cv2.bitwise_and(thresh, thresh, mask=mask)

            total = cv2.countNonZero(mask)

            if bubbled is None or total > bubbled[0]:
                bubbled = (total, j)

        color = (0, 0, 255)
        k = ANSWER_KEY[q]

        if k == bubbled[1]:
            color = (0, 255, 0)
            correct += 1

        cv2.drawContours(paper, [cnts[k]], -1, color, 3)

    # Print score and save it to CSV
    print("Score: {}/5".format(correct))
    data = [correct]
    with open('score.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

    # Save the graded image
    output_image_path = os.path.join(folder_path, f"graded_{filename}")
    cv2.putText(paper, "{}/5".format(correct), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
    cv2.imwrite(output_image_path, paper)  # Save the graded image

    def show_images(images, titles, kill_later=True):
        for index, image in enumerate(images):
            cv2.imshow(titles[index], image)
        cv2.waitKey(0)
        if kill_later:
            cv2.destroyAllWindows()

    show_images([image, paper], ["Test", "Result"])



