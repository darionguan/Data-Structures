# CS3C Advanced Algorithms and Data Structures Using Python
# Lab #3 - Practical Problems Using Trees
# Application: WWW List Collector
# Description: This application converts each batch of ordered or unordered
#              lists from an HTML file into a Python list and then outputs
#              them in the order encountered as a list of lists.
# File Dependencies: N/A
# Development Environment: PyCharm 2022.3.1
# Version: Python 3.9
# Solution File: DarionGuanLab3.py
# Date: 2/28/23

from html.parser import HTMLParser


class ListCollector(HTMLParser):
    def __init__(self):
        super(ListCollector, self).__init__()
        self.lst = []
        self.final_lst = []

# Modified HTMLParser methods
    def handle_starttag(self, tag, attrs):
        self.lst.append('<' + tag)

    def handle_endtag(self, tag):
        self.lst.append('</' + tag)

    def handle_data(self, data):
        self.lst.append(data)

    # Helper function to create lists
    def create_lists(self):
        for i in range(len(self.lst)):
            if self.lst[i] == '<ul':
                current = []
                j = i + 1
                while self.lst[j] != '</ul':
                    if self.lst[j].startswith('<') is False:
                        current.append(self.lst[j])
                    j += 1
                self.final_lst.append(['ul', current])

            if self.lst[i] == '<ol':
                current = []
                j = i + 1
                while self.lst[j] != '</ol':
                    if self.lst[j].startswith('<') is False:
                        current.append(self.lst[j])
                    j += 1
                self.final_lst.append(['ol', current])

    def getLists(self):
        self.create_lists()
        new = []
        for i in self.final_lst:
            new.append(i[1])
        return new
