import cv2
import time
from PIL import Image
from gui import GUI
from tkinter import messagebox

from task.compare_face.comparing_face import ComparingFace
from task.compare_background.matching_background import MatchingBackground
from task.check_spoof.face_anti_spoofing import FaceAntiSpoofing

THRESHOLD_FACE = 0.5
THRESHOLD_SPOOF = 0.5
THRESHOLD_BG = 15

CF = ComparingFace()
MB = MatchingBackground()
FAS = FaceAntiSpoofing()

def compare(path_img1, path_img2):
    result = ''
    compare_face_score = CF.compare_face(path_img1, path_img2)
    if compare_face_score > THRESHOLD_FACE:
        result = 'Không đúng người !!!'
        return result
    spoof_score = FAS.check_spoof(path_img2)
    if spoof_score < THRESHOLD_SPOOF:
        result = 'Đây là ảnh giả mạo !!!'
        return result
    compare_bg_score, matched_img = MB.compare_background(path_img1, path_img2)
    if compare_bg_score < THRESHOLD_BG:
        result = 'Ảnh chụp không đúng background !!!'
        return result
    
    result = 'Kết quả: Thành công !!! - Face: {}, Bg: {}, Spoof: {}'.format(compare_face_score, compare_bg_score, spoof_score)
    return result, matched_img

screen = GUI()
screen.show()
path_img1, path_img2 = screen.getFiles()
print(path_img1, path_img2)
start = time.time()
print('Running...')
result, img = compare(path_img1, path_img2)
runtime = 'Thời gian: {}s'.format(time.time() - start)
messagebox.showinfo('Done',result)

cv2.imwrite('./result/'+path_img1.split('/')[-1], img)
with open('./result/'+path_img1.split('/')[-1][0:len(path_img1.split('/')[-1]) - 4]+'.txt','w',encoding = 'utf-8') as file:
    file.write(result)
    file.write('\n')
    file.write(runtime)