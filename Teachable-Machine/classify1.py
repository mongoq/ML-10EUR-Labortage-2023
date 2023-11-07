import tensorflow as tf
import numpy as np
import cv2

model = tf.keras.models.load_model('keras_model.h5')

with open('labels.txt', 'r') as file:
    labels = file.read().splitlines()

def classify_image(image):
    img = cv2.resize(image, (224, 224))
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = tf.expand_dims(img, axis=0)

    predictions = model.predict(img)
    predicted_class = np.argmax(predictions)
    confidence = predictions[0][predicted_class]

    return labels[predicted_class], confidence

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    class_name, confidence = classify_image(frame)
    cv2.putText(frame, f'Class: {class_name}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f'Confidence: {confidence * 100:.2f}%', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Webcam Classification', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
