#!/usr/bin/python3

import datetime
import os
import re
import subprocess
import time

base_folder = '/data'

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
        file_out = re.sub(r'\.pdf$', '-ocr.pdf', file_in)
        if check(file_in, file_out):
            return file_in, file_out
    return None

while True:
    file_next = get_file_next()
    if file_next:
        file_in, file_out = file_next
        print('Processing %s...' % file_in)
        try:
            run('ocrmypdf', [
                '-l', os.environ['OCRMYPDF_LANGUAGE'],
                '--rotate-pages',
                '--deskew',
                '--clean',
                '--force-ocr',
                '--remove-background',
                '--optimize', '3',
                '--jobs', '4',
                '--output-type', 'pdfa',
                file_in,
                file_out
            ])
            print('Done.')
        except BaseException as e:
            print('Error: %s' % str(e))
    time.sleep(15)
