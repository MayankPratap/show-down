import os
import sys
from showDown import showDown

def main() :
	user = showDown()
	    
	if sys.argv[1] == '-p':
		user.setproxy(sys.argv[2])
		
	elif sys.argv[1]=='-d' and sys.argv[2]=='-l':
		user.downloadLatest(sys.argv[3])
		                         
	else:
		print ('Invalid command : %s' %sys.argv[1])

main()
