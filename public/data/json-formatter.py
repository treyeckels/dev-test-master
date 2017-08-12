import json
from datetime import datetime
from bs4 import BeautifulSoup

# Reading data back
with open('articles.json', 'r') as f:
     data = json.load(f)
     for i, content in enumerate(d['post_content'] for d in data):
         soup = BeautifulSoup(content)
         # kill all unwanted DOM elements
         for tags in soup(["img", "h1", "h2", "h3"]):
             tags.extract()  # rip it out
         parsedContent = soup.get_text()
         parsedContent = parsedContent.replace('\n','')
         parsedContent = parsedContent.replace('\r','')
         data[i]['post_teaser'] = parsedContent
         python_date = datetime.strptime(data[i]['post_date'],'%Y-%m-%dT%H:%M:%S.%fZ')
         data[i]['post_date'] = python_date.strftime('%B %d, %Y')
     with open('articles-formatted.json', 'w') as outfile:
         json.dump(data, outfile, indent=4)
