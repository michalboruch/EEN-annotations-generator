# -*- coding: utf-8 -*-

"""Annotations."""

import json
import random
import string

from resources import labels, texts


def get_box_dimensions():
    x_axis = get_random_floats()
    y_axis = get_random_floats()

    top = y_axis[0]
    height = y_axis[1]
    left = x_axis[0]
    width = x_axis[1]

    return [[top, left], [height, width]]


def get_random_label():
    return random.choice(labels)


def get_random_thickness():
    return random.choice(["thin", "normal", "thick"])


def get_random_color(chars="ABCDEF" + string.digits):
    return "#" + "".join(random.choice(chars) for _ in range(6))


def get_random_floats(start=0, stop=1):
    return sorted([random.uniform(start, stop), random.uniform(start, stop)])

def get_random_text():
    return random.choice(texts)

def get_annotation_data():
    return json.dumps(
        {
            "_s": {
                "b": get_box_dimensions(),
                "d": "",
                "l": get_random_label(),
                "lt": get_random_thickness(),
                "sc": get_random_color(),
                "t": get_random_text(),
                "tt": "tool tip",
                "tw": "43",
                "u": "https://google.com",
            }
        }
    )
