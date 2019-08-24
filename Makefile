.PHONY: build test

build:
	docker build -t remcocats/ocrmypdf-nl .

test: build
	docker run --rm -it -e "PUID=1000" -e "PGID=1000" -v "$(PWD)/done:/done" -v "$(PWD)/error:/error" -v "$(PWD)/data:/data" -e "OCRMYPDF_LANGUAGE=nld" remcocats/ocrmypdf-nl
