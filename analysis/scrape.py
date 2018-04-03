from requests import get
from requests.exceptions import RequestException
from contextlib import closing 
from bs4 import BeautifulSoup



def simple_get(url):
    """
    Attempts to get the content at url by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns true if the response seems to be HTML, false otherwise
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def getAnswerChoices(queryString):
    query = queryString
    raw_html = simple_get("https://www.google.com/search?q="+query+"&cad=h")

    raw_html = raw_html[raw_html.find("People also search for".encode()):]

    html = BeautifulSoup(raw_html, 'html.parser')
    # print("\n\n\n\n")
    # print(html)
    mydivs = html.find_all("a", class_="fl")
    # otherD = html.find_all("div", class_="czonVc")

    choices = []


    for i in range(len(mydivs)):
        if i >= 3: 
            break
        if "..." not in mydivs[i].text:
            choices.append(str(mydivs[i].text))
            # print(str(mydivs[i].text))

    return choices

getAnswerChoices('Special Relativity')