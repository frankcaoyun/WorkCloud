# Reference: https://maoviola.medium.com/a-complete-guide-to-web-scraping-linkedin-job-postings-ad290fcaa97f

import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By

# define the url for scraping
url = 'https://www.linkedin.com/jobs/search?keywords=Machine%20Learning%20Engineer&location=Singapore%2C%20Singapore&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit&position=1&pageNum=0'

# set up chromedriver
wd = webdriver.Chrome(executable_path='./chromedriver.exe')
wd.get(url)

# get the number of jobs
no_of_jobs = wd.find_element(By.CSS_SELECTOR, 'span.results-context-header__new-jobs')
# no_of_jobs = wd.find_element(By.CSS_SELECTOR, 'h1>span')
# print('test: ', no_of_jobs.get_attribute(name='class'))
# print('test: ', no_of_jobs.getText())
print("attributes: ", dir(no_of_jobs))
print("text: ", no_of_jobs.text)

# print('the number of jobs are: \n', no_of_jobs)

