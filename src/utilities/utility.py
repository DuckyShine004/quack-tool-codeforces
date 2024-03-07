import requests
import bs4


class Utility:
    @staticmethod
    def get_samples(url):
        samples = []
        request = requests.get(url)
        url_data = bs4.BeautifulSoup(request.text, "html.parser")
        target_div = url_data.find_all(class_="input")

        for div in target_div:
            tag = div.find("pre")
            samples.append(tag.text.strip())

        return samples

    @staticmethod
    def get_tests(samples):
        tests = []

        for sample in samples:
            test = []

            for sample_input in sample.split("\n"):
                test.append(sample_input)

            tests.append(test)

        return tests
