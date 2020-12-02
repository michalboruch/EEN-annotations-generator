#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Generate EEN annotations."""

import time

from api import API
from annotation import get_annotation_data
from resources import banner
from user_input import UserInput


def gather_startup_data():
    global api, camera_esn, namespace

    print(banner)

    username, password = UserInput.get_login_data()

    print("Authenticating & Authorizing the User...")
    api = API(username, password)

    camera_esn, namespace = UserInput.get_camera_data()


if __name__ == "__main__":
    gather_startup_data()

    # Start creating annotations
    while True:
        print(f"{'-----' * 16}")
        print("iterating:")

        annotation_data = get_annotation_data()
        api.create_annotation(annotation_data, camera_esn, namespace)

        status_code = api.create_annotation(annotation_data, camera_esn, namespace)
        if status_code == 200:
            print("Created annotation, sleeping for 10s.")
            time.sleep(10)
        else:
            print("Creation of the annotation failed, sleeping for 5s.")
            time.sleep(5)
