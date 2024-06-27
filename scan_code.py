import cv2
import webbrowser
from pyzbar.pyzbar import decode  # Library for decoding QR codes


# Function to detect QR code and perform action
def detect_qr_code_and_action():
    cap = cv2.VideoCapture(0)  # Open the camera
    qr_opened = False

    while not qr_opened:
        ret, frame = cap.read()  # Read frame from the camera
        if not ret:
            break

        # Convert the frame to grayscale (QR code detection works better in grayscale)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect QR codes in the grayscale frame
        qr_codes = decode(gray)

        for qr in qr_codes:
            # Extract the QR code data
            qr_data = qr.data.decode('utf-8')

            # Example action based on QR code data (replace with your own action)
            if qr_data.startswith('http'):
                # If the QR code contains a URL, open it in a web browser
                webbrowser.open(qr_data)
                qr_opened = True

            # Print the QR code data to the console
            print(f"Detected QR code: {qr_data}")

            # You can add more conditions here based on the qr_data content

            # Exit the loop after processing one QR code
            break

        # Display the frame with QR code detected (optional)
        cv2.imshow('QR Code Detector', frame)

        # Wait for 'q' key to quit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()  # Release the camera
    cv2.destroyAllWindows()  # Close all OpenCV windows


# Run the function
detect_qr_code_and_action()