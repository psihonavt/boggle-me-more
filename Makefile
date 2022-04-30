deps:
	pip install -r requirements.txt

run:
	PYTHONPATH=$(shell pwd)/src src/hosted_boggle_python/server.py

test:
	PYTHONPATH=$(shell pwd)/src python -m unittest -v tests/handlers.py tests/server.py
