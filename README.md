[![workflows_run-test-suite](https://github.com/kaloyan-marinov/rename/actions/workflows/run-test-suite.yml/badge.svg)](https://github.com/kaloyan-marinov/rename/actions/workflows/run-test-suite.yml)

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
    --cov-report=term-missing \
    --cov-branch
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
