import face_recognition

class ComparingFace:
    def __init__(self) -> None:
        self.score = None

    def compare_face(self, path_img1:str, path_img2:str):
        img1 = face_recognition.load_image_file(path_img1)
        img2 = face_recognition.load_image_file(path_img2)

        img1_encodings = face_recognition.face_encodings(img1)
        img2_encodings = face_recognition.face_encodings(img2)

        face1 = img1_encodings[0]
        face2 = img2_encodings[0]
        face_distances = face_recognition.face_distance([face1], face2)
        self.score = round(face_distances[0], 4)
        return self.score