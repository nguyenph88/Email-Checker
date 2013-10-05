#!/usr/bin/env python

import urllib

from optparse import OptionParser


def get_options():
    usage = '%prog [options] filename\n       filename: file contains text \
will be pasted on pastebin'
    version = '%prog 0x01'
    parser = OptionParser(usage=usage, version=version)
    parser.add_option('-n', '--name', action='store', type='string', 
                      dest='name', help='title or name of your paste. \
Default: None', default=None, metavar='NAME')
    parser.add_option('-m', '--mail', action='store', type='string', 
                      dest='email', help='email for sending result link to. \
Default: None', default=None, metavar='MAIL')
    parser.add_option('-d', '--domain', action='store', type='string', 
                      dest='domain', help='domain name for using as subdomain \
in paste link. Default: None', default=None, metavar='DOMAIN')
    parser.add_option('-p', '--private', action='store_true', dest='private', 
                      help='if this option is specified, make your paste \
private. If not, it will be public.', default=False)
    parser.add_option('-e', '--expire', action='store', type='string',
                      dest='expire', help='adding expiration date. \
N for never, 10M for 10 minutes, 1H for 1 hour, 1D for 1 day, 1M for 1 month. \
Default: N', default='N', metavar='TIME')
    parser.add_option('-f', '--format', action='store', type='string', 
                      dest='format_', help='for adding syntax highlighing. \
Some common formats: python, asm, c, cpp, apache, css, fortran, html4strict, \
java, perl, php, ruby, bash, ... Visit http://pastebin.com to \
see complete list. Default: python', default='python', metavar='FORMAT')
    return parser

    
def create_data(code, name=None, email=None, domain=None, 
                        private=False, expire='N', format_='python'):    
    # Prepare all data for the post request
    data = {}
    # Code is required
    data['paste_code'] = code
    # Default options
    data['paste_expire_date'] = expire
    data['paste_format'] = format_
    if private == True:
        data['paste_private'] = 1
    else:
        data['paste_private'] = 0
    # All others are optional
    if name:
        data['paste_name'] = name
    if email:
        data['paste_email'] = email
    if domain:
        data['paste_subdomain'] = domain
    return data


def make_request(url, data):
    # Encode the data
    post_data = urllib.urlencode(data)
    # Make request and get the response
    request = urllib2.Request(url, post_data)
    response = urllib2.urlopen(request)
    # The response will contain the pastebin link
    paste_link = response.read()
    return paste_link


def main():
    # Get options and arguments list
    parser = get_options()
    options, args = parser.parse_args()
    # Check if the expire time is valid
    if options.expire != 'N' and options.expire != '10M' and \
        options.expire != '1H' and options.expire != '1D' and \
        options.expire != '1M':
        parser.print_help()
        print('Error: expire time invalid.')
        exit(1)
    # Check if no filename is specified
    if len(args) <= 0:
        parser.print_help()
        print('Error: please specify filename.')
        exit(1)
    # Read text from file
    filename = args[0]
    try:
        f = open(filename, 'r')
    except:
        print('Error: cannot open file %s' % filename)
        exit(1)
    text = f.read()
    f.close()
    # Create data for post message
    data = create_data(text, options.name, options.email, options.domain, 
                           options.private, options.expire, options.format_)
    # Make a request to http://pastebin.com and get a paste link or error
    url = 'http://pastebin.com/api_public.php'
    link = make_request(url, data)
    print(link)
    
        
if __name__ == '__main__':
    main()
