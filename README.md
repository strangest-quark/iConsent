# iConsent

## Setup
Python 3.7+

    brew install imagemagick
    brew install cairo
    pip install -r requirements.txt
    
Create empty folders in assets. Like /assets/video and /assets/audio.
 
## Add fonts to Imagemagick
http://www.bigbing.net/2016/08/11/add-new-font-imagemagick-mac-osx/
1. Hindi - https://fonts.google.com/specimen/Noto+Sans?subset=devanagari#standard-styles
2. Tamil - https://fonts.google.com/specimen/Meera+Inimai?subset=tamil&preview.text_type=custom
 
## Input
Modify input.json

## Run
    python main.py
 
## Troubleshooting
* ImageMagick on MacOS does not load fonts: https://github.com/tlk/homebrew-imagemagick-x11
