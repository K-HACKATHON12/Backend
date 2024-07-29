# venv
```shell
python -m venv venv
source venv/Scripts/activate
```

# start
```shell
pip install -r requirements.txt
uvicorn main:app --reload
```

# create requirements.txt
```shell
pip freeze > requirements.txt
```
