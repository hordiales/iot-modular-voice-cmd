Proyecto para Raspberry Pi 3 que recibe ordenes por voz. Según lo detectado, prende leds (luces), averigua el clima en internet y lo comunica vía voz. Modular, cada componente puede ser cloud o local.


# Servicios
* Speech To text (voz a texto)
* Text To speech (texto a voz)
* Weather (clima)
* General json web APIs

# Componentes
* Raspberry Pi 3
* Placa de audio USB con mic
* Speaker
* Push button, leds, resistencias (10k, 560 ohms)

Raspbian OS
https://www.raspberrypi.org/downloads/raspbian/

# APIs 

# Local

## Text to Speech
$ sudo apt-get install festival


or


$ sudo apt-get install espeak

## Voice recording

8 and 16 bits (narrow and broad band detection)

8 bits: $ arecord -d 5 -D plughw:1,0 test8.wav
        
16 bits: $ arecord -d 5 -f cd -D plughw:1,0 test16.wav

## Rest API WebService
$ sudo pip install flask
 
# Cloud

## Wolfram Alpha
API (free): http://products.wolframalpha.com/api/

$ sudo pip install wolframalpha

queries: forecast and other general requests

## IBM Watson
API (demo): https://developer.ibm.com/watson/

Use: Speech2Text, Voice Synthesis (text2speech)

$ sudo pip install --upgrade watson-developer-cloud

## Google Cloud
API (demo): https://cloud.google.com/speech/docs/

Use: Speech2Text

$ git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git

$ cd python-docs-samples/speech/api-client

$ virtualenv env

$ source env/bin/activate

$ pip install -r requirements.txt

## Others

Weather: forecast.io, http://www.wunderground.com/weather/api/ 