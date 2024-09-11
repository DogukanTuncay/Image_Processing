import cv2
from ultralytics import YOLO

# YOLOv8 modelini yükleyin
model = YOLO('yolov8n.pt')  # veya model yolunuza göre değiştirin

# Kamerayı aç
cap = cv2.VideoCapture(0)  # 0, genellikle varsayılan kamerayı belirtir

while True:
    # Kameradan bir kare oku
    ret, frame = cap.read()
    
    # Eğer kare başarıyla alındıysa
    if not ret:
        print("Kare alınamadı. Çıkılıyor...")
        break

    # Kareyi YOLOv8 ile işleyin
    results = model(frame)
    
    # YOLOv8'in sonuçlarını ekrana çizin
    annotated_frame = results[0].plot()  # Sonuçları çiz

    # Kareyi göster
    cv2.imshow('Kamera Akışı', annotated_frame)

    # 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
