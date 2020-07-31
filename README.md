# selenium_twitter_scraper
Scrape all of the posts on a user's Twitter page in Selenium with Python without using the Twitter API. 

# Getting Started

Download twitter.py and the web driver that matches the version of the browser you plan to use ('chromedriver.exe' is the default filepath for the webdriver).

## Scrape all the tweets on Github's twitter page, saving them as github_tweets.json

    from twitter import Twitter
    twitter = Twitter('https://twitter.com/github', 'github_tweets.json')
    twitter.scrape()


## Scrape all the tweets on Github's twitter page, saving them as github_tweets.json

    from twitter import Twitter
    twitter = Twitter('https://twitter.com/github', 'github_tweets.json')
    twitter.scrape(100)
