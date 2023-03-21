from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chromedriver = 'C:\\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
browser.get("https://www.deviantart.com")

login_button = browser.find_element(By.XPATH, '//*[@id="root"]/header/div[3]/a[2]/span')
login_button.click()
username_box = browser.find_element(By.XPATH, '//*[@id="username"]')
password_box = browser.find_element(By.XPATH, '//*[@id="password"]')
username_box.send_keys("brandongeorge87")
password_box.send_keys("SoftwareQA12Engineer")
second_login = browser.find_element(By.XPATH, '//*[@id="loginbutton"]')
second_login.click()
search_box = browser.find_element(By.XPATH, '//*[@id="search-input"]')
search_box.send_keys("shellyeah")
search_box.send_keys(Keys.ENTER)
user = browser.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div/div/div[3]/div/div/div[3]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/a[2]')
user.click()
gallery = browser.find_element(By.XPATH, '//*[@id="content-container"]/div[2]/div[2]/div/div/nav/div[2]/a[2]')
gallery.click()
#first_featured = browser.find_element(By.XPATH, '//*[@id="sub-folder-gallery"]/div/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div')
#first_featured.click()
#comment = browser.find_element(By.XPATH, '//*[@id="root"]/main/div/div[1]/section/div/div[3]/div[1]/span[2]/div/div/button/span[2]')
#comment.click()
#comment_box = browser.find_element(By.XPATH, '//*[@id="commentpanel-777245185"]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[2]/div/div/div/div')
#comment_box.send_keys("This is a test comment sent by automation")
#browser.find_element(By.XPATH, '//*[@id="commentpanel-777245185"]/div/div/div[2]/div/footer/div[2]/button[2]').click()
#comment = browser.find_element(By.XPATH, '//*[@id="comment-4-942465-top"]/div/div/div[2]/div/button').click()
#comment = WebDriverWait(browser, 2)
#comment_box = browser.find_element(By.XPATH, '//*[@id="comment-4-942465-top"]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[2]/div/div/div/div')
#comment_box.send_keys("This is a test comment sent by automation.")
#comment_box = WebDriverWait(browser,2)
#browser.find_element(By.XPATH, '//*[@id="comment-4-942465-top"]/div/div/div[2]/div/footer/div[2]/button[2]').click()
