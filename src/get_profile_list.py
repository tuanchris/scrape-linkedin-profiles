import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from time import sleep
from parsel import Selector, SelectorList
from bs4 import BeautifulSoup
import os
import argparse
import getpass


username = input('LinkedIn email: ')
password = getpass.getpass()


parser = argparse.ArgumentParser(description='Crawl linkedin profiles from Google with title and city')
parser.add_argument('--keyword')
parser.add_argument('--city')
parser.add_argument('--pages',default=10)
parser.add_argument('--output')
args = parser.parse_args()

def login_linkedin():
    driver.get('https://www.linkedin.com/login')
    sleep(0.5)
    driver.find_element_by_id('username').send_keys(username)
    sleep(0.5)
    driver.find_element_by_id('password').send_keys(password)
    sleep(0.5)
    login_button = driver.find_element_by_class_name('login__form_action_container ')
    login_button.click()
    sleep(0.5)

def search_google(title,city):
    driver.get('https://www.google.com')
    search_query = driver.find_element_by_name('q')
    sleep(0.5)
    search_query.send_keys(f'site:linkedin.com/in/ AND "{title}" AND "{city}"')
    sleep(0.5)
    search_query.send_keys(Keys.RETURN)
    sleep(0.5)


def scrape_google_results(pages, file_name):
    urls = []
    while True and pages > 0:
        try:
            linkedin_urls = driver.find_elements_by_class_name('iUh30')
            sleep(0.5)
            urls.append([url.text for url in linkedin_urls])
            next = driver.find_element_by_xpath('//*[@id="pnnext"]/span[2]')
            next.click()
            sleep(0.5)
            pages -= 1
        except:
            break

    urls = pd.Series(sum(urls, []))
    urls.to_csv(file_name,index=False)
    return urls

if __name__ == '__main__':
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    login_linkedin()
    search_google(args.keyword,args.city)
    urls = scrape_google_results(args.pages,args.output)
