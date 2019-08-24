# ocrmypdf-nl

A docker daemon that watches a given folder and automatically runs [OCRmyPDF](https://github.com/jbarlow83/OCRmyPDF) on PDFs placed inside that folder.
This is a fork from [ocrmypdf-auto](https://github.com/choffmeister/docker-ocrmypdf-auto) only added support for nld fra and spa

Extended error folder for pdf files that can't be done.
A done folder for files that have been done.

All files are done with OCR even if they have OCR.

```
# out of the box supported languages are "eng", "deu", "nld", "spa" and "fra"  
docker run -d -e PUID=1000 -e PGID=1000 -v $PWD/data:/data -v $PWD/done:/done -v $PWD/error:/error -e OCRMYPDF_LANGUAGE=eng+nld remcocats/ocrmypdf-nl:latest
```