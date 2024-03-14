from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Kullanıcıdan anahtar kelimeyi ve tıklanılacak siteyi alın
search_term = input("Lütfen aramak istediğiniz anahtar kelimeyi girin: ")
site_url = input("Lütfen tıklanılacak siteyi URL'sini girin: ")

# Web sürücüsünü başlat
driver = webdriver.Chrome()  # Chrome kullanıyorsanız, kendi sürücünüzü yükleyin

while True:
    # Google'a gidin
    driver.get("https://www.google.com")

    # Arama kutusunu bulun ve anahtar kelimeyi girin
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.clear()
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)

    # İlgili siteye tıklayın
    try:
        first_result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//a[contains(@href, '{site_url}')]"))
        )
        first_result.click()
        print(f"{site_url} başarıyla tıklandı.")
    except:
        print("İlgili site bulunamadı veya tıklanamadı.")

# Tarayıcıyı kapat
driver.quit()
