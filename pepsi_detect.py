import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#111
    # Define range of blue color for Pepsi can in HSV
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Create a blue HSV color boundary and threshold the HSV image
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize variables for the largest contour
    largest_contour = None
    max_area = 0

    for contour in contours:
        # Calculate the area of each contour
        area = cv2.contourArea(contour)

        # Update largest contour if the current area is larger
        if area > max_area:
            max_area = area
            largest_contour = contour

    if largest_contour is not None:
        # Calculate the bounding box for the largest contour
        x, y, w, h = cv2.boundingRect(largest_contour)

        # Draw the bounding box on the original frame
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Calculate the center point of the bounding box
        center_x = x + w // 2
        center_y = y + h // 2

        # Print the center point location
        print("Center Point Location: ({}, {})".format(center_x, center_y))

    # Display the original frame with bounding box
    cv2.imshow('Pepsi Can Detection', frame)

    # Wait for Esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()

