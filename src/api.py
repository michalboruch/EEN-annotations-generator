# -*- coding: utf-8 -*-

"""EEN API."""

import json
import requests
import sys


class API:
    """Authenticate & Authorize API."""

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.token = self.authenticate()
        self.auth_key = self.authorization()

    def authenticate(self):
        """
        Authenticate the User.

        Docs: https://apidocs.eagleeyenetworks.com/#1-authenticate
        """
        r = requests.post(
            "https://login.eagleeyenetworks.com/g/aaa/authenticate",
            data={"username": self.username, "password": self.password},
        )
        if r.status_code != 200:
            sys.exit("Authentication failed.")
        return r.json()["token"]

    def authorization(self):
        """
        Authorize the User.

        Docs: https://apidocs.eagleeyenetworks.com/#3-authorize
        """
        r = requests.post(
            "https://login.eagleeyenetworks.com/g/aaa/authorize",
            data={"token": self.token},
        )
        if r.status_code != 200:
            sys.exit("Authorization failed.")
        return r.cookies["auth_key"]

    def create_annotation(self, data, camera_esn, namespace):
        """
        Create Annotation.

        Docs: https://apidocs.eagleeyenetworks.com/#create-annotation
        """
        r = requests.put(
            f"https://login.eagleeyenetworks.com/annt/set?c={camera_esn}&ns={namespace}&A={self.auth_key}",
            data=data,
        )
        return r.status_code
