#!/usr/bin/env python
"""New problem: Navigating back to the search page after getting textbook info needs to clear the books already selected, and also begin selectingn from the the correct column at the correct spot.
"""
"""
Python script for scraping the results from http://architectfinder.aia.org/frmSearch.aspx
"""

import re
import string
import urlparse
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
"""
selectTerm = Select(self.driver.find_element_by_id('ctl00_ctl00_Content_Content_courseSelect_select_term'))
optionIndexesTerm = range(1, len(selectTerm.options))

for indexes in optionIndexesTerm:
    selectTerm.select_by_index(indexes)
    selectDept = Select(self.driver.find_element_by_id('ctl00_ctl00_Content_Content_courseSelect_select_dept'))
    optionIndexesDept = range(1, len(selectDept.options))
    for indexesTerm in optionIndexesDept:
        selectSect = Select(self.driver.find_element_by_id('ctl00_ctl00_Content_Content_courseSelect_select_section'))
        optionIndexesSect = range(1, len(selectSect.options))
        selectSect.select_by_index(indexesTerm)
        self.driver.find_element_by_id('ctl00_ctl00_Content_Content_courseSelect_btnAddCourseToList').click()
       # self.driver.find_element_by_id('ctl00_ctl00_Content_Content_btnGetCourseMaterials').click()
        
s - BeautifulSoup(self.driver.page_source)
#for span in s.findAll('span', id=)
for span in s.findAll('span', {'id' : 'ctl00_ctl00_Content_Content_courseSearchList_courseList_ctl00_instructorLabel'}):
    print 'instructor: ', span.text
    print
self.driver.quit()"""

class ArchitectFinderScraper(object):
    def __init__(self):
        #self.url = "http://architectfinder.aia.org/frmSearch.aspx"
        self.url = "http://bookstore.middlebury.edu/SelectTermDept.aspx"
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1120, 550)

        
    

    def scrape(self):
        termVals = ['']
        self.driver.get(self.url)
        selectTerm = Select(self.driver.find_element_by_id('ctl00_ctl00_Content_Content_courseSelect_select_term'))
        optionIndexesTerm = range(0, len(selectTerm.options))
        counter = 0
        submitNow = 0
        for indexes in optionIndexesTerm:
           # print indexes
            selectTerm.select_by_index(indexes)
            time.sleep(3)
            #selectTerm.select_by_value('6907')
            #self.driver.implicitly_wait(10)
          #  self.driver.find_element_by_css_selector('value.'+'6907').click()
            
            #self.driver.indexes.click()
            selectDept = Select(self.driver.find_element_by_id('ctl00_ctl00_Content_Content_courseSelect_select_dept'))
            optionIndexesDept = range(0, len(selectDept.options))
            interation = 0
