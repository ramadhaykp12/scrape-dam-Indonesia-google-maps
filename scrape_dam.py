from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

driver = webdriver.Chrome()  
driver.get("https://www.google.com/maps")

# Data untuk referensi nama daerah
data = pd.read_csv('daftar bendungan.csv')  

addresses = []
latitudes = []
longitudes = []

for index, row in data.iterrows():
    search_box = driver.find_element(By.ID,"searchboxinput")
    search_box.clear()
    search_box.send_keys(row['Koordinat'])
    search_box.send_keys(Keys.RETURN)
    time.sleep(10)  # Tunggu beberapa detik untuk memuat hasil pencarian
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@data-tooltip='Salin alamat']")))
    #menu_div = driver.find_element(By.XPATH, "//div[@class='bJzME tTVLSc']")
    #outer_div = menu_div.find_element(By.XPATH,"//div[@data-tooltip='Salin alamat']")
    #inner_div = menu_div.find_element(By.XPATH,"//div[@class='LCF4w ']")
    #inner_span = inner_div.find_element(By.XPATH, "//div[@class='JpCtJf']")

    url = driver.current_url
    if '@' in url:
        coordinates = url.split('@')[1].split(',')[0:2]
        latitudes.append(coordinates[0])
        longitudes.append(coordinates[1])
    else:
        latitudes.append(None)
        longitudes.append(None)

    print(row['Koordinat'])
    print(addresses)
    print(latitudes,longitudes)
    address_element =driver.find_element(By.CLASS_NAME, "DkEaL")
    address = address_element.text if address_element else None
    addresses.append(address)
    df = pd.DataFrame({'Address': addresses,
                       'Latitude':latitudes,
                       'Longitudes':longitudes})
    df.to_csv('bendungan_trial.csv', index=False)

# Menambahkan data latitude dan longitude ke data referensi


# Export data menjadi file csv