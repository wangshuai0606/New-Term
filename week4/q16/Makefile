.PHONY: all check build clean

all: check build

check:
	./check.sh

build:
	pip wheel . --no-deps -w dist

clean:
	rm -rf build src/greetlab_25040032035.egg-info
