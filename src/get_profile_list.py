import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from time import sleep
from parsel import Selector, SelectorList
from bs4 import BeautifulSoup
import os
load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')


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

driver = webdriver.Chrome('/usr/local/bin/chromedriver')

login_linkedin()
search_google('enterprise architect','viet nam')
urls = scrape_google_results(100,'ea_list.csv')


name = '//*/div[2]/div[2]/div[1]/ul[1]/li[1]/text()'
title = '//*/div[2]/div[2]/div[1]/h2/text()'
experience = '//*[@id="ember128"]/div[2]/h3'

for i in range(len(urls)):
    driver.get(urls[i])
    sel = Selector(text=driver.page_source)
    sleep(1)
    name = sel.xpath('//*/div[2]/div[2]/div[1]/ul[1]/li[1]/text()').extract_first()
    if name:
        name = name.strip()

    print(urls[i], name)

def set_df_value(css_selector, name,  i):
    res.at[i,name] = soup.select(css_selector)[0].get_text().strip()

def set_df_values(css_selector, name, i):
    res.at[i,name] = [text.get_text().strip() for text in soup.select(css_selector)]


res = pd.DataFrame(dtype=object)
for i in range(1):
    i = 0
    driver.get(urls[i])

    soup = BeautifulSoup(driver.page_source)
    set_df_value('li.inline','name',i)
    set_df_value('h2.mt1','title',i)
    set_df_value('span.t-16.t-black','connections',i)
    set_df_values('.full-width.ember-view h3','experiences',i)
res

soup.select('.full-width.ember-view h3')

[text.get_text().strip() for text in soup.select('h3.pv-entity__school-name')]
set_df_values('.full-width.ember-view h3','experiences',i)

res.at[1,'experiences'] = [text.get_text().strip() for text in soup.select('.full-width.ember-view h3')]


driver.get(urls[i])
show_more_link = driver.find_elements_by_css_selector('.lt-line-clamp__line a')
[ele.click() for ele in show_more_link]

driver.find_element_by_css_selector('li.pv-profile-section__card-item-v2').get_attribute('outerHTML')


from scrape_linkedin import ProfileScraper
