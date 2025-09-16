import cv2
from PIL import Image

# Get the file name from user input

# Load an image (replace 'pics/gambar_rotasi_180.png' with the actual image path)
image_path = 'report/mirror_image.png'
output_file = f'report/intens_RGB_mirror.txt'  # Specify the output file name

# Read the image using OpenCV
image = cv2.imread(image_path)

# Get the dimensions of the image
height = image.shape[0]
width = image.shape[1]

# Open the output file for writing
with open(output_file, 'w') as file:
    # Output the RGB intensity and coordinates of each pixel
    for y in range(height):
        for x in range(width):
            # Get the RGB values of the pixel
            r = image[y, x][2]
            g = image[y, x][1]
            b = image[y, x][0]

            # Calculate the intensity
            intensity = round((0.299 * r) + (0.587 * g) + (0.114 * b))

            # Output the intensity and coordinates
            file.write(f"({x},{y}) => R: {r}, G: {g}, B: {b}, Intensity: {intensity}\n")

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)  # Wait until a key is pressed
cv2.destroyAllWindows()

