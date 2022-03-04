![badge](https://github.com/kaloyan-marinov/rename-files/workflows/workflows_run-test-suite/badge.svg)

# Set up the project
```
$ python3 --version
Python 3.8.3

$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install --upgrade pip
(venv) $ pip install -r requirements.txt
```

# Run the tests
```
(venv) $ PYTHONPATH=. pytest \
    --cov=src/ \
    --cov-report=term-missing
```

# Example usage
```
(venv) $ cp -r \
    data \
    data-copy

(venv) $ PYTHONPATH=. \
    python src/rename.py \
    --directory=data-copy

(venv) $ rm -r data-copy/
```
