# Set up the project
```
$ python3 --version
Python 3.8.3

$ pytho3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install --upgrade pip
(venv) $ pip install -r requirements.txt
```

# Run the tests
```
$ PYTHONPATH=. pytest \
    --cov=src/ \
    --cov-report=term-missing
```