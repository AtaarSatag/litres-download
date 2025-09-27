# LitRes book downloader

## Workflow

Do you want to download a book from `litres.com/ru`, but it doesn't have such an feature? There is a solution to. This repo has two kinds of scripts: the first downloads raw book material - pages as images, the second is dedicated to convert the raw material to one of formats: PDF, TIFF - for a single file, and other formats.

Script [`get_images.py`](https://github.com/AtaarSatag/litres-book-downloader/blob/master/get_images.py) is of the first kind, it downloads the raw material with [Selenium](https://selenium.dev/) and it can raise error (see [ChromeDriver issue](#ChromeDriver-issue)). Scripts of the second kind are two there:

- [`create_pdf_by_fpdf2.py`](https://github.com/AtaarSatag/litres-book-downloader/blob/master/create_pdf_by_fpdf2.py) (alive successor of fpdf, learn more: [https://py-pdf.github.io/fpdf2/History.html](https://py-pdf.github.io/fpdf2/History.html))
- [`create_pdf_by_pillow.py`](https://github.com/AtaarSatag/litres-book-downloader/blob/master/create_pdf_by_pillow.py) ([fork](https://github.com/python-pillow/Pillow) of PIL)
The first one only converts the book to PDF, the second can convert to PDF, and image formats: AVIF, BMP, GIF, PDF, TIFF, JPEG, PNG, and more (see [https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html))

The repo has also [`config.py`](https://github.com/AtaarSatag/litres-book-downloader/blob/master/config.py). You need to set up it, namely:

- fill up your `LOGIN` and `PASSWORD` of your LitRes account
- put your `BOOK_ID` (to know, go to the book webpage, open the LitRes reader, its page will have an URL like `https://litres.com/static/or3/view/or.html?art_type=4&file=00000000`, you need a value of the `file` parameter, it's the book ID)
- put the book `PAGES` (to know, open the book with the LitRes reader, run *DevTools* (**Ctrl+Shift+I**, usually), pick the last page by the element selector/picker (**Ctrl+Shift+C**), in the Elements tab, you will find an `img` element which has the parent `div`, it has an `id` attribute like `id="p_X"`, a number X + 1 is `PAGES`)

After that:

- run [`get_images.py`](https://github.com/AtaarSatag/litres-book-downloader/blob/master/get_images.py) to download the raw material
- run `create_pdf_by_X.py` (fpdf2 or pillow) to get a PDF or another format of the book

That's done!

## ChromeDriver issue

(The following solution is for GNU/Linux)

If you get an error like `selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 114 Current browser version is...` when [`get_images.py`](https://github.com/AtaarSatag/litres-book-downloader/blob/master/get_images.py) is running, try:

1. Check your Chrome/Chromium version
2. Go to [https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/) or to [https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json](https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json)
3. Download a necessary version of **ChromeDriver** (not Chrome)
4. Unzip the archive
5. Find your ChromeDriver executable folder (something like `/usr/bin/chromedriver-linux64`)
6. Move/copy the downloaded ChromeDriver to that folder, i.e. replace the existing one
7. Try to run [`get_images.py`](https://github.com/AtaarSatag/litres-book-downloader/blob/master/get_images.py) again 
