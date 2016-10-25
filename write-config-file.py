import json

watson_config = {'watson.username': '', 'watson.password': ''}

wolframalpha_config = {'wolfram.app_id': ''}

leds_config = {'led.red': '18', 'led.green': '23'}

# spech2text: watson / google / local? / LAN_Rest_API
# text2speech: festival / espeak
services_config = {'speech2text': 'watson', 'text2speech': 'festival', 'record': 'arecord'}

# quality (and broad or narrowband model): 8bits vs 16bits (bug with 16bits and arecord)
audio_qualitiy = {'audio.quality': '8bits'}

def merge_dicts(*dict_args):
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

config = merge_dicts(watson_config, wolframalpha_config, leds_config, services_config)

print(config)
with open('iot-config.json', 'w') as f:
    json.dump(config, f)
