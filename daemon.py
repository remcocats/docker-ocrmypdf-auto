#!/usr/bin/python3

import datetime
import os
import re
import subprocess
import time

base_folder = '/ocr/data'
done_folder = '/ocr/done'
error_folder = '/ocr/error'

def run(bin, params):
    p = subprocess.Popen([bin] + params)
    p.communicate()
    if p.returncode != 0:
        raise Exception('Command %s exited with code %d' % (bin, p.returncode))

def check(file_in, file_out):
    file_in_name = os.path.basename(file_in)
    if re.match(r'^[\.@].*$', file_in_name) or re.match(r'^.*\-ocr\.pdf$', file_in_name):
        return False
    else:
        if os.path.isfile(file_out):
            return False
        else:
            return True

def get_file_next():
    os.listdir(base_folder)
    for file in filter(lambda f: os.path.isfile(os.path.join(base_folder, f)), os.listdir(base_folder)):
        file_in = os.path.join(base_folder, file)
        file_in_done = os.path.join(done_folder, file)
        file_in_error = os.path.join(error_folder, file)
        file_out = re.sub(r'\.pdf$', '-ocr.pdf', file_in)
        file_out_done = re.sub(r'\.pdf$', '-ocr.pdf', file_in_done)
        if check(file_in, file_out):
            return file_in, file_out, file_in_done, file_out_done, file_in_error
    return None

while True:
    file_next = get_file_next()
    if file_next:
        file_in, file_out, file_in_done, file_out_done, file_in_error = file_next
        print('Processing %s...' % file_in)
        try:
            run('ocrmypdf', [
                '-l', os.environ['OCRMYPDF_LANGUAGE'],
                '--rotate-pages',
                '--deskew',
                '--clean',
                '--force-ocr',
                '--tesseract-oem', '1',
                '--remove-background',
                '--optimize', '3',
                '--jobs', '4',
                '--output-type', 'pdfa',
                file_in,
                file_out
            ])
            print('Done.')
            os.rename(file_in, file_in_done)
            print('move file %s to %s' % (file_in, file_in_done))
            os.rename(file_out, file_out_done)
            print('move file %s to %s' % (file_out, file_out_done))
        except BaseException as e:
            print('Error: %s' % str(e))
            os.rename(file_in, file_in_error)
            print('move file %s to %s' % (file_in, file_in_error))
    time.sleep(15)



#    language=None,
#     image_dpi=None,
#     output_type=None,
#     sidecar=None,
#     jobs=None,
#     use_threads=None,
#     title=None,
#     author=None,
#     subject=None,
#     keywords=None,
#     rotate_pages=None,
#     remove_background=None,
#     deskew=None,
#     clean=None,
#     clean_final=None,
#     unpaper_args=None,
#     oversample=None,
#     remove_vectors=None,
#     threshold=None,
#     force_ocr=None,
#     skip_text=None,
#     redo_ocr=None,
#     skip_big=None,
#     optimize=None,
#     jpg_quality=None,
#     png_quality=None,
#     jbig2_lossy=None,
#     jbig2_page_group_size=None,
#     pages=None,
#     max_image_mpixels=None,
#     tesseract_config=None,
#     tesseract_pagesegmode=None,
#     tesseract_oem=None,
#     pdf_renderer=None,
#     tesseract_timeout=None,
#     rotate_pages_threshold=None,
#     pdfa_image_compression=None,
#     user_words=None,
#     user_patterns=None,
#     fast_web_view=None,
#     keep_temporary_files=None,
#     progress_bar=None,
#     tesseract_env=None,