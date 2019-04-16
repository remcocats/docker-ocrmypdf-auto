FROM jbarlow83/ocrmypdf-alpine:latest

RUN apk add --update --no-cache s6 tesseract-ocr-data-deu
COPY docker-entry.sh /docker-entry.sh
COPY daemon.py /daemon.py
ENV OCRMYPDF_LANGUAGE eng
ENTRYPOINT ["/docker-entry.sh"]
