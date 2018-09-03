from __future__ import absolute_import, unicode_literals

import json
from base64 import b64encode

from celery import task

import requests


def get_credentials():
    """
    Get user grendentials from file to make the request in an API.
    """
    with open('.loader_credentials.json', 'r') as f:
        file_data = json.loads(f.read())

    username = file_data['username']
    password = file_data['password']

    utf_8_authorization = "{username}:{password}".format(
        username=username, password=password
    ).encode()

    return "Basic " + b64encode(utf_8_authorization).decode("ascii")


@task()
def get_parliamentarians():
    """
    Get the data of the parliamentarians from a private api.
    """
    url = "http://loader:3500/"
    request_body = "{\n\"task\": \"get_parliamentarians\"\n}"

    requests.post(
        url=url,
        data=request_body,
        headers={
            "content-type": "application/json",
            "Authorization": get_credentials()
        }
    )


@task()
def get_propositions():
    """
    Get the data of the proposals of the parliamentarians of a private api.
    """
    url = "http://loader:3500/"
    request_body = "{\n\"task\": \"get_propositions\"\n}"

    requests.post(
        url=url,
        data=request_body,
        headers={
            "content-type": "application/json",
            "Authorization": get_credentials()
        }
    )
