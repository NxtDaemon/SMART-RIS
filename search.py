import requests
import sys
import json
from bs4 import BeautifulSoup


class RIS():
    def __init__(self, image):
        self.ImageFilePath = image
        self.RunImageSearch()

    def RunImageSearch(self):
        Modules = ["GoogleRIS", ]  # "TinEyeRIS", "YandexRIS"]
        for Module in Modules:
            getattr(self, Module)()

    def GoogleRIS(self):
        ImageFilePath = self.ImageFilePath
        SearchURL = "http://www.google.com/searchbyimage/upload"
        MultiPart = {"encoded_image": (ImageFilePath, open(
            ImageFilePath, "rb")), "image_content": ""}
        Response = requests.post(
            SearchURL, files=MultiPart, allow_redirects=False)
        FetchURL = Response.headers["Location"]

        # Content = requests.get(FetchURL).content
        # soup = BeautifulSoup(Content, "html.parser")
        # print(soup.find("div", id="result-stats"))

        print(FetchURL)

    def TinEyeRIS(self):
        "Tineye's Own API makes manually doing such somewhat precarious, Futher Analysis will be needed"
        pass

    def YandexRIS(self):
        ImageFilePath = self.ImageFilePath
        SearchURL = 'https://yandex.com/images/search'
        Files = {'upfile': ('blob', open(ImageFilePath, 'rb'), 'image/jpeg')}
        Params = {'rpt': 'imageview', 'format': 'json',
                  'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
        Response = requests.post(SearchURL, params=Params, files=Files)
        QueryString = json.loads(Response.content)[
            'blocks'][0]['params']['url']
        FetchURL = SearchURL + '?' + QueryString

        # Content = requests.get(FetchURL).content
        # soup = BeautifulSoup(Content, "html.parser")
        # print(soup.find_all("div",_class=CbirSites-ItemTitle))

        print(FetchURL)


if __name__ == "__main__":
    R = RIS(sys.argv[1])
