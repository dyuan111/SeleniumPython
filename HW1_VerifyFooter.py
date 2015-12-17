from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from functions.common import login, logout

__author__ = 'yiyuan'
import unittest
from selenium import webdriver

class HW1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("http://hrm.seleniumminutes.com")

    #this function will verify the right footer text is displayed under each image within Quick Launch div
    def testFooter(self):
        driver = self.driver
        login(driver)
        driver.find_element_by_id('menu_dashboard_index')

        self.assertEqual('Quick Launch',driver.find_element_by_xpath('//legend').text)

        QuickLaunchDict = {'ApplyLeave.png':'Assign Leave',
                          'MyLeave.png':'Leave List',
                          'MyTimesheet.png':'Timesheets',
                          }

        QuickLaunchElements = driver.find_elements_by_xpath('//div[@class = "quickLaunge"]')

        for i in QuickLaunchElements:
            #extract the image file name, which is the last part of the value for src attribute
            curr_img = i.find_element_by_xpath('.//img').get_attribute("src").split('/')[-1]
            #print curr_img
            #get the footer text that matches this image
            curr_footer = i.find_element_by_xpath('.//span').text
            print curr_footer
            #curr_footer = i.find_element_by_xpath('.//img[contains(@src, ".png")]//following-sibling::span').text
            #print QuickLaunchDict[curr_img]
            self.assertEqual(QuickLaunchDict[curr_img], curr_footer)
            # assert QuickLaunchDict[curr_img]== curr_footer,\
            #     "Expected the image name below the {0}, but it was {1} instead".format(0= )



        logout(driver)  #why this line always fails?

    def testEven_Odd_class(self):
        driver = self.driver
        login(driver)
        action = ActionChains(driver)

        # PIM = driver.find_element_by_id('menu_pim_viewPimModule')
        # Employee_list = driver.find_element_by_id('menu_pim_viewEmployeeList')
        # action.move_to_element(PIM)
        # action.move_to_element(Employee_list)
        # action.click()
        driver.find_element_by_id('menu_pim_viewPimModule').click()
        driver.find_element_by_id('menu_pim_viewEmployeeList').click()

        all_rows_on_page = driver.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr')
        count = len(all_rows_on_page)
        # print count
        if count > 0:
            i = 1
            for row in all_rows_on_page:
                #class_value = (driver.find_element_by_xpath('//tbody/tr[{0}]').format(i).get_attribute('class')   this line does not work
                #print i
                class_value = row.get_attribute("class")
                print class_value
                if i%2 == 1:
                    self.assertEqual('odd', class_value)
                else:
                    self.assertEqual('even', class_value)
                i+=1

        logout(driver)



    def tearDown(self):
        self.driver.quit()

