# -*- coding: utf-8 -*-
#!/usr/bin/python2

# Author: Hernán Ordiales <hordiales@gmail.com>

import os
import subprocess
import time
import sys
import json

# Cloud APIs
from watson_developer_cloud import SpeechToTextV1
import wolframalpha

# rpy
import RPi.GPIO as GPIO

# Config file
with open('iot-config.json', 'r') as f:
    config = json.load(f)

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIN_RED_LED = int(config['led.red'])
PIN_GREEN_LED = int(config['led.green'])
GPIO.setup(PIN_RED_LED,GPIO.OUT) 
GPIO.setup(PIN_GREEN_LED,GPIO.OUT)

PIN_REC_BTN = int(config['btn.rec'])
GPIO.setup(PIN_REC_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Cloud APIs initialization
speech_to_text = SpeechToTextV1(
    username=config['watson.username'],
    password=config['watson.password'],
    x_watson_learning_opt_out=False
)
audio_type = 'audio/wav'
continuous = False # short phrases

app_id=config['wolfram.app_id']
client = wolframalpha.Client(app_id)

def turnOnOffLed(pin=PIN_RED_LED, sleeptime=1):
  print("LED %i on"%pin)
  GPIO.output(pin,GPIO.HIGH)
  time.sleep(sleeptime)
  print("LED %i off"%pin)
  GPIO.output(pin,GPIO.LOW)

def record_voice_cmd(duration,filename):       
    '''
        16 bits: arecord -f cd -D plughw:1,0 test16.wav
    '''
    # arecord bug with 16 bits (many wav files)
    #rec_cmd = "arecord -d %i -f cd -D plughw:1,0 %s"%(duration,filename)
    rec_cmd = "arecord -d %i -D plughw:1,0 %s"%(duration,filename)
    subprocess.call(rec_cmd, shell=True)

seconds = 4
audio_quality = "8bits" # o 16bits
rec_filename = ""
audio_model = ""
if audio_quality=="8bits":
    rec_filename = "tmp_8bits.wav"
    audio_model = 'es-ES_NarrowbandModel'
else:
    rec_filename = "tmp_16bits.wav"
    audio_model = 'es-ES_BroadbandModel'

def voice(txt):
    subprocess.call("echo \"%s\" | festival --tts "%txt, shell=True)

def detect_and_cmd():
  GPIO.output(PIN_RED_LED,GPIO.HIGH) # on
  record_voice_cmd(seconds,rec_filename)
  GPIO.output(PIN_RED_LED,GPIO.LOW) # off

  with open(join(dirname("__file__"), rec_filename), 'rb') as audio_file:
          #Watson API
          print("Cloud: speech2text IBM Watson API")
          a = json.dumps( speech_to_text.recognize(
                  audio_file, content_type=audio_type, timestamps=True, model=audio_model, continuous=continuous) )
          #Google API (TODO)
          
          b = json.loads( a )
          print( b )
          print( "Result: ")
          try:
            print( b['results'][0]['alternatives'][0]['transcript'] )
            transcript = b['results'][0]['alternatives'][0]['transcript']
            transcript = transcript.strip()
            transcript = transcript.lower()
            #TODO: check confidence value
          except Exception, e:
            print(e)
            transcript = ""
          print("Comando: ")
          if "ojo" in transcript: # ROJO 'ojo'/'rojo
              voice("RED LED")
              turnOnOffLed(pin=PIN_RED_LED, sleeptime=2)
          elif "erde" in transcript: #VERDE 'erde'/'verde''
              voice("GREEN LED")
              turnOnOffLed(pin=PIN_GREEN_LED, sleeptime=2)
          elif "lima" in transcript: # Acepta 'clima', 'lima' o 'el clima'
              print("Cloud: Wolfram API")
              query="Forecast Buenos Aires"
              res = client.query(query)
              output = next(res.results).text
              temp, state = output.split('\n')
              print(state)
              clima = state
              voice(clima)
          else:
              print("No se detecto comando")
              voice(transcript)

  print("En")
#detect_and_cmd()

#TODO: run as startup service https://www.raspberrypi.org/documentation/linux/usage/rc-local.md
if __name__ == '__main__':
  while True:
    #WARNING: cloud API consumption
    input_state = GPIO.input(PIN_REC_BTN)
    if input_state == False:
        print('REC button pressed')
        detect_and_cmd()
        time.sleep(0.2)
