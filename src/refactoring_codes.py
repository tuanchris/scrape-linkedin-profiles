import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from time import sleep
from parsel import Selector, SelectorList
from bs4 import BeautifulSoup
import os

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