#not executing this loop.
            for indexesSect in optionIndexesDept:
                selectDept.select_by_index(indexesSect)
                time.sleep(3)
               # self.driver.save_screenshot('lol.png')
                #break 
                selectSect = Select(self.driver.find_element_by_id('ctl00_ctl00_Content_Content_courseSelect_select_section'))
                optionIndexesSect = range(0, len(selectSect.options))
                counter = 0
                if submitNow == 1:
                    optionIndexesSect = range(iteration, len(selectSect.options))

                for indexesBooks in optionIndexesSect:
                    selectSect.select_by_index(indexesBooks)
                    #time.sleep(3)
                    counter += 1
                    iteration = counter
                   
                    if counter >= 5:       
                        print "here"          
                        submitNow = 1
                        self.driver.find_element_by_id('ctl00_ctl00_Content_Content_btnGetCourseMaterials').click()
                        time.sleep(3)
                        s = BeautifulSoup(self.driver.page_source, "html.parser")
                        count = 0
                       # tag = s.findAll('div', {'class': 'material_info'})
                        for tag in s.findAll('h3'):
                            print "inside for loop"
                            print tag.text
                        #break
                        
                        #break
                    
                    if submitNow == 1:
                         self.driver.execute_script("window.history.go(-1)")
                         time.sleep(3)
                         #selectDept = Select(self.driver.find_element_by_id('ctl00_ctl00_Content_Content_courseSelect_select_dept'))
                         #optionIndexesDept = range(0, len(selectDept.options))
                         selectSect = Select(self.driver.find_element_by_id('ctl00_ctl00_Content_Content_courseSelect_select_section'))
                         optionIndexesSect = range(0, len(selectSect.options))
                         self.driver.find_element_by_id('ctl00_ctl00_Content_Content_courseSelect_btnAddCourseToList').click() #not really sure why this works but it does
                         time.sleep(3)
                         selectDept.select_by_index(indexesSect)
                         time.sleep(3)
          
                         """self.driver.find_element_by_id('ctl00_ctl00_Content_Content_courseSelect_btnAddCourseToList').click()
                         time.sleep(3)

                         selectSect = Select(self.driver.find_element_by_id('ctl00_ctl00_Content_Content_courseSelect_select_section'))
                         optionIndexesSect = range(0, len(selectSect.options))
                         submitNow = 0

                         selectSect = Select(self.driver.find_element_by_id('ctl00_ctl00_Content_Content_courseSelect_select_section'))
                         optionIndexesSect = range(0, len(selectSect.options))"""
                         
                         
                         
                         """selectSect = Select(self.driver.find_element_by_id('ctl00_ctl00_Content_Content_courseSelect_select_section'))
                         optionIndexesSect = range(0, len(selectSect.options))
                         submitNow = 0"""
                         self.driver.save_screenshot('lol.png')
                         print "printing image"
                         break
                    else:
                        self.driver.find_element_by_id('ctl00_ctl00_Content_Content_courseSelect_btnAddCourseToList').click()
                        time.sleep(3)

                        selectSect = Select(self.driver.find_element_by_id('ctl00_ctl00_Content_Content_courseSelect_select_section'))
                        optionIndexesSect = range(0, len(selectSect.options))
                  
                    #self.driver.save_screenshot('lol.png')
                    #print "printing image"
                   

                    

                    
                    #self.driver.save_screenshot('lol.png')
                    #break
                
                #selectDept = Select(self.driver.find_element_by_id('ctl00_ctl00_Content_Content_courseSelect_select_dept'))
                #optionIndexesDept = range(0, len(selectDept.options))
                break
                
                #break

                #print counter
                #print
                #counter += 1
            
            #selectTerm = Select(self.driver.find_element_by_id('ctl00_ctl00_Content_Content_courseSelect_select_term'))
            #optionIndexesTerm = range(0, len(selectTerm.options))
            break

        #self.driver.save_screenshot('lol.png')
                
                #wait = WebDriverWait(self.driver, 10)
                # self.driver.find_element_by_id('ctl00_ctl00_Content_Content_btnGetCourseMaterials').click()
      
      
     
    
        
        self.driver.quit()
        print "haha"
        

"""
    def scrape(self):
        self.driver.get(self.url)
        
        try:
            self.driver.find_element_by_id('ctl00_ContentPlaceHolder1_btnAccept').click()
        except NoSuchElementException:
            pass

        select = Select(self.driver.find_element_by_id('ctl00_ContentPlaceHolder1_drpState'))
        option_indexes = range(1, len(select.options))

        for index in option_indexes[:3]:
            select.select_by_index(index)
            self.driver.find_element_by_id('ctl00_ContentPlaceHolder1_btnSearch').click()

            #
            # Wait for results to finish loading
            #
            wait = WebDriverWait(self.driver, 10)
            wait.until(lambda driver: driver.find_element_by_id('ctl00_ContentPlaceHolder1_uprogressSearchResults').is_displayed() == False)

            pageno = 2

            while True:
                s = BeautifulSoup(self.driver.page_source)
                r1 = re.compile(r'^frmFirmDetails\.aspx\?FirmID=([A-Z0-9-]+)$')
                r2 = re.compile(r'hpFirmName$')
                x = {'href': r1, 'id': r2}

                for a in s.findAll('a', attrs=x):
                    print 'firm name: ', a.text
                    print 'firm url: ', urlparse.urljoin(self.driver.current_url, a['href'])
                    print 

                # Pagination
                try:
                    next_page_elem = self.driver.find_element_by_xpath("//a[text()='%d']" % pageno)
                except NoSuchElementException:
                    break # no more pages

                print 'page ', pageno, '\n'
                next_page_elem.click()

                def next_page(driver):
                    '''
                    Wait until the next page background color changes indicating
                    that it is now the currently selected page
                    '''
                    style = driver.find_element_by_xpath("//a[text()='%d']" % pageno).get_attribute('style')
                    return 'background-color' in style

                wait = WebDriverWait(self.driver, 10)
                wait.until(next_page)

                pageno += 1

        self.driver.quit()"""

if __name__ == '__main__':
    scraper = ArchitectFinderScraper()
    scraper.scrape()        







   





    """s = BeautifulSoup(self.driver.page_source, "html.parser")
        for span in s.findAll('span', id='ctl00_ctl00_Content_Content_courseSearchList_courseList_ctl00_instructorLabel'):
            print span.text
            print

        for tag in s.findAll('table', {'class' : 'cart'}):
            spanTags = tag.findAll('span', {'id': 'ctl00_ctl00_Content_Content_courseSearchList_courseList_ctl00_instructorLabel'})
            for tag in spanTags:
                print tag.text"""