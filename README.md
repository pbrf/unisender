# unisender
Python script for use unisender API

```
pip install -r pip.txt
python commands.py subscribe


def subscribe():
    api = Unisender('api key')
    data = {'fields[email]': 'exmaple@example.com', 'list_ids': 100}
    print api.run('subscribe', data)
    
```
