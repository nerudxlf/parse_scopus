import time

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


def get_author_h_index(soup) -> str:
    """
    get h index from html
    :param soup:
    :return string:
    """
    try:
        h_index = soup.find_all('h3', {'class': '_1kYdpHTL20fs5Qk9XhXPVJ'})[2].text
    except IndexError:
        h_index = "Error"
    return h_index


def get_author_name(soup) -> str:
    """
    get name from html
    :param soup:
    :return string:
    """
    try:
        section = soup.find("section", {"id": "author-general-details"})
        name = section.find("h2").text
    except AttributeError:
        name = "Not found"
    return name


def get_arr_html(arr, browser) -> list:
    """
    get all html code for parse
    :param arr:
    :param browser:
    :return list with html:
    """
    return_arr_html_text = []
    for i in arr:
        browser.get("https://www.scopus.com/authid/detail.uri?authorId=" + i)
        time.sleep(2)
        return_arr_html_text.append(browser.page_source)
    return return_arr_html_text


def read_txt(path, mode) -> list:
    """
    read text from txt file
    :param path:
    :param mode:
    :return:
    """
    arr_result = []
    with open(path, mode) as f:
        data = f.readlines()
        for i in data:
            if i[-1] == "\n":
                arr_result.append(i[:-1])
            else:
                arr_result.append(i)
    arr = set(arr_result)
    arr_result = list(arr)
    return arr_result


def chrome(path):
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(executable_path=path, chrome_options=options)
    return browser


def main():
    arr_h_index = []
    arr_author_name = []
    chromedriver_path = 'C:/programs/chrome/chromedriver'

    arr_link = read_txt("id.txt", "r")  # read id
    browser = chrome(chromedriver_path)  # get browser
    arr_html_text = get_arr_html(arr_link, browser)  # get all html
    for i in arr_html_text:
        soup = BeautifulSoup(i, 'html5lib')
        arr_h_index.append(get_author_h_index(soup))
        arr_author_name.append(get_author_name(soup))
    df = pd.DataFrame(
        {
            "id": arr_link,
            "author name": arr_author_name,
            "h index": arr_h_index
        }
    )
    df.to_excel("Out.xlsx", index=False)

