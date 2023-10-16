from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep



class Cookies:

    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.cookies_aft = []
        self.cookies_bef = []

# Access the url 

    def access_page(self):
        try:
            self.driver.get(self.url)
        except Exception as url_error:
            print("url_error:",url_error)

# Find the cookies are found before login 

    def cookie_bef_login(self):
        try:
            self.access_page()
            sleep(5)
            print("Cookies Before Login:")
            self.cookies_bef = self.driver.get_cookies()
            if self.cookies_bef:
                for cook in self.cookies_bef:
                    print(cook)
            else:
                print("No cookies Found")
        except Exception as Error_found:
            print("Error_found: ",Error_found)
    
# Login the webpage 

    def login_credential(self,username,password):
        try:
            self.driver.find_element(by=By.ID, value="user-name").send_keys(username)
            self.driver.find_element(by=By.ID, value="password").send_keys(password)
            sleep(5)
            self.driver.find_element(by=By.ID, value="login-button").click()
            sleep(5)
        except Exception as Error_found:
            print("Error_found:",Error_found)

# find the cookies found after the login process 

    def cookie_aft_login(self):
        try:
            self.cookies_aft =self.driver.get_cookies()
            print("Cookies After Login: ")
            if self.cookies_aft:
                for cook in self.cookies_aft:
                    print(cook)
            else:
                print("No cookies are found")
        except Exception as error:
            print("error: ",error)

# verify the cookies created & logout the webpage 

    def verify_logout(self,username,password):
        try:
            self.cookie_bef_login()
            self.login_credential(username,password)
            self.cookie_aft_login()
            if self.cookies_bef != self.cookies_aft:
                print("Verifed that Cookies are generated over Login process")
            else:
                print("No Cookies were generated over Login process")
        except Exception as error:
            print("error:",error)
        finally:
            self.driver.find_element(by=By.ID, value= 'react-burger-menu-btn').click()
            self.driver.find_element(by=By.ID, value= 'logout_sidebar_link').click()
            sleep(5)
            self.driver.quit()



url = "https://www.saucedemo.com/"
saucedemo_cookies = Cookies(url)
saucedemo_cookies.verify_logout("standard_user", "secret_sauce")