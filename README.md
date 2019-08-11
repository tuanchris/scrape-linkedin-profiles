# Scrape LinkedIn Profiles
A side project to scrape LinkedIn profile and find suitable candidate
## Introduction
This is a python project to scrape LinkedIn profiles from Google search results and scrape all public information from those profiles.

**Warning: LinkedIn has a very strong anti-scraping policy. Use the codes here at your own risks.**

## Install
Clone this repo to your local machine:
```
git clone https://github.com/tuanchris/scrape-linkedin-profiles
```
Navigate to the directory and install the required packages
```
pip install -r requirements.text
```
## Usage

To crawl LinkedIn profiles from Google search, navigate to the `src` folder and run the follow command:
```
python python get_profile_list.py --keyword "Data Analyst" --city "Ha Noi" --pages 10 --output ../data/da_profiles.csv
```
where:
* `keyword`: Title for the position you are scraping
* `city`: City you are searching
* `pages`: Number of Google search pages to scrape
* `output`: Output directory

Input LinkedIn login `email` and `password` when prompted. The crawled LinkedIn profile will be stored in the `output` directory as a `.csv` file.
