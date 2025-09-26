import os

from PIL import Image

from config import BOOK_NAME, BOOK_ID

book_format = input('Choose a file format to save of AVIF, BMP, GIF, PDF, TIFF, JPEG, PNG (more: https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html): ')

folder_path = f'books/{BOOK_NAME}_{BOOK_ID}'
folder = os.listdir(folder_path)
sorted_folder = sorted(folder, key=lambda x: int(os.path.splitext(x)[0]))
images = []

for file in sorted_folder:
    images.append(f'{folder_path}/{file}')

print(images)

images = [
    Image.open(img)
    for img in images
]

file_path = f'{folder_path}.{book_format}'

images[0].save(
    file_path, book_format , resolution=100.0, save_all=True, append_images=images[1:]
)
print('Done.')
