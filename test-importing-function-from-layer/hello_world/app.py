from say_hello import say_hello
# import requests


def lambda_handler(event, context):
    return say_hello()
