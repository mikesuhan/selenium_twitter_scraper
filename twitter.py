import os
import json
import logging
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup


logging.basicConfig(filename='log.log',
                    filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.ERROR)

class Twitter:

    def __init__(self, url, filename, driver='chromedriver.exe', folder='twitter_data'):
        self.url = url
        self.filename = filename
        self.folder = folder
        self.filepath = os.path.join(self.folder, self.filename)
        if not self.filepath.endswith('.json'):
            self.filepath += '.json'
        self.tweets = {}
        self.driver = webdriver.Chrome(driver)


    def scrape(self, max_tweets=0):
        if not os.path.exists(self.folder):
            os.mkdir(self.folder)

        self.driver.get(self.url)
        sleep(2)

        ids = []

        while True:
            for tweet in self.driver.find_elements_by_css_selector("[data-testid=\"tweet\"]"):
                if tweet.id not in ids:
                    ids.append(tweet.id)
                    html = tweet.get_property('innerHTML')
                    html = BeautifulSoup(html, "html.parser")

                    date = html.find('time')['datetime']

                    on_next = False
                    lines = []
                    for line in html.strings:
                        line = line.strip()
                        if line == '·':
                            on_next = 1
                        elif on_next == 1:
                            on_next += 1
                        elif on_next == 2:
                            lines.append(line)


                    for line in reversed(lines):
                        if not line or line[0].isdigit():
                            del lines[-1]
                        else:
                            break

                    lines = ' '.join(lines)
                    self.tweets[date] = lines

                    if len(self.tweets) >= max_tweets:
                        self.save()
                        return None


            self.driver.execute_script('window.scrollTo(0, window.scrollY + window.innerHeight / 2)')
            sleep(1)

            at_bottom = self.driver.execute_script(
                'return window.innerHeight + window.scrollY >= document.body.scrollHeight')
            if at_bottom:
                c = 0
                while c < 10:
                    print(c, "- Trying to load more data just in case it's not really at the bottom. "
                             "Will save after the 10th attempt.")
                    sleep(2)
                    at_bottom = self.driver.execute_script(
                        'return window.innerHeight + window.scrollY >= document.body.scrollHeight')
                    if at_bottom:
                        c += 1
                    else:
                        break
                else:
                    print('Done')
                    self.save()
                    break

    def save(self):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.tweets))

        print('Saved as', self.filepath)