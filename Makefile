init:
	pip install -r requirements.txt

test:
	pytest tests

build: 
	python setup.py sdist
	python setup.py bdist_wheel --universal

install: build
	pip install ./dist/filetree-*.tar.gz

publish: build
	python setup.py register
	python setup.py sdist upload
	python setup.py bdist_wheel --universal upload
	rm -fr build dist filetree.egg-info

.PHONY: init test build install publish
