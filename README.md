# RedditApiPostScrapper
Simple wrapper importing data from specified subreddit to CSV file

Wrapper works only with Python 3.

How to get data?

First you need to generate reddit API credentials. Go to https://www.reddit.com/prefs/apps and click "Are You a developer? Create and app". Fulfill the form to obtain "reddit client id" and "secret key" and as "redirect address" you can just type 127.0.0.1. It works https://prnt.sc/l709z4

Then open reddit_api.txt and REPLACE the text in lines with keys, and your account username and password. As "user agent" you can just type anything. As far as I work with reddit API I never had any issues even when I typed there some random characters but just in case I recommend to type something more reasonable than "asd".

When you already fulfilled the form you can run the wrapper. App will ask what subreddit you want to wrap, how much data you want to save and what's the sort. The data is saved as CSV file. By default it saves title, url, author, ups, downs, number of comments, nsfw and date. You can freely edit it just ckeck PRAW documentation and submission class https://praw.readthedocs.io/en/latest/code_overview/models/submission.html

The app was just made for learning purposes if there are any tips or questions feel free to ask :-)
