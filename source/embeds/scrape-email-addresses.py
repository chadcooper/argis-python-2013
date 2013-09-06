>>> import re
>>> email_pattern = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+")
>>> all_text = open("workshops.docx.txt").read()
>>> emails = re.findall(email_pattern, all_text)
>>> emails
>>> len(emails)
>>> f = open("outputs/scraped_emails.txt", "w")
>>> type(f)
>>> type(all_text)
>>> for email in emails:
...     f.write(email + ", ")
...
>>> f.close()