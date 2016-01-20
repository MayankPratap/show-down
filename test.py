from showDown import showDown
import argparse

user = showDown()

parser = argparse.ArgumentParser(description='A Command line tool to download your favorie TV Shows')
parser.add_argument('-dl','--downloadlatest', help='Download the latest episode of your favorite TV Show', required=False)
parser.add_argument('-p','--proxy', help='Set the proxy', required=False)
parser.add_argument('-u','--unsetproxy', help='Unset the proxy', action='store_true')

args = vars(parser.parse_args())

if args['proxy']:
    user.setproxy(args['proxy'])
    
if args['unsetproxy']:
    user.unsetproxy()

if args['downloadlatest']:
    user.downloadLatest(args['downloadlatest'])
    

