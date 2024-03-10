import requests

from bs4 import BeautifulSoup
from collections import defaultdict


class Utility:
    @staticmethod
    def get_samples(url):
        samples = defaultdict(list)

        request = requests.get(url)
        url_data = BeautifulSoup(request.text, "html.parser")
        input_divs = url_data.find_all(class_="input")
        output_divs = url_data.find_all(class_="output")

        for input_div in input_divs:
            tag = input_div.find("pre")
            samples["input"].append(tag.text.strip())

        for output_div in output_divs:
            tag = output_div.find("pre")
            samples["output"].append(tag.text.strip())

        return samples
