import re
import requests


def get_last_publications_medium():
    url = 'https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@samuelsan95'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['items']
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []


def get_publication_image(publication):
    if publication and 'description' in publication and isinstance(publication['description'], str):
        description = publication['description']
        regex = r'src="([^"]*)"'
        match = re.search(regex, description)
        
        if match:
            return match.group(1)  
    return "icons/medium.svg"


def get_publication_description(publication):
    if publication and 'description' in publication and isinstance(publication['description'], str):
        description = publication['description']
        regex = r'<p>([^"]*)</p>'
        match = re.search(regex, description)
        
        if match:
            return remove_html_code(match.group(1))
    return ""


def remove_html_code(text_code):
    regex = re.compile(r'<[^>]+>')

    return regex.sub('', text_code)
