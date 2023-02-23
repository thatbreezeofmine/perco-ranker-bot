import json


def get_users_data():
    with open("data/users.json", "r") as f:
        data = json.load(f)
    return data


def get_guildes_data():
    with open("data/guildes.json", "r") as f:
        data = json.load(f)
    return data

