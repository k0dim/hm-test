from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def check_for_email(my_email, my_password):
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(executable_path="/Users/dmitriykonnov/Downloads/chromedriver", chrome_options=chrome_options)
    driver.get("https://passport.yandex.ru/auth/")

    text_error = {
        "Логин": "",
        "Пароль": "",
    }

    # Логин
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "login"))).send_keys(my_email)
    driver.find_element(By.ID, "passp:sign-in").click()
    try:
        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "field:input-login:hint")))
        text_error['Логин'] = 'ОШИБКА ЕСТЬ'
        driver.close()
    except TimeoutException:
        text_error['Логин'] = 'ОШИБКИ НЕТ'

        # Пароль
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "passp-field-passwd"))).send_keys(my_password)
        driver.find_element(By.ID, "passp:sign-in").click()
        try:
            WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "field:input-passwd:hint")))
            text_error['Пароль'] = 'ОШИБКА ЕСТЬ'
            driver.close()
        except TimeoutException:
            text_error['Пароль'] = 'ОШИБКИ НЕТ'
            driver.close()
    return text_error

if __name__ == "__main__":
    my_email = "konnov-di2015@yandex.ru"
    my_password = "1"
    print(check_for_email(my_email, my_password))

