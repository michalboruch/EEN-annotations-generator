# -*- coding: utf-8 -*-
"""Helpers."""


import getpass


class UserInput:
    @staticmethod
    def get_login_data():
        print("Please provide credentials for EEN superuser or user from device account.")
        username = input("username: ")
        password = getpass.getpass("password:")
        return username, password

    @staticmethod
    def get_camera_data():
        camera_esn = input("Provide camera esn: ") or "10094619"
        namespace = int(input("Provide namespace (default: 102): ") or 102)
        return camera_esn, namespace
