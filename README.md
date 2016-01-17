# show-down
A simple script to download latest episode of any TV show by simply typing a show name.

Supported in both Python2 and Python3

- Dependencies
    - beautifulsoup4 module of python :- Install it using command ```pip install beautifulsoup4``` in terminal.
    
    
- Download ZIP file for the repository/Clone the repository.

- Run test.py 

- If using for first time and your system is in proxy network then

    - Use ```proxy -p http://user:pass@proxy:port```

    - You can choose to change proxy anytime
    
- For Downloading 

    - Use  ```download -m <tv series name> -latest```
    
    - Default format is .mp4

    - For format setting use option -f

- **Those who want to schedule their downloader to run weekly and check for latest episode of TV Series you entered :-**
    - *For Ubuntu and other Linux versions*
        
        - Open Terminal, type ```crontab -e```
        
        - Add this at end of file :- ```@weekly DISPLAY=:0 xterm -e python2 /path/to/my/test.py```
               
            For example :- ```@weekly DISPLAY=:0 xterm -e python2 /opt/lampp/htdocs/show-down/test.py```
               
        - Save changes in crontab -e and exit.
        
        

