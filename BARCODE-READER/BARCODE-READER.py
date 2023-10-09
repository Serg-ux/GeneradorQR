import cv2

# Encargado de detectar el código de barras
bd = cv2.BarcodeDetector_create()
cap = cv2.VideoCapture(0)

# Diccionario de detecciones para los falsos positivos
detecciones = {}

while True:
    # Verifica si hay algún código de barras
    ret, frame = cap.read()
    if ret:
        ret_bc, decode, puntos, _ = bd.detectAndDecodeMulti(frame)
        # Generar un rectángulo alrededor de ese código de barras
        if ret_bc:
            for i in range(len(decode)):
                points = puntos[i].astype(int)
                frame = cv2.polylines(frame, [points], isClosed=True, color=(0, 255, 0), thickness=2)
                codigo = decode[i]
                # Verificar si el código se encuentra en nuestro diccionario
                if codigo in detecciones:
                    detecciones[codigo] += 1
                    if detecciones[codigo] >= 30:
                        print("Detección exitosa:", codigo)
                        cv2.waitKey(250)
                        detecciones.clear()
                else:
                    detecciones[codigo] = 1
                punto = (points[0], points[1] - 10)
                frame = cv2.putText(frame, codigo, punto, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow('Escaner de barras', frame)
    # Salir de la aplicación cuando el usuario presione 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
