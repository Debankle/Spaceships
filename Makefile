PYTHON=python3
BUILDFLAGS=-i pygame -O2

SRC=src/main.py
SETUP=setup.py
APP=dist/main.app

all: test

.PHONY: all test build

test: $(SRC)
	$(PYTHON) $^

build: $(SETUP)
	$(PYTHON) $^ py2app $(BUILDFLAGS)

run:
	open $(APP)

clean:
	rm -rf build dist
	find . | grep -E "(__pycache__)" | xargs rm -rf