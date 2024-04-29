import json
import os

def load_cache(cache_file):
    if os.path.exists(cache_file):
        with open(cache_file, "r") as f:
            return json.load(f)
    return {}

def save_cache(data, cache_file):
    with open(cache_file, "w") as f:
        json.dump(data, f)
