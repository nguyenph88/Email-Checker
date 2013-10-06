Email-Checker
=============

Check the validity of various kinds of email addresses, this piece of tool demonstrates on Yahoo Mail and Gmail.

Requirement:
- Python 3 (Python 2 has different method names)
- Better run on Windows (some codes interacts with windows objects)
- SSL on (othewise Gmail/Other mail check won't work)

Usage:
- pptx file was used for presentation.
- Run command: python check.py

Algorithm and Idea:
- Refer to the pptx file.
- Use DOM to send and receive response from a website, then determine the validity of the combination user/pass.
- Send a combination user/pass to a login form, submit it => recieve the response of the next web page, find the pattern and determine whether it's valid or not.

Options:
  --version       show program's version number and exit
  -h, --help      show this help message and exit
  -s, --single    Check single login validity. Ex: check.py -s asd@asd.com,asd
  -f, --filename  File contains email/password. Ex: check.py -f accounts.txt

Disclaimer:
- For education and testing purpose only.
- Email Providers keep changing their config and structure so sometimes the code doesn't work.
- This code is not cross-platform. Meant that it was made and tested with Python 3 on Windows only.
- That also means it doesn't work well with linux.

Note:
- I remove some code from the original tool as I think you should figure it out. Problems as following:
    + Cannot send many requests.
    + Cannot use the same IP to check many times.
    + Account may be locked after several tries.
    + Connection will be locked as using same config on header/agent.
    
Version:
1.0 - First pushed code.
1.1 - Fixed check yahoo after yahoo update their structure.
