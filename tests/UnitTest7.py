import unittest
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner
from utils.Constants import constants

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get(constants.url)
        cls.driver.maximize_window()

    def test_a_login(self):
        # try:
        self.driver.find_element_by_id("userme").send_keys(constants.username)
        self.driver.find_element_by_id("password").send_keys(constants.password)
        self.driver.find_element_by_id("Login").click()

        time.sleep(5)
        self.driver.get_screenshot_as_file("C:/Users/Srujan/PycharmProjects/SampleFW/screenshots/loginsuccess.png")
            # except EnvironmentError:
            # print("in catch block")



    # def test_b_createUser(self):
    #     self.driver.find_element_by_xpath("//a[@title='Create Menu']").click()
    #     self.driver.find_element_by_xpath("//span[@class='slds-align-middle']").click()
    #     time.sleep(8)
    #     frame1 = self.driver.find_element_by_xpath("//iframe[@title='New User ~ Salesforce - Developer Edition']")
    #     self.driver.switch_to.frame(frame1)
    #     self.driver.find_element_by_id("name_firstName").send_keys("surendra firstname")

    @classmethod
    def tearDownClass(cls):
        time.sleep(4)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Srujan/PycharmProjects/SampleFW/reports'),verbosity=2)
