import os
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
			company_header_path = '/html/body/div[2]/div[1]/section[4]/div[1]/div[1]/div[2]/div[1]/div[2]/div[6]/ul[1]/li[' + str(list) + ']/div[1]/span[1]'
			header = driver.find_element(By.XPATH, company_header_path)
			fields.append(header.text)

		return fields 


	def get_company(self, driver, list1, list2):
		#name of csv file 
		filename = "company.csv"

		with open(filename, 'w') as csvfile: 
			#creating a csv writer object 
			csvwriter = csv.writer(csvfile) 

			for tr in range(list1, list2 + 1):
				if tr <  11:
					driver.execute_script("window.scrollTo(0,  650)")
				if tr == 11:
					driver.execute_script("window.scrollTo(0, 1200)")
				Pause(driver).pause(1)

				main_page_path = '/html/body/div[2]/div[1]/section[5]/div[1]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[' + str(tr) + ']/td[1]/span[1]/a[1]'
				wait = WebDriverWait(driver, 0)
				clickable = EC.element_to_be_clickable((By.XPATH, main_page_path))
				link = wait.until(clickable)
				link.click()

				#writing the fields 
				if tr == 1:
					fields = self.get_header(driver)
					csvwriter.writerow(fields) 

				arr = []
				col = []
				li_limit = 23
				for j in range(1, li_limit):
					company_value_path = '/html/body/div[2]/div[1]/section[4]/div[1]/div[1]/div[2]/div[1]/div[2]/div[6]/ul[1]/li[' + str(j) + ']/div[1]/div[1]'

					if tr == 4 and j == 16:
						company_value_path = '/html/body/div[2]/div[1]/section[4]/div[1]/div[1]/div[2]/div[1]/div[2]/div[6]/ul[1]/li[16]/div[1]/div[1]/a[1]'

					print(j)
					print(main_page_path)
					print(company_value_path)
					li = driver.find_element(By.XPATH, company_value_path)
					col.append(li.text)

				arr.append(col)
				print(arr)	

				#writing the data rows 
				csvwriter.writerows(arr)

				driver.back()


	def components(self):
		option = webdriver.EdgeOptions()
		option.add_argument("start-maximized");
		driver = webdriver.Edge(options = option)
		driver.get('https://www.mpmadirectory.org.my/all-members')

		self.get_company(driver, 3, 4)

		driver.quit()


if __name__ == '__main__':
	#os.system('tput reset')

	se = Se()
	se.components()
