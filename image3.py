import os
import sys
import imageio
import zipfile
from skimage.transform import resize


def find_subfolder(directory):
    for foldername in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, foldername)):
            return os.path.join(directory, foldername)
    return directory


def create_thumbnails(img, filename):
    aspect_ratio = img.shape[1] / img.shape[0]
    if aspect_ratio > 1:
        img_resized = resize(img, (200, int(200*aspect_ratio)))
    else:
        img_resized = resize(img, (int(200/aspect_ratio), 200))

    img_resized = (255 * img_resized).astype('uint8')
    imageio.imsave(os.path.join(thumbnail_dir, filename), img_resized)

def move_and_rename_images(folder_path):
    files = os.listdir(folder_path)
    existing_images = [f for f in files if f.endswith('.png')]

    if existing_images:
        existing_images.sort(key = lambda x: int(x.split('image')[-1].split('.png')[0]))
        next_num = int(existing_images[-1].split('image')[-1].split('.png')[0]) + 1
    else:
        next_num = 1

    for filename in os.listdir(folder_path):
        if filename.endswith('.png'):
            new_filename = f'image{next_num}.png'
            print(new_filename)
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

            img = imageio.imread(os.path.join(folder_path, new_filename))
            create_thumbnails(img, new_filename)
            next_num += 1


def unzip_folder(folder_to_unzip):
    with zipfile.ZipFile(folder_to_unzip, 'r') as zip_ref:
        zip_ref.extractall(unzipped_folder)


if __name__ == '__main__':
    image_dir = 'images'
    thumbnail_dir = 'images/thumbnails'
    unzipped_folder = 'unzipped_images'

    os.makedirs(image_dir, exist_ok=True)
    os.makedirs(thumbnail_dir, exist_ok=True)
    os.makedirs(unzipped_folder, exist_ok=True)

    if len(sys.argv) != 2:
        raise Exception('Invalid arguments. Pass the zip file as an argument to the script.')

    folder = sys.argv[1]

    if not os.path.isfile(folder):
        raise Exception('The provided argument is not a valid file.')

    unzip_folder(folder)
    unzipped_folder_path = find_subfolder(unzipped_folder)
    move_and_rename_images(unzipped_folder_path)

    print("All possible thumbnails are successfully created!")

