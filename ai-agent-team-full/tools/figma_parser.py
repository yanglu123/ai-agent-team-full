import json

def parse_figma(path):
    with open(path, 'r') as f:
        return json.load(f)
