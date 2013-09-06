>>> import urllib
>>> url = "http://www.fhwa.dot.gov/bridge/nbi/2012/delimited/DC12.txt"
>>> f = r"C:\Users\class5user\ar-gis-python\outputs\dc.csv"
>>> urllib.urlretrieve(url, f)