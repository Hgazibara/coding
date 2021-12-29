import sys
import re

text = sys.stdin.read()
questionp = re.compile(r'<a\s+href="/questions/(\d+)/[a-zA-Z0-9-]+"\s+class="question-hyperlink">([^<]+)</a>')
datep = re.compile(r'<span.*?class="relativetime">([^<]+)</span>')

questions = re.findall(questionp, text)
dates = re.findall(datep, text)

for question, date in zip(questions, dates):
    print(';'.join([question[0], question[1], date]))