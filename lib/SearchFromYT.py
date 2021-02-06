from requests import get
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL

URL = "https://www.google.com/search?client=firefox-b-d&q="

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://google.com",
    "DNT": "1"
}


YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}

def search(arg):
    try:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            try:
                get(arg) 
            except:
                video = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
            else:
                video = ydl.extract_info(arg, download=False)

            return ["yout" + video['id'], video['title']]
    except:
        return False

def getPage(query):
    query = query.replace(' ', "+")
    url = URL + query
    try:
        page = get(url, headers=header).content
        print(page.decode('windows-1252'))
        soup = BeautifulSoup(page, 'html.parser')
        for link in soup.find_all('a'):
            print(link.get('href'))
    except Exception as e:
        return [str(e), False]

if __name__ == "__main__":
    # print(getPage('tomar jonno by arnob'))
    print(search('tomar jonno by arnob'))