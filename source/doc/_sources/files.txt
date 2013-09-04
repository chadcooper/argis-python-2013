Working with files
==================

Scraping a file for email addresses
-----------------------------------

I'm lazy. It's true, I admit it. So when someone sends a file with a bunch of 
email addresses in it that I need to get out, I turn to Python. Sure, you can 
copy and paste, but so can my 6th grader. I'd rather invest that copy/paste 
time into something a little bit more interesting.

1. Open up the file ``/inputs/workshops.docx.txt`` in Notepad. Scoll around 
   til you see some of the email addresses that are scattered about in the 
   document. This was a Word document, I opened it in Google Drive, then saved it 
   out to text, which took about 15 seconds.

2. Open up a Command Prompt: Start > Search box > type ``cmd``

3. Change directories ("cd") to the ``inputs`` directory.

4. Fire up the Python interpreter

5. Use the ``re`` module in the Python standard library, so type:

   .. literalinclude:: /code/scrape-email-addresses.py
      :lines: 1
      
6. Now we need to build up the pattern, the regular expression, to find any 
   email addresses in the text string:
   
   .. literalinclude:: /code/scrape-email-addresses.py
      :lines: 2
      
7. Open up the text file and read it all into memory:

   .. literalinclude:: /code/scrape-email-addresses.py
      :lines: 3
      
8. Execute the pattern search on the in-memory text of the file:

   .. literalinclude:: /code/scrape-email-addresses.py
      :lines: 4
      
9. Print out the emails and the count of how many were found:

   .. literalinclude:: /code/scrape-email-addresses.py
      :lines: 5-6
      
Writing the email addresses out to a text file
++++++++++++++++++++++++++++++++++++++++++++++

We have the email addresses out of the file and into a list object. We can 
copy/paste that list, but they are strings and have those damned pesky single 
quotes around them. Gmail might not dig that. Let's write them out to a file so 
we can have em for later if we need em:

1. Open up a writable object, a text file in our ``outputs`` directory:

   .. literalinclude:: /code/scrape-email-addresses.py
      :lines: 7
      
2. What type of objects are we dealing with?

   .. literalinclude:: /code/scrape-email-addresses.py
      :lines: 8-9
      
3. Iterate through the list of email addresses, write each one out to file, 
   separated by a comma and a space:
   
   .. literalinclude:: /code/scrape-email-addresses.py
      :lines: 10-12
      
4. Close the text file:

   .. literalinclude:: /code/scrape-email-addresses.py
      :lines: 13
