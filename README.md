
# /r/mealtimevideos to /r/pooptimevideos

It reposts videos from /r/mealtimevideos to /r/pooptimevideos

I'm already running the script so no point in you running it.

If you'd like to use it on another pair of subreddits:

1. Create a .env file in the same directory as this file
2. Add the following lines to the .env file:
```
source_subreddit=mealtimevideos
destination_subreddit=pooptimevideos

username=
password=
client_id=
secret=
user_agent=
```
3. Install dependencies
```
pip3 install -r requirements.txt
```
4. Run the script
```
python3 main.py
```


