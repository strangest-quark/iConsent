<h1 align="center">
iConsent
</h1>

<p align="center">
  <a href="https://github.com/strangest-quark/iConsent/actions?query=workflow%3AVue" alt="Vue"><img src="https://github.com/strangest-quark/iConsent/workflows/Vue/badge.svg" /></a>
  <a href="https://github.com/strangest-quark/iConsent/actions?query=workflow%3AFlask" alt="Flask"><img src="https://github.com/strangest-quark/iConsent/workflows/Flask/badge.svg" /></a>
  <a href="https://github.com/strangest-quark/iConsent/actions?query=workflow%3AVue" alt="Video Generator"><img src="https://github.com/strangest-quark/iConsent/workflows/Video%20Geneartor/badge.svg" /></a>
  <br>
  <a href="https://iconsent.netlify.app/" alt="Netlify Status"><img src="https://api.netlify.com/api/v1/badges/679ce57f-f995-4feb-a1b1-b084a79075b6/deploy-status" /></a>
  <a href="https://www.patreon.com/iConsent" alt="Patreon"><img src="https://img.shields.io/badge/Sponsor on Patreon-iConsent-red.svg?logo=patreon" /></a>
</p>

## Setup
Python 3.7+

    cd aa-hack/video-generator
    brew install libraqm
    pip install -r requirements.txt
 
## Input
Modify aa-hack/video-generator/config/local_input.json

## Local Run
    cd video-generator
    python debug.py
 
## Deployments
Based out of serverless framework. Custom lambda layer for text rendering will be needed to set this up in lambda. Reach out to maintainers for details.

    cd aa-hack/video-generator
    sls deploy
    
## Target state - Modules

WIP for frame-by-frame config for modular components of iConsent. Run modules/debug.py to test the modules separately. Fine grained config to play with in modules/config/

## Maintainers

|     Sowmiya     |      Ikram      |    Pramothini  |
| :-------------: | :-------------: | :-------------:|
| <a href="https://www.buymeacoffee.com/strangestquark" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>| <a href="https://www.buymeacoffee.com/strangestquark" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a> | <a href="https://www.buymeacoffee.com/strangestquark" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a> |

## About
https://devfolio.co/submissions/iconsent

[![](http://img.youtube.com/vi/jUFco7XdpN4/0.jpg)](http://www.youtube.com/watch?v=jUFco7XdpN4 "iConsent")
