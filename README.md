Proyecto para Raspberry Pi 3 que recibe ordenes por voz. Según lo detectado, prende leds (luces), averigua el clima en internet y lo comunica vía voz. Modular, cada componente puede ser cloud o local.


# Tecnlogías
* Speech to text
* Text to speech
* Web APIs vía json

# Componentes
* Raspberry Pi 3
* Placa de audio USB con mic
* Speaker
* Push button, leds, resistencias

Raspbian OS
https://www.raspberrypi.org/downloads/raspbian/

# APIs 

# Local

## Text to Speech
$ sudo apt-get install festival

## Rest API WebService
$ sudo pip install flask
 
# Cloud

## Wolfram Alpha
API (free): http://products.wolframalpha.com/api/
$ sudo pip install wolframalpha

## IBM Watson
API (demo): https://developer.ibm.com/watson/
$ sudo pip install --upgrade watson-developer-cloud

## Google Cloud
API (demo): https://cloud.google.com/speech/docs/
$ git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git
$ cd python-docs-samples/speech/api-client
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
