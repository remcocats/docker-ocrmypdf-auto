.PHONY: build test

build:
	docker build -t choffmeister/ocrmypdf-auto .

test: build
	docker run --rm -it -v "$(PWD)/data:/data" -e "OCRMYPDF_LANGUAGE=deu" choffmeister/ocrmypdf-auto
