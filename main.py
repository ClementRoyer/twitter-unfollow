#!/usr/bin/env python3

import twitter
import os

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
pseudo=''

file='.followers'

def init():
    return twitter.Api(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token_key=access_token,
        access_token_secret=access_token_secret
    )

def getUserId(username):
    return api.GetUser(screen_name=username).id

def sendDirectMessage(text):
    msg = 'Bot update\nNew unfollow : @'
    api.PostDirectMessage(text=msg + text, user_id=user_id)

def getFollowers():
    return [user.screen_name for user in api.GetFollowers(user_id=user_id)]

def getOldFollowers():
    if not os.path.exists(file):
        return []
    f = open(file, 'r')
    content = f.read()
    content = content.split(',')
    f.close()
    return content

def compare(old, new):
    unfollow = []
    new_follow = []

    if (len(old) == 0):
        return '', new

    for user in old:
        if not (user in new):
            unfollow.append(user)

    for user in new:
        if not (user in old):
            new_follow.append(user)
    return unfollow, new_follow

def save(content):
    f = open(file, 'w+')
    f.write(content)
    f.close()

def run():
    global user_id
    user_id = getUserId(pseudo)
    old_followers = getOldFollowers()
    followers = getFollowers()
    unfollow, new_follow = compare(old_followers, followers)
    if (len(unfollow) != 0):
        sendDirectMessage(',@'.join(unfollow))
    if (len(new_follow) != 0 or len(unfollow) != 0):
        save(','.join(followers))

def exit():
    print('\n🤖 Bye')
    os._exit(0)

if __name__ == '__main__':
    try:
        api = init()
        # api.CreateFriendship(screen_name=pseudo)
        run()

    except KeyboardInterrupt:
        exit()
    except SystemExit:
        exit()