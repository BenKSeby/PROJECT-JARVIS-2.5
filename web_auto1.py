from selenium import webdriver
import time

class Movie():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\selenium browser driver\chromedriver.exe')

    def movie_review(self, name):
        self.driver.get(url="https://www.google.com")
        search1 = self.driver.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        search1.click()
        search1.send_keys(name + " movie reviews")
        #submit1 = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/ul[1]/div/ul/li[1]/div/div[2]')
        submit1 = self.driver.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')
        submit1.click()
        time.sleep(60)
        
        from repeat import first1
        return first1()

#bot = Movie()
#bot.movie_review("titanic")
