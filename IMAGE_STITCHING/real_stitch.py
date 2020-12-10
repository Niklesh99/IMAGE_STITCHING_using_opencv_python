from Stitcher import Stitcher
import imutils
import cv2

print("IMPORTING VIDEOS FROM DATASETS")

imageA = cv2.imread(r"C:\Users\Priya\Desktop\IMAGE_STITCHING\pano_left.jpg",1)
imageB = cv2.imread(r"C:\Users\Priya\Desktop\IMAGE_STITCHING\pano_right.jpg",1)
imageA = imutils.resize(imageA,width=400)
imageB = imutils.resize(imageB,width=400)


stitcher = Stitcher()
(result,vis) = stitcher.stitch([imageA,imageB],showMatches=True)

cv2.imshow("image A",imageA)
cv2.imshow("image B",imageB)
cv2.imshow("Keypoint Matches", vis)
cv2. imshow("Result", result)

cv2.waitKey(0)


