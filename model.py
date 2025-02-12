import cv2

# Load an image 
image = cv2.imread("Path to the image file")

# Define a function to handle mouse events for selecting the RoI
def select_roi(event, x, y, flags, param):
    global x_start, y_start, drawing, image_copy
    
    if event == cv2.EVENT_LBUTTONDOWN:  # Mouse button press
        drawing = True
        x_start, y_start = x, y
        
    elif event == cv2.EVENT_MOUSEMOVE:  # Mouse move event
        if drawing:
            image_copy = image.copy()  # Copy the original image
            cv2.rectangle(image_copy, (x_start, y_start), (x, y), (0, 255, 0), 2)  # Draw rectangle

    elif event == cv2.EVENT_LBUTTONUP:  # Mouse button release
        drawing = False
        cv2.rectangle(image_copy, (x_start, y_start), (x, y), (0, 255, 0), 2)  # Final rectangle
        # Show the final selection
        cv2.imshow("Image", image_copy)
        # Return the coordinates of the ROI 
        print("RoI Coordinates:", x_start, y_start, x, y)

# Initialize drawing flag and coordinates
drawing = False
x_start, y_start = -1, -1
image_copy = image.copy()

# Display the image and bind the mouse callback function
cv2.imshow("Image", image)
cv2.setMouseCallback("Image", select_roi)
 
# Wait for a key press to close the image window
cv2.waitKey(0)                 
cv2.destroyAllWindows()
