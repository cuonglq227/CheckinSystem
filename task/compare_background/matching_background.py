import cv2
import numpy as np
import face_recognition

class MatchingBackground:
    def __init__(self) -> None:
        self.matches = None
        self.image = None

    def get_frame_remove(self, path_img:str):
        img = face_recognition.load_image_file(path_img)
        face = face_recognition.face_locations(img)
        top, right, bottom, left = face[0][0], face[0][1], face[0][2], face[0][3]
        top = int(round(top - 0.4*(bottom-top)))
        if top <= 0 : top=0
        bottom = img.shape[0]
        return top, bottom, left, right

    def get_points(self, path_img:str):
        top, bottom, left, right = self.get_frame_remove(path_img)
        img = cv2.imread(path_img, cv2.COLOR_GRAY2BGR)
        sift = cv2.SIFT_create()
        kp1, des1 = sift.detectAndCompute(img,None)
        kp11 = []
        des11 = []
        for j in range(len(kp1)):
            if kp1[j].pt[0] >= left and kp1[j].pt[0] <= right and kp1[j].pt[1] >= top and kp1[j].pt[1] <= bottom :
                continue
            else:
                kp11.append(kp1[j])
                des11.append(des1[j])
        kp11 = tuple(kp11)
        des11 = np.array(des11)
        # img = cv2.drawKeypoints(img, kp11, 0, (0,255,0), flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img, kp11, des11

    def compare_background(self, path_img1:str, path_img2:str):
        img1, kp1, des1 = self.get_points(path_img1)
        img2, kp2, des2 = self.get_points(path_img2)
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1,des2,k=2)
        good = []
        for m,n in matches:
            if m.distance < 0.5*n.distance:
                good.append([m])
        self.matches = len(good)
        img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        self.image = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
        return self.matches, self.image