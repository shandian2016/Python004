from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()

    browser.get('https://www.processon.com/login?f=index')
    time.sleep(1)

    browser.find_element_by_xpath('//*[@id="login_email"]').send_keys('')
    browser.find_element_by_xpath('//*[@id="login_password"]').send_keys('')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="signin_btn"]').click()

    # cookies = browser.get_cookies()  # 获取cookies
    # print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:
    browser.close()
