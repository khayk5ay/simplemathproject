install:
	pip install -r requirements.txt

lint:
	pylint --disable=R,C  hello.py, hellocli.py

test:
	python -m pytest -vv --cov=hello test_hello.py