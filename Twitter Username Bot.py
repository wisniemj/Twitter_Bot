import twitter
from tkinter import *
import csv
import os

default_directory = os.getcwd()

# Input box module
master = Tk()
e = Entry(master)
e.pack()
e.focus_set()

def callback():
    twitter_handle = e.get()  # This is the text you may want to use later
    # Connect the input from input box with API call
    api = twitter.Api(consumer_key='GpkcTo23SJqpEjg1KUrsPioQo',
                      consumer_secret='u2txNaI9FDGsfqe2VWOxkyBOoTdBZOtNkiWtBrXoM78eEqeNSk',
                      access_token_key='1526716592-vE7YJkdVU5qav5hSkIX2zUBEuaRnOvr97xVHz7L',
                      access_token_secret='jx5ihyIGrGKF40BD9Tc3IK6kNOF7dZoZOgemvqRykdbEK'
                      )
    # t is getting the meta data from the Twitter API
    t = api.GetUserTimeline(screen_name=twitter_handle, count=5)

    # tweets is assigning the meta data to a dictionary
    tweets = [i.AsDict() for i in t]

    # Read in meta data
    for t in tweets:
        # Create output that is in a readable format for .csv
        output = [[t['text'], t['created_at'], len(t['text'].split())] for t in tweets]

        # write the csv
        with open('%s_tweets.csv' % twitter_handle, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["Tweet", "Datetime", "English Words"])
            writer.writerows(output)

# Button layout
b = Button(master, text="OK", width=30, command=callback)
b.pack()

mainloop()