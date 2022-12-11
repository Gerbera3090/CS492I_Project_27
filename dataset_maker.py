import pickle
import pandas as pd

with open("review_data.pickle", 'rb') as f:
    reviews = pickle.load(f)
for i in range(len(reviews)):
    reviews[i][1] = int(reviews[i][1])
for review in reviews:
    print(review)
print(reviews)
print(len(reviews))
# with open("review_data.pickle", 'wb') as f:
#     pickle.dump(reviews,f)
exit(1)
df = pd.DataFrame(reviews, columns=['Review', 'Label'])
print(df)
df.to_csv('review_data.csv', sep=',', na_rep='NaN')
exit(1)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver_path = 'C:/Users/hw309/Downloads/chromedriver_win32/chromedriver.exe'

driver = webdriver.Chrome(driver_path)
url = 'https://www.yogiyo.co.kr/mobile/#/대전광역시/000000/'
driver.get(url)
time.sleep(3)
driver.find_element( By.CLASS_NAME ,"restaurants-info").click()
print(driver.current_url)
