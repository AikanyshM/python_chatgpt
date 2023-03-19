

# import necessary libraries
import requests
from bs4 import BeautifulSoup
import googletrans
 


# create a web page request
url = 'https://www.techworld-with-nana.com/post/a-guide-of-how-to-get-started-in-it-in-2023-top-it-career-paths'
page = requests.get(url)

# parse the response
soup = BeautifulSoup(page.content, 'html.parser')

# Get all the header elements
headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

# Translate each header to Russian
translator = googletrans.Translator()
russian_headers = []
for header in headers:
    translated_header = {
        "text": translator.translate(header.text, dest='ru').text,
        "name": header.name
    }
    
    russian_headers.append(translated_header)

# create an HTML file
with open('russian_headers.html', 'w') as f:
    # write the opening tag of the file
    f.write('<html>\n')
    for header in russian_headers:
        f.write(f'<{header["name"]}>{header["text"]}</{header["name"]}>\n')
    f.write('</html>\n')