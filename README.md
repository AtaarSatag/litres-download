# LitRes book downloader

## Русский

Скрипты для скачивания книг с litres.ru, для которых нет опции скачать.

### Описание

- Заполнить свои данные в [config.py](config.py)
  - Логин
  - Пароль
  - ID книги
  - Количество страниц книги
- Запустить [get_images.py](get_images.py)
  - Ожидать пока он сохранит все страницы
- Запустить [create_pdf.py](create_pdf.py)
  - Ожидать пока он создаст PDF из изображений

В целях удобства скрипты разнесены на 3 отдельных, поскольку каждая процедура занимает около 20-30 минут. Один скачивает исходный материал - книгу в виде картинок, два оставшихся конвертируют исходники в PDF или другой формат, если вы используете `create_pdf_by_pillow.py`.

### ID книги
- Для получения ID книги открыть *Инструменты разработчика* **(Ctrl+Shift+I)** при онлайн просмотре
- Найти ссылку на изображение вида `https://www.litres.ru/pages/get_pdf_page/?file=ХХХХХХХХ`
- `XXXXXXXX` это и есть ID книги

### Проблема с ChromeDriver

(Решение для GNU/Linux)

Если вы сталкиваетесь с проблемой `selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 114 Current browser version is...`, когда запускаете скрипт `get_images.py`, то попробуйте следующии шаги:

1. Обновите ваш Chrome/Chromium до последней версии
2. Перейдите в [https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/)
3. Скачайте stable версию **ChromeDrive** (не Chrome)
4. Разархивируйте архив
5. Найдите папку с бинарником уже установленного ChromeDriver (обычно, `/usr/bin/chromedriver-linux64`)
6. Замените скачанным ChromeDriver'ом уже установленный (в его папке)
7. Попробуйте запустить `get_images.py` снова

## English

There are scripts to download books if they aren't downloadable from litres.ru.

### Description

- Put your data into [config.py](config.py)
  - Login
  - Password
  - Book ID
  - Book page number
- Run [get_images.py](get_images.py)
  - Wait while the files are downloading.
- Run [create_pdf.py](create_pdf.py)
  - Wait while the files are converting into PDF.

For convenience, there are 3 scripts due to time costs which are about 20-30 minutes. One script downloads raw material - book as images, the remaining two convert the material into PDF or another format if you use `create_pdf_by_pillow.py`.

### Book ID
- To get a book ID go to *Developer tools* **(Ctrl+Shift+I)** when the book is opened in the native reader
- Search for a pattern like `litres.ru/pages/get_pdf_page/?file=ХХХХХХХХ`
- `XXXXXXXX` is the book ID

### ChromeDriver issue

(The following solution is for GNU/Linux)

If you get an error like `selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 114 Current browser version is...` when `get_images.py` is running, try:
1. Update your Chrome/Chromium browser to the latest version
2. Go to [https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/)
3. Download a stable version of **ChromeDriver** (not Chrome)
4. Unzip the archive
5. Find your ChromeDriver executable folder (something like `/usr/bin/chromedriver-linux64`)
6. Move/copy downloaded ChromeDriver to that folder, i.e. replace the existing one
7. Try to run `get_images.py` one more time
