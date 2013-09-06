import urllib
import os

drg_list = [['o36094a2', 'Fayetteville', 'AR'],
            ['o36094b1', 'Sonora', 'AR'],
            ['o36094a1', 'Elkins', 'AR'],
            ['o36094b2', 'Springdale', 'AR']]
             
exts = ['tif', 'tfw', 'fgd']
base_url= "http://www.archive.org/download/usgs_drg_"

for drg in drg_list:
    for ext in exts:
        # http://www.archive.org/download/usgs_drg_ar_35094_d2/o35094d2.tif
        full_url = (base_url + drg[2].lower() + '_' + drg[0][1:6] +
                    '_' + drg[0][6:] + "/" + drg[0] + '.' + ext)
        local_file = os.path.join(os.path.dirname(os.path.split(os.path.abspath(__file__))[0]),
                                  "outputs", drg[0] + '.' + ext)
        print local_file
        urllib.urlretrieve(full_url, local_file)
