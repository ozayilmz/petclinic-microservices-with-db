from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

# Headless (ekransız) modda çalışmak için Chrome seçeneklerini ayarla
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("no-sandbox")
chrome_options.add_argument("disable-dev-shm-usage")

# Chrome webdriver örneğini başlat ve seçenekleri ekle
driver = webdriver.Chrome(options=chrome_options)

# Uygulamaya bağlan
APP_IP = os.environ['MASTER_PUBLIC_IP']
url = "http://" + APP_IP.strip() + ":8080/"
print(url)
driver.get(url)
sleep(3)

# "VETERINARIANS" linkine tıkla
vet_link = driver.find_element("link text", "VETERINARIANS")
vet_link.click()

# Tablo yüklendiğini doğrula
sleep(5)
verify_table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))

print("Table loaded")

# Tarayıcıyı kapat
driver.quit()