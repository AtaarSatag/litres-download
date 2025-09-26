import os

from fpdf import FPDF

from config import BOOK_NAME, BOOK_ID

pdf = FPDF()
folder_path = f'books/{BOOK_NAME}_{BOOK_ID}'
folder = os.listdir(folder_path)
sorted_folder = sorted(folder, key=lambda x: int(os.path.splitext(x)[0]))
images = []

for file in sorted_folder:
    images.append(f'{folder_path}/{file}')

print(images)

for image in images:
    pdf.add_page()
    pdf.image(image, 0, 0, 210, 297)
    print(f'add page {image}')
print('create pdf...')
pdf.output(f'{folder_path}.pdf')

print('finish')
