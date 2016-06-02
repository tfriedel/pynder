import pynder
from datetime import timedelta, datetime
import random
from pickle import dump, load
from private import *
import time


def get_ping_time(user):
    time_format = '%Y-%m-%dT%H:%M:%S'
    return datetime.strptime(user.ping_time.split('.')[0], time_format)

def get_active_users(matches):
    active_matches = [m for m in matches if get_ping_time(m.user) > datetime.now() - timedelta(hours=1)]
    return active_matches

def get_user_named(matches, name):
    filtered_matches = [m for m in matches if str(m) == "u'{}'".format(name)]
    return filtered_matches[0]

def like_all(session, ids):
    counter = 0
    while session.likes_remaining > 0:
        users = session.nearby_users()
        for user in users:
            time.sleep(random.random() / 5.0)
            if not user.id in ids:
                like = user.like()
            else:
                like = user.dislike()
                print("user already matched:")
            counter += 1
            print(user.name)
    print ("liked {}".format(counter))

# this script swipes everyone right
session = pynder.Session(facebook_id=facebook_id, facebook_token=facebook_token)
matches = session.matches()

ids = [match.user.id for match in matches if match.user]
like_all(session, ids)