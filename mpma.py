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
		action = ActionChains(self.driver)
		action.pause(timer)
		action.perform()


class Se:
	def __init__(self):
		pass


	def get_header(self, driver):
		fields = []
		for list in range(1,19):
			path = '/html/body/div[2]/div[1]/section[4]/div[1]/div[1]/div[2]/div[1]/div[2]/div[6]/ul[1]/li[' + str(list) + ']/div[1]/span[1]'
			print(path)
			header = driver.find_element(By.XPATH, path)
			fields.append(header.text)

		print(fields)
		return fields 


	def get_company(self, driver, list1, list2):
		for tr in range(list1, list2 + 1):
			Pause(driver).pause(1)

			path = '/html/body/div[2]/div[1]/section[5]/div[1]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[' + str(tr) + ']/td[1]/span[1]/a'
			wait = WebDriverWait(driver, 0)
			clickable = EC.element_to_be_clickable((By.XPATH, path))
			link = wait.until(clickable)
			link.click()

			#name of csv file 
			filename = "company.csv"
			fields   = self.get_header(driver)
				
			#writing to csv file 
			with open(filename, 'w') as csvfile: 
				#creating a csv writer object 
				csvwriter = csv.writer(csvfile) 
					
				#writing the fields 
				csvwriter.writerow(fields) 
	
				li = driver.find_elements(By.CLASS_NAME, "flexi")

				for element in li:

					#data rows of csv file 
					rows = [
						['Nikhil', 'COE', '2', '9.0'], 
						['Sanchit', 'COE', '2', '9.1'], 
						['Aditya', 'IT', '2', '9.3'], 
						['Sagar', 'SE', '1', '9.5'], 
						['Prateek', 'MCE', '3', '7.8'], 
						['Sahil', 'EP', '2', '9.1']
					]
						
					#writing the data rows 
					csvwriter.writerows(rows)

			driver.back()


	def components(self):
		option = webdriver.EdgeOptions()
		option.add_argument("start-maximized");
		driver = webdriver.Edge(options = option)
		driver.get('https://www.mpmadirectory.org.my/all-members')

		driver.execute_script("window.scrollTo(0,  650)")
		self.get_company(driver,  1, 1)
		driver.execute_script("window.scrollTo(0, 1200)")
		#self.get_company(driver, 11, 20)

		driver.quit()


if __name__ == '__main__':
	#os.system('tput reset')

	se = Se()
	se.components()
