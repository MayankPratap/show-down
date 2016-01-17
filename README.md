# show-down
A simple script to download latest episode of any TV show by simply typing a show name.

--> Dependencies

    --> python2 ( We are updating it to work in python3)
    --> beautifulsoup4 module of python :- Install it using "pip install beautifulsoup4" (without quotes) on terminal.
    
    
-->Download ZIP file for the repository/Clone the repository.

--> Run test.py 

--> If using for first time and your system is in proxy network then

    --> use "proxy -p http://user:pass@proxy:port" (without quotes)

    --> U can choose to change proxy anytime
    
--> For downloading :-

    --> use  " download -m <tv series name> -latest " (without quotes)
    
    --> Default format is .mp4

    --> for format setting use option -f

--> For coming out of downloader script :-

    --> Type "exit" (without quotes)

### Those who want to schedule their downloader to run weekly and check for latest episode of TV Series you entered :-
    
    #### For Ubuntu and other Linux versions
        
        --> Open Terminal type "crontab -e" (without quotes)
        
        --> Add this at end of file :- " @weekly DISPLAY=:0 xterm -e python2 /path/to/my/test.py " (without quotes)
               
                  For example :- @weekly DISPLAY=:0 xterm -e python2 /opt/lampp/htdocs/show-down/test.py
               
        --> save changes in crontab -e and exit.
        
        

