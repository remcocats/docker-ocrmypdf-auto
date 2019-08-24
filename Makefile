.PHONY: build test

build:
	docker build -t remcocats/ocrmypdf-nl .

test: build
	docker run --rm -it -e "PUID=1000" -e "PGID=1000" -v "$(PWD)/ocr:/ocr" -e "OCRMYPDF_LANGUAGE=nld" remcocats/ocrmypdf-nl
