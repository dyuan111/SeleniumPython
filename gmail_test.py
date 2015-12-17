from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime

__author__ = 'yiyuan'
import unittest
from selenium import webdriver

class Gmail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.wait= WebDriverWait(self.driver, 30)
        self.action = ActionChains(self.driver)

    def test_gmail(self):
        driver = self.driver
        driver.get("http://mail.google.com")

      #  self.action.move_to_element(element1).move_to_element()

        driver.find_element_by_id('Email').send_keys('kaya7384@gmail.com')
        driver.find_element_by_id('next').click()

        self.wait.until(
            EC.visibility_of_element_located((By.ID, 'Passwd'))).send_keys('SeleniumMinutes123')
        driver.find_element_by_id('signIn').click()

        driver.find_element_by_xpath('//div[contains(text(), "COMPOSE")]').click()

        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[role="dialog"]')))

        #driver.find_element_by_xpath("//div[contains(text(),'Recipient')").click()
        self.wait.until(EC.visibility_of_element_located((By.NAME,'to'))).send_keys('kaya7384@gmail.com')

        subject = "Selenium class:{0}".format(str(datetime.now()))
        driver.find_element_by_name('subjectbox').send_keys(subject)
        #driver.find_element_by_css_selector("[role='textbox']").send_keys("Wow!")
        driver.find_element_by_xpath("//div[@role = 'textbox']").send_keys("Wow!")

        body = driver.find_element_by_css_selector("table div.editable[aria-label=\"Message Body\"]")
        driver.execute_script('arguments[0].textContent = "Wow! This works!"', body)

        driver.find_element_by_xpath("//div[contains(text(), 'Send')]").click()
        #driver.find_element_by_css_selector()

        #wait for 2 miniutes to check email arrival
        try:
            WebDriverWait(driver, 120).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"[role = 'link'] b"),subject))
        except TimeoutException:
            assert False, "The email was not received within 2 minutes after it was sent"



        # print('Hello Class  :)')


    # def tearDown(self):
    #     self.driver.quit()