# Bitly url shorterer

Python3 script that make short bitlink url by bit.ly service or give stat for existing short link.
The script receive link url as argument. If given link is a short link the script returns stats othervise it makes new short link from given link or with wrong argument used it returns error ('Неправильный формат ссылки') 

Example: with shell from current directory (where is 'main.py' file)
```
python main.py {put here your url}
```

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).