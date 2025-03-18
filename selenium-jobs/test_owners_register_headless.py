from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
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
url = "http://"+APP_IP.strip()+":30001/"
print(url)
driver.get(url)

# "OWNERS" linkine tıkla
owners_link = driver.find_element("link text", "OWNERS")
owners_link.click()
sleep(2)

# "REGISTER" linkine tıkla
all_link = driver.find_element("link text", "REGISTER")
all_link.click()
sleep(2)

# Yeni bir sahibi Petclinic uygulamasına kaydet
fn_field = driver.find_element_by_name('firstName')
fn = 'Callahan' + str(random.randint(0, 100))
fn_field.send_keys(fn)
sleep(1)

fn_field = driver.find_element_by_name('lastName')
fn_field.send_keys('Clarusway')
sleep(1)

fn_field = driver.find_element_by_name('address')
fn_field.send_keys('Ridge Corp. Street')
sleep(1)

fn_field = driver.find_element_by_name('city')
fn_field.send_keys('McLean')
sleep(1)

fn_field = driver.find_element_by_name('telephone')
fn_field.send_keys('+1230576803')
sleep(1)

fn_field.send_keys(Keys.ENTER)

# Yeni eklenen sahip listesinin güncellenmesi için 10 saniye bekle
sleep(10)

# Yeni kullanıcının Sahipler Tablosunda olup olmadığını doğrula
if fn in driver.page_source:
    print(fn, 'is added and found in the Owners Table')
    print("Test Passed")
else:
    print(fn, 'is not found in the Owners Table')
    print("Test Failed")

# Tarayıcıyı kapat
driver.quit()