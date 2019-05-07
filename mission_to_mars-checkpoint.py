{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import dependencies\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as bs\n",
    "import pandas as pd\n",
    "import requests\n",
    "import pymongo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "#load driver for Splinter\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# URL of page to be scraped\n",
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)\n",
    "\n",
    "#create a str of the webpage code\n",
    "html = browser.html\n",
    "\n",
    "# Create BeautifulSoup object; parse with 'html'\n",
    "soup = bs(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'InSight Captures Sunrise and Sunset on Mars'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get first 1st news title\n",
    "div_result = soup.find('div', class_='content_title')\n",
    "news_title = div_result.find('a').text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"InSight joins the rest of NASA's Red Planet surface missions, all of which have photographed either the start or end of a Martian day.\""
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get teaser of 1st news article\n",
    "news_p = soup.find('div', class_='article_teaser_body').text\n",
    "news_p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [],
   "source": [
    "#load driver for Splinter\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "#visit jpl spaceimages\n",
    "url = 'https://www.jpl.nasa.gov/spaceimages/'\n",
    "browser.visit(url)\n",
    "\n",
    "#create a str of the webpage code\n",
    "html = browser.html\n",
    "\n",
    "# Create BeautifulSoup object; parse with 'html'\n",
    "soup = bs(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA18847_ip.jpg'"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get URL of Featured Image, concat initial portion of link\n",
    "featured_image_url = 'https://www.jpl.nasa.gov' + soup.find('a', class_='button fancybox')['data-fancybox-href']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "#load driver for Splinter\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "#visit mars weather Twitter account\n",
    "url = 'https://twitter.com/marswxreport?lang=en'\n",
    "browser.visit(url)\n",
    "\n",
    "#create a str of the webpage code\n",
    "html = browser.html\n",
    "\n",
    "# Create BeautifulSoup object; parse with 'html'\n",
    "soup = bs(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "InSight sol 154 (2019-05-03) low -97.6ºC (-143.7ºF) high -17.2ºC (1.0ºF)\n",
      "winds from the SW at 4.5 m/s (10.0 mph) gusting to 13.1 m/s (29.2 mph)\n",
      "pressure at 7.40 hPapic.twitter.com/0KZXlbiuXO\n"
     ]
    }
   ],
   "source": [
    "#extract latest tweet with weather\n",
    "latest_tweet = soup.find('p', class_=\"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text\")\n",
    "\n",
    "#remove anchor tag and associated text from paragraph \n",
    "unwanted = latest_tweet.find('a')\n",
    "unwanted.extract()\n",
    "\n",
    "latest_tweet = latest_tweet.text.strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://space-facts.com/mars/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[                      0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.42 x 10^23 kg (10.7% Earth)\n",
       " 3                Moons:            2 (Phobos & Deimos)\n",
       " 4       Orbit Distance:       227,943,824 km (1.52 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                  -153 to 20 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers]"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#extract all tables into a list\n",
    "tables = pd.read_html(url)\n",
    "tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Parameter</th>\n",
       "      <th>Measure</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.42 x 10^23 kg (10.7% Earth)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.52 AU)</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              Parameter                        Measure\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.42 x 10^23 kg (10.7% Earth)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.52 AU)"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#use first table from list\n",
    "mars_facts_df = tables[0]\n",
    "\n",
    "#rename columns\n",
    "mars_facts_df.columns = ['Parameter', 'Measure']\n",
    "\n",
    "mars_facts_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [],
   "source": [
    "#List with test you want to click later\n",
    "mars_hemisps = [\"Cerberus Hemisphere Enhanced\",\"Schiaparelli Hemisphere Enhanced\",\n",
    "              \"Syrtis Major Hemisphere Enhanced\", \"Valles Marineris Hemisphere Enhanced\"]\n",
    "\n",
    "#empty list to store dictionary\n",
    "mars_hemisps_dict=[]\n",
    "\n",
    "#load driver for Splinter\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "#visit mars weather Twitter account\n",
    "url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(url)\n",
    "\n",
    "#create a str of the webpage code\n",
    "html = browser.html\n",
    "\n",
    "# Create BeautifulSoup object; parse with 'html'\n",
    "soup = bs(html, 'html.parser')\n",
    "\n",
    "#loop to click test, extract data, and return to original page\n",
    "for hemi in mars_hemisps:\n",
    "    browser.click_link_by_partial_text(hemi)\n",
    "    \n",
    "    html = browser.html\n",
    "\n",
    "    # Create BeautifulSoup object; parse with 'html'\n",
    "    soup = bs(html, 'html.parser')\n",
    "\n",
    "    # Get first 1st news title\n",
    "    image_title = soup.find('h2', class_='title').text\n",
    "\n",
    "    #get url, create final url\n",
    "    image_url = 'https://astrogeology.usgs.gov' + soup.find('img', class_='wide-image')['src']\n",
    "    \n",
    "    dict = {\"title\":image_title, \"URL\":image_url}\n",
    "    \n",
    "    mars_hemisps_dict.append(dict)\n",
    "\n",
    "    browser.back()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere Enhanced',\n",
       "  'URL': 'https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'URL': 'https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'URL': 'https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'URL': 'https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg'}]"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Print List\n",
    "mars_hemisps_dict"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
