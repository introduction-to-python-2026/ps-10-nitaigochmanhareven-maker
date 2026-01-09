import cv2
from image_utils import detect_edges

def main():
    # Load your original image
    path_to_image = 'your_image.jpg' # Replace with your file path
    original = cv2.imread(path_to_image)

    if original is None:
        print("Error: Could not load image.")
        return

    # Process the image using your utility function
    edge_result = detect_edges(original)

    # Save the output (often required for the assignment)
    cv2.imwrite('edge_detected_result.png', edge_result)

    # Display the results
    cv2.imshow('Original', original)
    cv2.imshow('Edges', edge_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
