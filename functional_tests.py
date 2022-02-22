from selenium import webdriver

browser = webdriver.Chrome(executable_path=r'/home/tarena/桌面/web/chromedriver')
browser.get('http://localhost:8000')
assert 'Django' in browser.title
