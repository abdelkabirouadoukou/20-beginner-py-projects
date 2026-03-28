import cv2, os

def detect_faces(image_path, output_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error loading {image_path}")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(20, 20)
    )

    print(f"{image_path} → {len(faces)} face(s) detected")

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    height, width = img.shape[:2]
    scale = min(900/width, 700/height, 1)
    img_resized = cv2.resize(img, (int(width*scale), int(height*scale)))

    cv2.imshow(image_path, img_resized)
    cv2.waitKey(0)

    cv2.imwrite(output_path, img)


images = [
    "16-python-face-detection/face1.jpg",
    "16-python-face-detection/face2.jpg",
    "16-python-face-detection/face3.jpg"
]

for img_path in images:
    output_name = "output_" + os.path.basename(img_path)
    detect_faces(img_path, output_name)

cv2.destroyAllWindows()