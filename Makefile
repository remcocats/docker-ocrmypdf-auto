.PHONY: build test

build:
	docker build -t choffmeister/ocrmypdf-auto .

test: build
	docker run --rm -it -e "PUID=1000" -e "PGID=1000" -v "$(PWD)/data:/data" -e "OCRMYPDF_LANGUAGE=deu" choffmeister/ocrmypdf-auto
