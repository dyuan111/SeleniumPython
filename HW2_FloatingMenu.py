__author__ = 'yiyuan'

# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

class HW2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)


    def test_floatingmenu(self):
        driver = self.driver
        driver.get("http://www.tie3.mypalmbeachpost.com/news/entertainment/sushi-impresses-at-juno-beachs-china-tokyo/nXspN")
        # driver.find_element_by_css_selector("a.pq-access-meter-close.pq-close-modal").click()
        #wait.until(EC.presence_of_element_located((By.ID, 'pq-passage-quota-welcome'))).find_element_by_class_name('pg-close-modal').click()

        driver.find_element_by_xpath("(//a[contains(text(),'X')])[2]").click()

        #scroll down
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight )")

        article = driver.find_element_by_xpath("//div[@class='article']")
        article_location = article.location
        print "article location: " + str(article_location)
        article_size = article.size
        # print "article size: " + str(article_size)
        # article_right_bound = article_location['x']+ article_size['width']
        article_bottom_bound = article_location['y']+article_size['height']
        print "article bottom bound: " + str(article_bottom_bound)

        floating_menu = driver.find_element_by_xpath('//div[@class = "category-list"]')
        floating_menu_location = floating_menu.location
        print "menu location:" + str(floating_menu_location)
        floating_menu_size = floating_menu.size
        print "menu size: "+ str(floating_menu_size)
        menu_bottom_bound = floating_menu_location['y']+floating_menu_size['height']
        print "menu bottom bound: " + str(menu_bottom_bound)

        assert article_bottom_bound == menu_bottom_bound,\
        "article buttom found is {0}, but the menu bottom is {1}".format(article_bottom_bound, menu_bottom_bound)

#scroll to the top
        driver.execute_script("window.scrollTo(0,0)")
        article_y_position = article.location['y']
        print "current y position of article " + str(article_y_position)

        floating_y_position = floating_menu.location['y']
        print "menu y location is: " + str(floating_y_position)

        ad_class = driver.find_element_by_class_name('RP01')
        ad_frame = ad_class.find_element_by_tag_name('iframe')

        driver.switch_to_frame(ad_frame)
        ad = driver.find_element_by_xpath('//div[@id="google_image_div"]')

        ad_upper_y= ad.location['y']
        print "Ad upper y position is " + str(ad_upper_y)
        #ad_bottom_bound = ad_upper_y + ad.size['height']
        print "Ad height is: " + str(ad.size['height'])

        #ad_warning = driver.find_element_by_class_name('ad-warning')

        expected_position = article_y_position + ad.size['height']+14  #14 might be wrong, it is the space between the Ad image and the menu
        assert floating_y_position == expected_position,\
        "Expected menu position is {0}, but the acutal position is {1}".format(expected_position, floating_y_position)



    def tearDown(self):
        self.driver.quit()
