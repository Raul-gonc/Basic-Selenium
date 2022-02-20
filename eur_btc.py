from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://finance.yahoo.com/quote/BTC-EUR/history/')

f = open('eur_btc_rates.csv', 'a', newline="")
writer = csv.writer(f)
main = ('Date', 'BTC Closing Value')
writer.writerow(main)

count = 1
while count <= 10:
    date_path = f'//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[{count}]/td[1]'
    date = driver.find_element(By.XPATH, date_path)
    close_path = f'//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[{count}]/td[5]'
    close = driver.find_element(By.XPATH, close_path)
    content = (date.text, close.text)
    writer.writerow(content)
    count = count + 1

f.close()
