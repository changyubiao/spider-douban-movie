import urllib.request
import chardet

class HtmlDownloader(object):
    @staticmethod
    def download(new_url):
        if new_url is None:
            return None
        response = urllib.request.urlopen(new_url)

        if response.getcode() != 200:
            return None
        return response.read()
