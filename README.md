# selenium_twitter_scraper
Scrape all of the posts on a user's Twitter page in Selenium with Python without using the Twitter API. 

This module works by scrolling down a Twitter page and saving the the text content of every Tweet into a json file.

# Getting Started

Download twitter.py and the web driver that matches the version of the browser you plan to use ('chromedriver.exe' is the default filepath for the webdriver).

## Scrape all the tweets on Github's twitter page, saving them as github_tweets.json

    from twitter import Twitter
    twitter = Twitter('https://twitter.com/github', 'github_tweets.json')
    twitter.scrape()


## Scrape the 100 most recent Tweets on Github's twitter page, saving them as github_tweets.json

    from twitter import Twitter
    twitter = Twitter('https://twitter.com/github', 'github_tweets.json')
    twitter.scrape(100)

# Potential problems

Sometimes <div> elements containing tweets will disappear from the DOM structure after the driver.find_elements_by_css_selector() method has been called, which will result in the following error:

        stale element reference: element is not attached to the page document 
        
Making the window scroll down at a slower rate will sometimes stop this from happening. This line, near the middle of the Twitter.scrape() method, controls how far the window scrolls down each time:

        self.driver.execute_script('window.scrollTo(0, window.scrollY + window.innerHeight / 2)')
        
 You might try changing the 2 at the end to a larger number.
 
Increaseing the sleep() times in different parts of the code may also do the trick at eliminating this error. 
