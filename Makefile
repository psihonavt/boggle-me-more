deps:
	pip install -r requirements.txt

run:
	PYTHONPATH=$(shell pwd) runtime/bin/gunicorn -c gunicorn.conf src.boggle.application:WEB_SERVER

test:
	PYTHONPATH=$(shell pwd)/src runtime/bin/python -m pytest -v tests
