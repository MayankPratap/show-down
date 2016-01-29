from showDown import showDown
from showDown_hd import showDown_hd
import argparse

user = showDown()
user_hd = showDown_hd()

parser = argparse.ArgumentParser(description='A Command line tool to download your favorie TV Shows')
parser.add_argument('-dl','--downloadlatest', help='Download the latest episode of your favorite TV Show', required=False)
parser.add_argument('-hdl','--highdefinition', help='Download the latest episode in HD', required=False)
parser.add_argument('-p','--proxy', help='Set the proxy', required=False)
parser.add_argument('-u','--unsetproxy', help='Unset the proxy', action='store_true')

args = vars(parser.parse_args())

if args['proxy']:
    user.setproxy(args['proxy'])
    
elif args['unsetproxy']:
    user.unsetproxy()

elif args['highdefinition']:
	user_hd.downloadLatest(args['highdefinition'])

elif args['downloadlatest']:
    user.downloadLatest(args['downloadlatest'])
    

