__author__ = 'yiyuan'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

from parameterized_testcase import parameterize
import csv


# params = {
#      'addition':{
#         'num1':7,
#         'operator':'plus',
#         'num2': 8,
#         'result': 15
#     },
#      'subtraction':{
#         'num1':7,
#         'operator':'minus',
#         'num2': 8,
#         'result': -1
#     },
#     'multiplication':{
#         'num1':7,
#         'operator':'mul',
#         'num2': 8,
#         'result': 56
#     },
#      'division':{
#         'num1':8,
#         'operator':'div',
#         'num2': 2,
#         'result': 4
#     },
#     'division by zero':{
#         'num1':5,
#         'operator':'div',
#         'num2': 0,
#         'result': 'Infinity'
#     }
# }

params = {}  #declare before using it
with open("../data/data.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        params[row.pop('test')] = row

    #or do it this way
    # params = {row.pop('test'):row for row in reader}

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