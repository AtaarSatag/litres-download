import os
import sys
import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config import (URL_BOOKS, URL_LOGIN, BOOK_ID,
                    BOOK_NAME, PAGES, LOGIN, PASSWORD)

def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_service = Service(
            executable_path='/usr/bin/chromedriver-linux64/chromedriver')
    driver = webdriver.Chrome(service=chrome_service,
                              options=chrome_options)
    return driver

def login_litres(driver):
    driver.get(URL_LOGIN)
    username_in = driver.find_element(by=By.NAME, value='email')
    username_in.click()
    username_in.send_keys(LOGIN)
    username_in.send_keys(Keys.RETURN)
    time.sleep(2)
    password_in = driver.find_element(by=By.NAME, value='pwd')
    password_in.send_keys(PASSWORD)
    time.sleep(1)
    password_in.send_keys(Keys.RETURN)
    time.sleep(2)

def scroll_down(driver):
    count = 0
    while True:
        page = driver.find_element(by=By.TAG_NAME, value="html")
        page.send_keys(Keys.END)
        driver.implicitly_wait(1)
        page.send_keys(Keys.END)
        driver.implicitly_wait(1)
        page.send_keys(Keys.END)
        count += 1
        print(f'scroll down {count}')
        driver.implicitly_wait(1)
        footer = driver.find_element(by=By.CLASS_NAME, value='footer-wrap')
        if footer and footer.is_displayed():
            loader_button = driver.find_element(by=By.ID,
                                                value='arts_loader_button')
            if loader_button and not loader_button.is_displayed():
                break
    print(f'scroll down exit after {count} scrolls')

def load_books(driver: WebDriver):
    print(f"create dir {BOOK_NAME}_{BOOK_ID}")
    if not os.path.exists("books"):
        os.mkdir("books")
        if not os.path.exists(f"books/{BOOK_NAME}_{BOOK_ID}"):
            os.makedirs(f"books/{BOOK_NAME}_{BOOK_ID}")
    type_file = "jpg"
    driver.get(URL_BOOKS.format(0, type_file, BOOK_ID))
    time.sleep(2)
    session = requests.session()
    for cookie in driver.get_cookies():
        session.cookies.set(
            domain=cookie['domain'],
            name=cookie['name'],
            value=cookie['value'],
            path=cookie['path'],
            secure=cookie['secure'],
        )

    for i in range(PAGES):
        percent = ((i+1)/PAGES) * 100
        src = URL_BOOKS.format(i, type_file, BOOK_ID)
        resp = session.get(src)
        if (resp.status_code == requests.codes.not_found
           and type_file == 'jpg'):
            type_file = 'gif'
            resp = session.get(URL_BOOKS.format(i, type_file, BOOK_ID))
        elif (resp.status_code == requests.codes.not_found
              and type_file == 'gif'):
            type_file = 'jpg'
            resp = session.get(URL_BOOKS.format(i, type_file, BOOK_ID))
        elif resp.status_code == requests.codes.ok:
            time.sleep(2)
            resp = session.get(URL_BOOKS.format(i, type_file, BOOK_ID))
        else:
            raise Exception(f"""There an error. The script tried to get
                            the resource and got an answer:
                            STATUS CODE: {resp.status_code}""")
        with open(f"books/{BOOK_NAME}_{BOOK_ID}/{i}.{type_file}", "wb") as f:
            f.write(resp.content)

        match sys.platform:
            case 'linux' | 'darwin':
                os.system('clear')
            case 'win32':
                os.system('cls')
        print(f"Downloaded {i} pages of {PAGES}")

        if i == PAGES:
            driver.quit()

def litres_loads():
    driver = create_driver()
    driver.maximize_window()
    login_litres(driver)
    load_books(driver)
    time.sleep(1)
    print('DONE')

def main():
    litres_loads()

if __name__ == '__main__':
    main()
