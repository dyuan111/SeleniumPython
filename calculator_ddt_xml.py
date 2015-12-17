__author__ = 'yiyuan'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

from parameterized_testcase import parameterize
import xml.etree.cElementTree as ET1
import xml.etree.ElementTree as ET


params = {}  #declare before using it
xml= ET.parse("../data/data.xml")
root = xml.getroot()
for test in root.iter('test'):
    test_name = test.attrib['name']
    params[test_name] = {child.tag:child.text for child in test}






class Calculator:  #(unittest.TestCase) is removed since we are not running unit test here
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://chemistry.about.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_calculator(self):
        driver = self.driver
        driver.get(self.base_url + "/library/weekly/blcalculator.htm")
        prefix = "cal"
        driver.find_element_by_name(prefix+ str(self.num1)).click()
        driver.find_element_by_name(prefix+self.operator).click()
        driver.find_element_by_name(prefix + str(self.num2)).click()
        driver.find_element_by_name("calequal").click()
        #self.assertEqual(str(self.result), driver.find_element_by_name("calcResults").get_attribute("value"))
        assert str(self.result)== driver.find_element_by_name("calcResults").get_attribute("value")
        driver.find_element_by_class_name()


    def tearDown(self):
        self.driver.quit()

cases = parameterize(cases = [Calculator], params=params)