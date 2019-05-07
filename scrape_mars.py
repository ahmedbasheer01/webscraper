#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import pymongo


# In[2]:


#load driver for Splinter
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# URL of page to be scraped
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

#create a str of the webpage code
html = browser.html

# Create BeautifulSoup object; parse with 'html'
soup = bs(html, 'html.parser')


# In[16]:


#initiate empty dictionary
mars_dict=[]


# In[17]:


# Get first 1st news title
div_result = soup.find('div', class_='content_title')
news_title = div_result.find('a').text


# In[19]:


# Get teaser of 1st news article
news_teaser = soup.find('div', class_='article_teaser_body').text
news_teaser
mars_dict.append({"News Title":news_title, "News Teaser":news_teaser})


# In[21]:


#load driver for Splinter
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

#visit jpl spaceimages
url = 'https://www.jpl.nasa.gov/spaceimages/'
browser.visit(url)

#create a str of the webpage code
html = browser.html

# Create BeautifulSoup object; parse with 'html'
soup = bs(html, 'html.parser')


# In[22]:


# Get URL of Featured Image, concat initial portion of link
featured_image_url = 'https://www.jpl.nasa.gov' + soup.find('a', class_='button fancybox')['data-fancybox-href']
mars_dict.append({"Featured URL":featured_image_url})


# In[23]:


#load driver for Splinter
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

#visit mars weather Twitter account
url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)

#create a str of the webpage code
html = browser.html

# Create BeautifulSoup object; parse with 'html'
soup = bs(html, 'html.parser')


# In[24]:


#extract latest tweet with weather
latest_tweet = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")

#remove anchor tag and associated text from paragraph 
unwanted = latest_tweet.find('a')
unwanted.extract()

latest_tweet = latest_tweet.text.strip()
mars_dict.append({"Latest Tweet":latest_tweet})


# In[25]:


url = 'https://space-facts.com/mars/'

#extract all tables into a list
tables = pd.read_html(url)
mars_dict.append({"Space Facts":tables[0]})


# In[26]:


#use first table from list
mars_facts_df = tables[0]

#rename columns
mars_facts_df.columns = ['Parameter', 'Measure']


# In[27]:


#List with test you want to click later
mars_hemisps = ["Cerberus Hemisphere Enhanced","Schiaparelli Hemisphere Enhanced",
              "Syrtis Major Hemisphere Enhanced", "Valles Marineris Hemisphere Enhanced"]

#empty list to store dictionary
mars_hemisps_dict=[]

#load driver for Splinter
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

#visit mars weather Twitter account
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

#create a str of the webpage code
html = browser.html

# Create BeautifulSoup object; parse with 'html'
soup = bs(html, 'html.parser')

#loop to click test, extract data, and return to original page
for hemi in mars_hemisps:
    browser.click_link_by_partial_text(hemi)
    
    html = browser.html

    # Create BeautifulSoup object; parse with 'html'
    soup = bs(html, 'html.parser')

    # Get first 1st news title
    image_title = soup.find('h2', class_='title').text

    #get url, create final url
    image_url = 'https://astrogeology.usgs.gov' + soup.find('img', class_='wide-image')['src']
    
    dict = {"title":image_title, "URL":image_url}
    
    mars_dict.append(dict)

    browser.back()


# In[28]:


#Print List
mars_dict

