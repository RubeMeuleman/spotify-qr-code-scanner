# All used imports -> look in README.md to import all libraries
import cv2
import webbrowser
from pyzbar.pyzbar import decode


# Function to detect QR code and perform a custom action
def detect_qr_code():
    # Open the camera
    cap = cv2.VideoCapture(0)
    qr_opened = False
    # Keep scanning until a QR code has been found
    while not qr_opened:
        # Reads frame from the camera
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to grayscale (QR code detection works better in grayscale)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect QR codes in the grayscale frame
        qr_codes = decode(gray)

        for qr in qr_codes:
            # Decode and extract data from the QR code
            qr_data = qr.data.decode('utf-8')

            # Open the qr code in a browser when it starts with http (link based)
            if qr_data.startswith('http'):
                webbrowser.open(qr_data)
                qr_opened = True

            # Print the QR code data result
            print(f"Detected QR code: {qr_data}")
            break

        # Open a window and display the camera (Optional -> Will also work without, but might be less clear where to hold the QR code)
        cv2.imshow('QR Code Detector', frame)

        # Wait for 'q' key to quit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera
    cap.release()
    # Close all OpenCV windows
    cv2.destroyAllWindows()


detect_qr_code()
