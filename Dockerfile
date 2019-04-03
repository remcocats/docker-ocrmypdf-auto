FROM jbarlow83/ocrmypdf-alpine:latest

RUN apk add --update --no-cache tesseract-ocr-data-deu
COPY daemon.py /daemon.py
ENV OCRMYPDF_LANGUAGE eng
ENTRYPOINT ["/daemon.py"]
