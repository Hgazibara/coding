import sys
import re
import html.parser

class MyHTMLParser(html.parser.HTMLParser):

	tags = set()
	def handle_starttag(self, tag, attrs): self.tags.add(tag)

all_lines = [x.replace('\n', '') for x in sys.stdin][1:]

parser = MyHTMLParser()
parser.feed("".join(all_lines))

print(";".join(sorted(MyHTMLParser.tags)))