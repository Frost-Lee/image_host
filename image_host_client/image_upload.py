import requests
import re
import argparse
import os
import shutil

import config_secure

arg_parser = argparse.ArgumentParser(
    description='Client application for uploading image to image host.'
)
arg_parser.add_argument(
    'file',
    help='The path of the image to be uploaded.',
    type=str
)
arg_parser.add_argument(
    '-u',
    '--url', 
    help='URL address of uploading destination.', 
    type=str,
    default=config_secure.DEFAULT_URL
)
arg_parser.add_argument(
    '-t',
    '--token', 
    help='Token of the session.', 
    type=str,
    default=config_secure.DEFAULT_TOKEN
)
arg_parser.add_argument(
    '-q',
    '--quality', 
    help='Compress quality. 0 to 100, greater number means better quality', 
    type=int,
    default=100
)

args = arg_parser.parse_args()

with open(args.file, 'rb') as in_file:
    response = requests.post(
        args.url,
        files={
            'image' : in_file
        },
        data={
            'token' : args.token,
            'compress_quality' : args.quality
        }
    )
    print(response.text)
    os.system('echo {} | pbcopy'.format(response.text))
    if '/' in response.text:
        file_name = response.text.split('/')[-1]
        shutil.copyfile(args.file, os.path.join(os.path.dirname(args.file), file_name))
