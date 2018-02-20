#!/usr/bin/env python
# -*- coding: utf-8 -*-

# make a list of the bot's friends (whitelist)

import os, configparser, tweepy, inspect, pickle, time

path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

config = "configtest"
#config = "configprod"

configfile = os.path.join(path, config)

# read config
config = configparser.SafeConfigParser()
config.read(configfile)

whitelist = config.get("settings", "white_list_file")
file = os.path.join(path, whitelist)

slug = config.get("settings", "white_list_slug")

bot_id = config.get("settings", "bot_id")

# your hashtag or search query and tweet language (empty = all languages)
tweetLanguage = config.get("settings", "tweet_language")

# create bot
auth = tweepy.OAuthHandler(config.get("twitter", "consumer_key"), config.get("twitter", "consumer_secret"))
auth.set_access_token(config.get("twitter", "access_token"), config.get("twitter", "access_token_secret"))
api = tweepy.API(auth, wait_on_rate_limit=True)

docs = [ ]

# In this example, the handler is time.sleep(15 * 60),
# but you can of course handle it in any way you want.

members = tweepy.Cursor(api.list_members, owner_id=bot_id, slug=slug).items()
ids = [user.id for user in members]

for id in ids:
    docs.append(id)

with open(file, mode='wt') as f:
    for id in ids:
            f.write(str(id) + '\n')
