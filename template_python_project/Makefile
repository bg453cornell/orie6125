DIR := ${CURDIR}

.PHONY: clean

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -fr htmlcov/

env:
	virtualenv --setuptools $@
	$@/bin/pip install -U "setuptools>=19,<20"
	$@/bin/pip install -U "pip>=7,<8"
	$@/bin/pip install -U "pip-tools==1.6.4"

env/.requirements: requirements.txt requirements-test.txt | env
	$|/bin/pip-sync $^
	touch $@

requirements.txt requirements-test.txt: %.txt: %.in | env
	$|/bin/pip-compile --no-index $^

# To run a test
# make test ARG='-k test_location'
test: env/.requirements
	env/bin/py.test tests $(ARG)

cover:
	make lint
	make cover_tests
	mkdir -p coverage
	cp coverage.xml coverage/cobertura-coverage.xml


lint: env/.requirements
	env/bin/flake8 --max-line-length=100 sorting tests

cover_tests: env/.requirements
	env/bin/py.test -s --tb short --cov-config .coveragerc --cov sorting --cov-report term-missing --cov-report xml \
	--cov-report html \
	--junitxml junit.xml \
	--no-cov-on-fail \
	--cov-fail-under=100 \
	tests



