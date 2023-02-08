import re


def validate_email(email):
    pattern = re.compile(r"^\S+@((bmstu\.ru)|(student\.bmstu\.ru))$")
    return True if pattern.match(email) is not None else False
