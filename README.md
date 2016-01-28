# show-down

[![Join the chat at https://gitter.im/MayankPratap/show-down](https://badges.gitter.im/MayankPratap/show-down.svg)](https://gitter.im/MayankPratap/show-down?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

A simple script to download latest episode of any TV show by simply typing a show name.

Supported in Python3 only.

- Dependencies
    - beautifulsoup4 module of python :- Install it using command ```pip install beautifulsoup4``` in terminal.
    
    
- Download ZIP file for the repository/Clone the repository.

- If using for first time and your system is in proxy network then

    - Use ```python episode.py -p http://username:password@proxy_address:port```

    - You can choose to change proxy anytime
    
    - You can unset proxy by command ```python episode.py -u```
    
- For Downloading 

    - Use  ```python episode.py -dl show_name```
    
    - Download format is .mp4

- For Help
    
    - Type ```python episode.py -h```

- **Those who want to schedule their downloader to run weekly and check for latest episode of TV Series you entered :-**
    - *For Ubuntu and other Linux versions*
        
        - Open Terminal, type ```crontab -e```
        
        - Add this at end of file :- ```@weekly DISPLAY=:0 xterm -e python2 /path/to/my/episode.py```
               
            For example :- ```@weekly DISPLAY=:0 xterm -e python2 /opt/lampp/htdocs/show-down/episode.py```
               
        - Save changes in crontab -e and exit.
        
