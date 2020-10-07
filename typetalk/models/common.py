from datetime import datetime


def fromisoformat(date_string):
    # remove 'Z' suffixj
    return datetime.fromisoformat(date_string[:-1])
