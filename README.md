
# Reddit crossposter script

I'm using it to repost videos from /r/mealtimevideos to /r/pooptimevideos


If you'd like to use it on another pair of subreddits:

1. Create a .env file in the same directory as this file
2. Add the following lines to the .env file:
```
source_subreddit=
destination_subreddit=

username=
password=
client_id=
secret=
user_agent=
```
3. Setup virtual env
```
pip3 install virtualenv
python3 -m venv env
source env/bin/activate
```
4. Install dependencies
```
pip3 install -r requirements.txt
```
5. Run the script
```
python3 main.py
```


