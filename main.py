import username
from selenium import webdriver
class Instagram():
    def __init__(self):
        self.username = username.username
        self.password = username.password
        self.browser = webdriver.Firefox()
        self.browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        

instagram = Instagram()