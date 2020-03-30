import requests
from html.parser import HTMLParser
from colorama import init, Fore, Back, Style


class DoRequests:
    # tirar el codigo de la request
    def __init__(self):
        self.url = 'http://www.dracux.com'

    def get_status(self, url):
        self.url = url
        return requests.get(self.url).status_code

    def get_content(self, url):
        self.url = url
        return requests.get(self.url).text


class Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.print_data = False
        self.print_end_tag = False
        self.parsed_page = ''

    def handle_starttag(self, tag, attrs):
        self.print_data = True
        self.print_end_tag = True
        if tag == 'a':
            self.parsed_page += Fore.BLUE
        elif tag == 'input':
            self.parsed_page += Fore.GREEN
            self.parsed_page += '______________________________________'

    def handle_endtag(self, tag):
        if self.print_end_tag:
            self.parsed_page += '\n'
        self.print_end_tag = False

    def handle_data(self, data):
        if self.print_data:
            self.parsed_page += data
        self.print_data = False


class Browser:
    def __init__(self):
        self.url = ''
        self.content = ''

    def navigate(self):
        self.url = input("URL> ")
        my_request = DoRequests()
        if my_request.get_status(self.url) == 200:
            my_parser = Parser()
            self.content = my_request.get_content(self.url)
            my_parser.feed(self.content)
            print(my_parser.parsed_page)


if __name__ == '__main__':
    my_browser = Browser()
    my_browser.navigate()