# Парсер сайта scopus

Программа парсит сайт scopus и выгружает информацию по авторам в .xlsx файл.
На вкачестве входных значений программа использует файл id.txt в котором предоставлены id
авторов.

## Установка и использование
Программа использует Selenium и в качестве браузера используется Chrome Вы должны установить webdirver для Chrome https://chromedriver.chromium.org/downloads

Для парсинга используется bs4, для выгрузки данных в таблицу pandas

    pip install selenium
    pip install pandas
    pip install bs4