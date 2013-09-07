import urllib
import os

base_url = "http://www.fhwa.dot.gov/bridge/nbi/2012/delimited/"
states = ["RI", "DE", "NV"]

for state in states:
    url = base_url + state + "12.txt"
    local_file = os.path.join(os.path.dirname(os.path.split(os.path.abspath(__file__))[0]),
                                  "outputs", state + "12.txt")
    urllib.urlretrieve(url, local_file)