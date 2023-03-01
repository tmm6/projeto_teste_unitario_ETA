# ETA

## Setup

```bash
pip install -r requirements.txt
```

## Pytest

```bash
pytest .
```

## Test Coverage

- `coverage` and `pytest-cov` packages are required
- Add `pragma: no cover` to exclude code from coverage report

### With `pytest`

Terminal report:

 ```bash
pytest ./test/models --cov-report term-missing --cov . 
 ```

HTML report:

```bash
pytest --cov-report html --cov .
```
  or 
 ```bash
pytest ./test/models --cov . --cov-report html
 ```
