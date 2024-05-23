#!/usr/bin/env python

import json

def read_game_input_json(file_name):
    json_data = open(file_name)
    data = json.load(json_data)
    return data