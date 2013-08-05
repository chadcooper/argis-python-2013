import BeautifulSoup as bs
import urllib2

url = "http://www.phillypal.com/pal_locations.php"

# Open the URL
response = urllib2.urlopen(url)
# Slurp all the HTML code into memory
html = response.read()
# Feed it into BS parser
soup = bs.BeautifulSoup(html)
# Find all the table cells whose width=37%
addresses = soup.findAll("td", {"width":"37%"})

print len(addresses)

print addresses

for address in addresses:
    # Print out just the text
    print address.find(text=True)