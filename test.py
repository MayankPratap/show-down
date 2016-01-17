import os
from showDown import showDown

print ('\n##############################################################################')
print (' Show Down v1.0 ')

print ('##############################################################################')
def main() :
    data = []
    user = showDown()
    try:
    	cmd = input('>> ')
    except:
    	cmd = raw_input('>> ')
    cmd = " ".join(cmd.split())
    data = cmd.split('-')
    
    options = {}
    command = data[0].strip().lower()
    for row in data :
        if row.find(' ') != -1:
            option = row.split(' ')
            if len(option) >= 2:
                options['%s'%option[0]] = " ".join(option[1:]).strip()
            elif len(option) >= 1:
                options['%s'%option[0]] = ''
        else :
            options['%s'%row] = ''
    if command == 'proxy' :
        if 'p' in options :
            user.setproxy(options['p'])
        else :
            print ('Error : Set proxy using -p switch . Format : http://username:password@proxy:port')
    elif command == 'exit':
        os.system('setterm -cursor on')
        exit()
    elif command == 'download':
        if 'm' in options :
            if 'f' in options and 'latest' in options:
                if options['f'].lower() == 'mp4' or options['f'].lower() == '3gp' :
                    user.downloadLatest(options['m'] , options['f'] )
                else :
                    print ('Error : Format not supported. Only mp4 and 3gp supported.')
            elif 'latest' in options :
                user.downloadLatest(options['m'] , "mp4" )
                         
    else :
         print ('Invalid command : %s' %(data[0]))
    main()
             
main()

