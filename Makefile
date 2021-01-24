install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt        

test:
	python -m pytest -vv tests/test_app.py
    
lint:
	pylint --disable=R,C,W0703 app.py

all: install lint test
