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
from json import loads
from random import randint, choice
from string import ascii_lowercase



api_key = "563492ad6f917000010000019ece9e82749440728a8674141ad5f7ad"

header = {
    "Authorization": api_key
}

def getImg(q):
    img_name = ''
    try:
        url = "https://api.pexels.com/v1/search?query={}&per_page=1".format(q)

        get_json = get(url, headers=header).text

        get_json = loads(get_json)
        img_url = get_json["photos"][0]['src']['medium']
        get_ext = get_json["photos"][0]['src']['original'].split('.')[-1]
        
        r = get(img_url)

        img_name = r'img\tmp{}{}.{}'.format(randint(0, 4096), "".join([choice(ascii_lowercase) for _ in range(16)]), get_ext)
        
        open(img_name, 'wb').write(r.content)

    except:
        img_name = '404'

    return img_name

if __name__ == '__main__':
    print(getImg("dog"))