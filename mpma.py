import os
import pandas as pd
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class Pause:
	def __init__(self, driver):
		self.driver = driver
		pass

	def pause(self, timer):
		self.timer  = timer
		action = ActionChains(self.driver)
		action.pause(self.timer)
		action.perform()


class Se:
	def __init__(self):
		pass

	def company(self, driver, list1, list2):
		self.driver = driver
		self.list1  = list1
		self.list2  = list2

		for tr in range(self.list1, self.list2 + 1):
			Pause(self.driver).pause(1)

			p = '/html/body/div[2]/div[1]/section[5]/div[1]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[' + str(tr) + ']/td[1]/span[1]/a'
			wait = WebDriverWait(self.driver, 0)
			clickable = EC.element_to_be_clickable((By.XPATH, p))
			link = wait.until(clickable)
			link.click()
			li = driver.find_elements(By.CLASS_NAME, "flexi")

			for element in li:

				c  = '//*[@id="flexicontent"]/div[6]/ul/li[1]/div/span'
				header1 = driver.find_element(By.XPATH, c)
				print(header1.text)

				d  = '//*[@id="flexicontent"]/div[6]/ul/li[2]/div/span'
				header2 = driver.find_element(By.XPATH, d)
				print(header2.text)

				e = '//*[@id="flexicontent"]/div[6]/ul/li[3]/div/span'
				header3 = driver.find_element(By.XPATH, e)
				print(header3.text)

				# field names 
				fields = ['Name', 'Branch', 'Year', 'CGPA'] 
					
				# data rows of csv file 
				rows = [ ['Nikhil', 'COE', '2', '9.0'], 
						 ['Sanchit', 'COE', '2', '9.1'], 
						 ['Aditya', 'IT', '2', '9.3'], 
						 ['Sagar', 'SE', '1', '9.5'], 
						 ['Prateek', 'MCE', '3', '7.8'], 
						 ['Sahil', 'EP', '2', '9.1']] 
					
				# name of csv file 
				filename = "university_records.csv"
					
				# writing to csv file 
				with open(filename, 'w') as csvfile: 
					# creating a csv writer object 
					csvwriter = csv.writer(csvfile) 
						
					# writing the fields 
					csvwriter.writerow(fields) 
						
					# writing the data rows 
					csvwriter.writerows(rows

			driver.back()


	def components(self):
		option = webdriver.EdgeOptions()
		option.add_argument("start-maximized");
		driver = webdriver.Edge(options = option)
		driver.get('https://www.mpmadirectory.org.my/all-members')

		driver.execute_script("window.scrollTo(0,  650)")
		self.company(driver,  1, 1)
		driver.execute_script("window.scrollTo(0, 1200)")
		#self.company(driver, 11, 20)

		driver.quit()


if __name__ == '__main__':
	#os.system('tput reset')

	se = Se()
	se.components()
