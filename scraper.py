import requests
from bs4 import BeautifulSoup


path_url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
page_req = requests.get(path_url)
soup = BeautifulSoup(page_req.content, 'html.parser')

def get_citations_needed_count(url_string):
    citation_needed_paragraph = soup.find_all('sup', class_="noprint Inline-Template Template-Fact")
    return len(citation_needed_paragraph)




def get_citations_needed_report(url_string):
    citation_needed_paragraph = soup.find_all('sup', class_="noprint Inline-Template Template-Fact")
    report = ""
    for paragraph in citation_needed_paragraph:
        passage = paragraph.find_parent('p')
        report+=f"Citation needed for: {passage.text}\n\n"
    return report

count = get_citations_needed_count(soup)
report = get_citations_needed_report(soup)
print(f"Number of citations needed: {count}")
print(f"Citations needed report:\n\n{report}")