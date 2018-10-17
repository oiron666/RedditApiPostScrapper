import praw #Reddit Library
import csv
import time
import datetime

reddit_credentials = (open('reddit api.txt', 'r'))
red_id = reddit_credentials.read().split('\n')
reddit_client_id = red_id[0]
reddit_client_secret = red_id[1]
username = red_id[2]
password = red_id[3]
user_agent = red_id[4]
reddit = praw.Reddit(client_id = reddit_client_id, client_secret = reddit_client_secret, username = username, password = password, user_agent = user_agent) #reddit api data

while True:
    client_input = input('Type subreddit to parse \n')
    while client_input == '':
        client_input = input('Type subreddit to parse \n')
    subreddit_to_parse = reddit.subreddit(client_input)
    test = subreddit_to_parse.new(limit = (100))
    try:
        for submission in test:
            break
        break
    except:
        print('There is not subreddit {client_input}'.format(client_input = client_input))

def set_limit():
    #defines the amount of posts to parse
    type_limit=input('Type limit (1000 max) \n')
    tl_int = int(type_limit)
    while tl_int > 1000:
        type_limit=input('Type limit (1000 max) \n')
        tl_int = int(type_limit)
        print(tl_int)

    return tl_int

while True:
    type_sort = input('Type sort (hot, new, controversial, top, rising) \n')
    while type_sort == '':
        type_sort = input('Type sort (hot, new, controversial, top, rising) \n')
    if type_sort == 'new':
        #set_limit()
        limit = set_limit()
        sorted =  subreddit_to_parse.new(limit=limit)
        break
    elif type_sort == 'controversial':
        limit = set_limit()
        sorted =  subreddit_to_parse.controversial(limit=limit)
        break
    elif type_sort == 'hot':
        limit = set_limit()
        sorted =  subreddit_to_parse.hot(limit=limit)
        break
    elif type_sort == 'top':
        limit = set_limit()
        sorted =  subreddit_to_parse.top(limit=limit)
        break
    elif type_sort == 'rising':
        limit = set_limit()
        sorted =  subreddit_to_parse.hot(limit=limit)
        break
    else:
        type_sort = input('Type sort (hot, new, controversial, top, rising) \n')

file_path = 'reddit-{sr}.csv'.format(sr=client_input)

with open(file_path, 'a') as file_to_write:

    fieldnames = ['title', 'url', 'author', 'ups','downs', 'comments', 'over 18', 'date']
    csv_writer = csv.DictWriter(file_to_write, fieldnames = fieldnames, delimiter = ',')
    csv_writer.writeheader()

    print('Saving the data...')
    for submission in sorted:
            if not submission.stickied:
                date = submission.created_utc
                formatted_date = datetime.datetime.fromtimestamp(int(date)).strftime('%Y-%m-%d %H:%M:%S')
                content = {
                    'title':submission.title,
                    'url':submission.url,
                    'author':submission.author,
                    'ups':submission.ups,
                    'downs':submission.downs,
                    'comments':submission.num_comments,
                    'over 18':submission.over_18,
                    'date':formatted_date
                    }
                csv_writer.writerow(content)
                time.sleep(2)
print('Data saved as {file_path}'.format(file_path = file_path))
