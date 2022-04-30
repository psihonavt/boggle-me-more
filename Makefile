build:
	python3 -m virtualenv runtime
	runtime/bin/pip install -r requirements.txt

deps:
	bin/runtime/pip install -r requirements.txt

run:
	PYTHONPATH=$(shell pwd) runtime/bin/python src/boggle/server.py

test:
	PYTHONPATH=$(shell pwd)/src runtime/bin/python -m pytest -v tests
