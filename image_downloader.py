import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse

def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_images(url):
    soup = bs(requests.get(url).content, 'html.parser')

    # find images in html content
    urls = []
    for img in tqdm(soup.find_all("img"), "Extracting images"):
        img_url = img.attrs.get('src')
        if not img_url:
            continue

        img_url = urljoin(url, img_url)

        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass

        if is_valid(img_url):
            urls.append(img_url)
    return urls

# Download the file for the url
def download(url, pathname):
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # Download body of response by chunks
    response = requests.get(url, stream=True)
    # Get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    # retreive file name
    filename = os.path.join(pathname, url.split("/")[-1])

    progress = tqdm(response.iter._content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress:
            f.write(data)
            progress.update(len(data))