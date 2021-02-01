# Copyright (c) 2021 0x30c4

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from requests import get
from json import loads, load
from random import randint, choice
from string import ascii_lowercase
from platform import system

with open('api_keys.json') as key:
    key = load(key)

header = {
	"Authorization": key["Authorization_unsplash"]
}


def getImg(q):
    err = ''
    try:
        url = "https://api.unsplash.com/search/photos?query={}&page=1&client_id=GX6Ucpa3-J2XlDUQtgPYFWhy9Xqon4PsM9GcySBBkuY".format(q)

        get_json = get(url).text
        get_json = loads(get_json)

        img_urls = []
        for n, r in enumerate(get_json['results']):
            img_urls.append(r['urls']['small'])
            if n == 4: break
        
        path_sep = '/'
        if system() == 'Windows':
            path_sep = "\\"

        img_names = []
        for img_url in img_urls:
            r = get(img_url)
            get_ext = 'jpg'
            img_name = r'img{}tmp{}{}.{}'.format(path_sep, randint(0, 4096), "".join([choice(ascii_lowercase) for _ in range(16)]), get_ext)
            open(img_name, 'wb').write(r.content)
            img_names.append(img_name)
        
        return img_names

    except:
        err = '404'
    
    return err
if __name__ == '__main__':
    print(getImg("shit"))