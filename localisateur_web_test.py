import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://nadsav.github.io/Localisateurs_Web/")
driver.maximize_window()
driver.find_element(By.NAME,'nomprenom').send_keys("Savasteeva Nadejda")
driver.find_element(By.NAME,'code perment').send_keys("admin2023")
driver.find_element(By.XPATH,'(//input[@value='f'])').click()
time.sleep(2)
driver.find_element(By.XPATH,'(//input[@value="IFT 1945"])').click()
driver.find_element(By.XPATH,'(//input[@value="IFT 2830"])').click()
time.sleep(2)
Jour_Sem=driver.find_element(By.NAME,'disponibilité')
Select(Jour_Sem).select_by_visible_text("Jeudi")
Credit_Card=driver.find_element(By.NAME,'carte credit')
Select(Credit_Card).select_by_visible_text("Master card")
time.sleep(2)
driver.find_element(By.NAME,'Commentaires').send_keys("Desolée pour le retard")
driver.find_element(By.NAME,'Courriel').send_keys("abc@gmail.com")
driver.find_element(By.NAME,'Phone').send_keys("5145612403")
time.sleep(3)
driver.find_element(By.XPATH,'//input[@value="Reinitialiser"]').click()