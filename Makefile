init:
	pip install -r requirements.txt

test:
	pytest tests -r P

build:
	python setup.py sdist
	python setup.py bdist_wheel --universal

install: clean build uninstall
	pip install ./dist/filetree-*.tar.gz

publish: clean build
	twine upload dist/*

uninstall:
	pip uninstall filetree -y

clean:
	rm -fr build dist filetree.egg-info

.PHONY: init test build install publish uninstall clean
