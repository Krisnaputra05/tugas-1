import cv2
import numpy as np

# Load gambar yang dipilih
image_path = 'img/binary_image.png'
output_file_intensity = f'report/intens_biner.txt'  # simpan file intensitas

# Read the image using OpenCV
image = cv2.imread(image_path)

# Convert RBG image ke Grayscale
height = image.shape[0]
width = image.shape[1]
gray_image = np.zeros((height, width), dtype=np.uint8)

for y in range(height):
    for x in range(width):
        # Mengalikan intensitas grascale
        intensity = round((0.299 * image[y, x][2]) + (0.587 * image[y, x][1]) + (0.114 * image[y, x][0]))
        gray_image[y, x] = int(intensity)

# mengambil dimensi dari gambar grayscale
height, width = gray_image.shape

# masukan informasi intensitas kedalam file baru
with open(output_file_intensity, 'w') as file:
    # masukan kordinat dan juga nilai intensitas masing2 kordinat
    for y in range(height):
        for x in range(width):
            intensity = gray_image[y, x]
            file.write(f"({x},{y}) => Color Intensity: {intensity}\n")

# Display the grayscale image
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)  # Wait until a key is pressed
cv2.destroyAllWindows()

print(f"File yang disimpan : {output_file_intensity}")
