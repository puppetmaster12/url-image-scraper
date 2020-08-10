# url-image-scraper
<h4>Check validity of url</h4>
<pre>
  def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)
</pre>
<p>The above function checks the validity of the supplied url.</p>
<br>
<h4>Get all image urls</h4>
<pre>
  def get_all_images(url)
 </pre>
 <p>The get all images function gets the urls associated with each image in the page from the src attribute of the img tag</p>
 <br>
 <h4>Download images</h4>
 <pre>
  def download(url, path)
 </pre>
 <p>The download function downloads each image</p>
 <br>
 <h4>Dependencies</h4>
 <ul>
  <li>
    <a href="https://www.python.org/download/releases/3.0/">Python 3</a>
  </li>
  <li>
    <a href="https://requests.readthedocs.io/en/master/">Requests</a>
  </li>
  <li>
    <a href="https://pypi.org/project/beautifulsoup4/">Beautiful Soup</a>
  </li>
  <li>
    <a href="https://tqdm.github.io/">Tqdm</a>
  </li>
 </ul>
 <h4>Usage</h4>
 <p>Simply pass in the url and the directory to which to download the images to the main function</p>
 <pre>
  main(url, directory)
 </pre>
 
