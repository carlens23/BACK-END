from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.By import By
import time as t

driver = webdriver.Chrome()
driver.get("https://www.google.com.br/")

search_box = driver.find_element(By.XPATH, "//input[@class='gLFyf gsfi']")
search_box.send_keys('Jornada do artista' + Keys.ENTER)
t.sleep(2)

links = driver.find_elements(By.TAG_NAME, 'a').text
for link in links:
    print(link.get_attribute('href'))

t.sleep(2)
driver.quit()