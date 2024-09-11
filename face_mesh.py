import cv2
import mediapipe as mp
import math


def is_smiling(landmarks, img_width, img_height, threshold=0.007):
    lip_right = landmarks[61]
    lip_left = landmarks[291]
    lip_top = landmarks[13]
    lip_bottom = landmarks[14]
    
    lip_right_diff = lip_right.y - ((lip_top.y + lip_bottom.y) / 2)
    lip_left_diff = lip_left.y - ((lip_top.y + lip_bottom.y) / 2)
    print(lip_left_diff)
    print(lip_right_diff)
    return lip_right_diff < -threshold and lip_left_diff < -threshold

mpFaceMesh = mp.solutions.face_mesh
FaceMesh = mpFaceMesh.FaceMesh(max_num_faces=1)
mpDraw = mp.solutions.drawing_utils
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)

# Video kaynağı
cap = cv2.VideoCapture(0)
smile_img = cv2.imread("datas/sabri_abi.jpg")
# Video oynatma döngüsü
while True:
    success, img = cap.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = FaceMesh.process(imgRGB)

    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_TESSELATION, drawSpec)
            # Eğlenmek için yorum satırındakileri aç
            if is_smiling(faceLms.landmark, img.shape[1], img.shape[0]):
                cv2.namedWindow("Smile Detected", cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("Smile Detected", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow("Smile Detected", smile_img)
   #            cv2.putText(img, "Smile Detected!", (10, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    # Görüntüyü göster
    cv2.imshow("img", img)

    # 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
