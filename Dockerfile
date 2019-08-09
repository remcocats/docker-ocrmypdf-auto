FROM jbarlow83/ocrmypdf-alpine:latest

RUN apk add --update --no-cache s6 \
    tesseract-ocr-data-deu \
    tesseract-ocr-data-nld \
    tesseract-ocr-data-spa \
    tesseract-ocr-data-fra

COPY docker-entry.sh /docker-entry.sh
COPY daemon.py /daemon.py
ENV OCRMYPDF_LANGUAGE eng+deu+nld+spa+fra
ENTRYPOINT ["/docker-entry.sh"]
