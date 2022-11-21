# Reference: https://maoviola.medium.com/a-complete-guide-to-web-scraping-linkedin-job-postings-ad290fcaa97f

from selenium import webdriver
import time
import pandas as pd

# define the url for scraping
url = 'https://www.linkedin.com/jobs/search?keywords=Machine%20Learning%20Engineer&location=Singapore%2C%20Singapore&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit&position=1&pageNum=0'

# set up chromedriver
wd = webdriver.Chrome(executable_path='./chromedriver.exe')
wd.get(url)

# get the number of jobs
no_of_jobs = int(wd.find_element(
    'h1>span').get_attribute('innerText'))

print(no_of_jobs)