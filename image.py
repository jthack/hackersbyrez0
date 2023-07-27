import os
import imageio
from skimage.transform import resize

# The path to the image directory
image_dir = 'images'

# The path to the thumbnail directory
thumbnail_dir = 'images/thumbnails'

# Go through every file in the image directory
for filename in os.listdir(image_dir):
    # If the file is a .png
    if filename.endswith('.png'):
        try:
            # Read the image
            img = imageio.imread(os.path.join(image_dir, filename))
            
            # Calculate the aspect ratio
            aspect_ratio = img.shape[1] / img.shape[0]
            
            # Resize the image while keeping the aspect ratio, and ensuring the max dimension is 200
            if aspect_ratio > 1:
                img_resized = resize(img, (200, int(200*aspect_ratio)))
            else:
                img_resized = resize(img, (int(200/aspect_ratio), 200))
            
            # Convert the image data to 8 bit
            img_resized = (255 * img_resized).astype('uint8')
            
            # Write the image to the thumbnail directory
            imageio.imsave(os.path.join(thumbnail_dir, filename), img_resized)

        except Exception as e:
            print(f'Skipping file {filename} due to error: {e}')

print("All possible thumbnails are successfully created!")

