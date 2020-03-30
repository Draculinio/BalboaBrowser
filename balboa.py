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
        self.link_number = 0
        init()

    def handle_starttag(self, tag, attrs):

        self.print_data = True
        self.print_end_tag = True
        if tag == 'a':
            # self.parsed_page += '[' + f"{self.link_number}" + ']' + Fore.BLUE
            self.parsed_page += "[{}]".format(self.link_number) + Fore.BLUE
            self.link_number = self.link_number + 1
        elif tag == 'input':
            self.parsed_page += Fore.GREEN
            self.parsed_page += '______________________________________'
        elif tag == 'p':
            self.parsed_page += Fore.WHITE

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
        my_request = DoRequests()
        while self.url != 'q':
            self.url = input("URL> ")
            if self.url[0:11] != "http://www.":
                if self.url[-4] == ".":
                    self.url = "http://www." + self.url
                else:
                    self.url = 'https://www.bing.com/search?q=' + self.url

            if my_request.get_status(self.url) == 200:
                my_parser = Parser()
                self.content = my_request.get_content(self.url)
                my_parser.feed(self.content)
                print(my_parser.parsed_page)
            else:
                print('NOT FOUND')
                print(self.url)
                print(my_request.get_status(self.url))


if __name__ == '__main__':
    my_browser = Browser()
    my_browser.navigate()