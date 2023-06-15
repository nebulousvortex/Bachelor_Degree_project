from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions

# Устанавливаем путь к драйверу
driver_path = 'D:/YandexDriver/yandexdriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
options = ChromeOptions()
options.binary_location = 'C:/Users/Mega_/AppData/Local/Yandex/YandexBrowser/Application/browser.exe'
# открытие страницы в браузере
driver.get("http://localhost:8050")
element = driver.find_element(By.ID, "endTime")
element.click()
element.send_keys("02:00:00")
# проверка наличия элемента на странице
assert driver.find_element(By.ID, "endTime").is_displayed()