import os
import json
import appdirs

from quacktools.constants.extension_constants import APPLICATION_NAME, CACHE_FILE_NAME


class Cache:
    def __init__(self):
        self.cache_directory = ""
        self.cache_file_path = ""

        self.create_cache_directory()

        self.cache = self.get_cache()

    def create_cache_directory(self):
        self.cache_directory = appdirs.user_cache_dir(APPLICATION_NAME)
        self.cache_file_path = self.cache_directory + CACHE_FILE_NAME

        os.makedirs(self.cache_directory, exist_ok=True)

        if not os.path.exists(self.cache_file_path):
            with open(self.cache_file_path, "w", encoding="utf-8") as cache_file:
                json.dump({}, cache_file, indent=4)

    def check_samples_cached(self, cache_key):
        return cache_key in self.cache

    def set_samples(self, key, value):
        self.cache[key] = value

        with open(self.cache_file_path, "w", encoding="utf-8") as cache_file:
            json.dump(self.cache, cache_file, indent=4)

    def get_cache(self):
        with open(self.cache_file_path, "r", encoding="utf-8") as cache_file:
            return json.load(cache_file)

    def get_samples(self, key):
        return self.cache[key]
