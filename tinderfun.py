import pynder
from datetime import timedelta, datetime
from private import *
session = pynder.Session(facebook_id=facebook_id, facebook_token=facebook_token)


def get_ping_time(user):
    time_format = '%Y-%m-%dT%H:%M:%S'
    return datetime.strptime(user.ping_time.split('.')[0], time_format)

def get_active_users(matches):
    active_matches = [m for m in matches if get_ping_time(m.user) > datetime.now() - timedelta(hours=1)]
    return active_matches

def get_user_named(matches, name):
    filtered_matches = [m for m in matches if str(m) == "u'{}'".format(name)]
    return filtered_matches[0]
