Exploiting the interwebz
========================

The Python docs
---------------

Before we go any further, let's take a look at the Python docs for the version 
of Python ArcGIS 10.1 uses, 2.7.2:

http://docs.python.org/release/2.7.2/

Let's look at the ``os`` and ``urllib`` modules, which we will be using in this 
section.

Doing a simple file fetch from the web
--------------------------------------

.. literalinclude:: /embeds/simple-fetch.py

Fetching a bunch of files from a known URL structure
----------------------------------------------------

If files are sitting out on a server somewhere in a fairly rigid folder 
structure, it's relatively easy to fetch those files. The `Libre Map Project`_ 
hosts the 24K USGS DRGs for all 50 states for FREE on archive.org. We are 
interested in the `Arkansas DRGs`_.

On the Arkansas data page, hover over some of the links for the TIFF, TFW, and 
FGD files. See a pattern there?

``http://www.archive.org/download/usgs_drg_`` ``ar`` _ ``35`` ``094`` _ ``a2`` / 
``o`` ``35094`` ``a2`` ``.tif``

This breaks down to:

``base_url`` ``state`` _ ``deg lat`` ``deg lon`` _ ``map 
index no`` / ``category`` ``deg lat`` ``deg lon`` ``map index no`` ``.file ext``

.. note::

   This USGS standard explains the above nicely: 
   http://topomaps.usgs.gov/drg/drg_name.html
   
This quad information is available in the attributes of the 24K USGS quadrangle 
footprint that is readily available on the web. I got mine from the `USDA NRCS 
Data Gateway`_. Order by State | Arkansas | Map Indexes | Quadrangle Index 
1:24,000. You have this in the ``shapefiles`` directory as ``quads24k_a_ar.shp``. 
Load it into ArcMap and look at the attribute table. 

.. image:: /images/24k-att-table.png
   :width: 500px

Now open up 24K_Quads.xlsx from the ``inputs`` directory, in Excel. Let's build
our formula to in turn create our list of drgs to fetch.

.. rst-class:: html-toggle

Solution
++++++++

Look in Cell B16

Write the script to fetch DRGs
++++++++++++++++++++++++++++++

Import modules we will use:

.. literalinclude:: /embeds/fetch-drgs.py
   :lines: 1-2
      
Paste in your DRG list:

.. literalinclude:: /embeds/fetch-drgs.py
   :lines: 4-7
      
Create a list of extensions, these are the 3 filetypes we will fetch for each
quad:

.. literalinclude:: /embeds/fetch-drgs.py
   :lines: 9
      
Setup the ``base_url``:

.. literalinclude:: /embeds/fetch-drgs.py
   :lines: 10
      
Start a ``for`` loop to iterate through each nested list (each DRG) in 
``drg_list``:

.. literalinclude:: /embeds/fetch-drgs.py
   :lines: 12
      
Start *another* ``for`` loop *nested in the previous loop* to get all 3 
filetypes for each DRG (**note it is indented 4 spaces!**):

.. literalinclude:: /embeds/fetch-drgs.py
   :lines: 13
      
Let's play around with ``drg_list`` before we move on. Copy ``drg_list`` 
above and paste it into the ArcGIS Python window.

Type the following commands to get a feel for how lists and slicing work:

.. code-block:: python
   
   >>> for drg in drg_list:
           print drg
   >>> for drg in drg_list:
           print type(drg)
   >>> for drg in drg_list:
           for each in drg:
               print each
   >>> drg_list[0]
   >>> drg_list[2]
   >>> drg_list[0][1:6]
   >>> drg_list[0][6:]
   
Now let's build on list indexing and slicing and construct our url for 
fetching the data we want (**note that this and all following lines are 
indented 8 spaces!**). This takes parts of the quad info and builds the url 
for each DRG on the fly:

.. literalinclude:: /embeds/fetch-drgs.py
   :lines: 15-16

We need to have a local file and file path to store the fetched file in.

.. literalinclude:: /embeds/fetch-drgs.py
   :lines: 17-19
   
Call ``urllib.urlretrieve`` method and fetch the file:

.. literalinclude:: /embeds/fetch-drgs.py
   :lines: 20

``os.path`` goodness
####################

Let's figure out what all the ``os.whatever`` stuff was in the script we just 
wrote by deconstructing it.

In Windows Explorer, navigate to the ``source\code`` directory. Create a new file 
there call ``os-stuff.py``. Right-click on the file and select "Edit in IDLE".

Enter the following in ``os-stuff.py``:

.. literalinclude:: /embeds/os-stuff.py
   :lines: 1-2

Save the file. Leave it open in IDLE. Open up a Windows command prompt it you 
don't have one open already. Navigate to the ``source\code`` directory and enter:

.. code-block:: bash

   C:\Users\class5user\argis-python-2013\source\code>python os-stuff.py
   
On line 3, enter:

.. literalinclude:: /embeds/os-stuff.py
   :lines: 3
   
Save and run again.
   
One line 4, enter:

.. literalinclude:: /embeds/os-stuff.py
   :lines: 4
   
Save and run again.

On line 5, enter:

.. literalinclude:: /embeds/os-stuff.py
   :lines: 5
   
Save and run again.

One line 6-7 enter:

.. literalinclude:: /embeds/os-stuff.py
   :lines: 6-7
   
Save and run for the last time.




.. rst-class:: html-toggle

Solution
++++++++

.. literalinclude:: /embeds/fetch-drgs.py

Bonus
-----

Apply the principles of lists, iteration, and building of a url pattern we just 
learned to the first example of the NBI bridge data. Is there a way to fetch 
multiple states by using a list somehow? 

.. note:: 

   Use small states like RI, DE, and the District of Columbia, that way the 
   files you fetch are smaller.
   
.. rst-class:: html-toggle

Solution
++++++++

.. literalinclude:: /embeds/multi-fetch.py






      
      
      
      
      
      
      
      
      
      



   
   
.. _PhillyPals: http://www.phillypal.com/pal_locations.php
.. _Libre Map Project: http://libremap.org/
.. _Arkansas DRGs: http://libremap.org/data/state/arkansas/drg/
.. _USDA NRCS Data Gateway: http://datagateway.nrcs.usda.gov/GDGOrder.aspx