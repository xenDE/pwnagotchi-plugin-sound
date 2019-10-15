__author__ = 'https://github.com/xenDE/pwnagotchi-plugin-sound'
__version__ = '1.0.0'
__name__ = 'sound'
__license__ = 'GPL3'
__description__ = 'An plugin for pwnagotchi that plays an wav file with aplay on events and uses a text2speech engine. tested with 1.0.0-RC4'
__help__ = """
-this plugin needs a installed and working audio DAC HAT, USB-Soundcard or a connected bt-headset/headphone for audio output, like https://www.raspiaudio.com/
-for enable text2speech on raspberry-pi-zero with debian buster to speak the SSID on handshake and others, you need to install "pico2wave" as root:
⋅⋅⋅wget http://archive.raspberrypi.org/debian/pool/main/s/svox/libttspico-utils_1.0+git20130326-3+rpi1_armhf.deb
⋅⋅⋅wget http://archive.raspberrypi.org/debian/pool/main/s/svox/libttspico0_1.0+git20130326-3+rpi1_armhf.deb
⋅⋅⋅apt-get install -f ./libttspico0_1.0+git20130326-3+rpi1_armhf.deb ./libttspico-utils_1.0+git20130326-3+rpi1_armhf.deb
⋅⋅⋅# test:
⋅⋅⋅pico2wave -w lookdave.wav "Look Dave, I can see you're really upset about this." && aplay lookdave.wav
-with device https://www.raspiaudio.com/promo you can use the yellow button to shutdown your raspberry-pi. read sound/shutdown_button.py for help
-install: copy "sound.py" and "sound/" dir to your configured "custom_plugins" directory and add+edit sound config to /etc/pnagotchi/config.yml:
⋅⋅⋅    custom_plugins: /usr/local/pwnagotchi/plugins
⋅⋅⋅    plugins:
⋅⋅⋅      sound:
⋅⋅⋅        enabled: true
⋅⋅⋅        sound-dir: default
⋅⋅⋅        text2speech-use: false
⋅⋅⋅        text2speech-lang: en-US
"""

import logging
import os, sys
from subprocess import call

OPTIONS = dict()


def play_my_sound(event, say=""):
    "this function plays the event.wav file and if say is not empt, it talks this with text2speech after playing the event"
    sounddir = os.path.dirname(os.path.realpath(__file__))+"/sound/"+OPTIONS['sound-dir']+"/"
    soundfile= sounddir+event+".wav"
    if os.path.isfile(soundfile):
        t2s = '"'+OPTIONS['text2speech-lang']+'"'
        if OPTIONS['text2speech-use']:
            t2s += ' "'+say+'"'
        command = ["/bin/bash", "bash", "-c", sounddir+"do_play.sh "+soundfile+' '+t2s+" & disown"]
        logging.info("plugin.sound: event:"+event+" say:"+t2s)
        os.spawnlp(os.P_WAIT, *command)
    else:
        logging.debug("plugin.sound: file not exist: "+soundfile)
        pass


# called when the plugin is loaded
def on_loaded():
    logging.info("sound plugin loaded")
    # sys._getframe().f_code.co_name = "on_loaded"  <<< the event/function name
    play_my_sound(sys._getframe().f_code.co_name)


# called when a new handshake is captured, access_point and client_station are json objects
def on_handshake(agent, filename, access_point, client_station):
    #    access_point: {'ipv4': '0.0.0.0', 'ipv6': '', 'mac': '44:4e:6d:aa:aa:aa', 'hostname': 'FRITZ!Box 6430 Cable BX', 'alias': '', 'vendor': 'AVM Audiovisuelles Marketing und Computersysteme GmbH', 'first_seen': '2019-10-08T01:24:08.535091885+01:00', 'last_seen': '2019-10-08T01:24:32.879958989+01:00', 'meta': {'values': {}}, 'frequency': 2437, 'channel': 6, 'rssi': -85, 'sent': 161, 'received': 0, 'encryption': 'WPA2', 'cipher': 'CCMP', 'authentication': 'PSK', 'wps': {'Config Methods': 'Push Button, Keypad, Display', 'Device Name': 'FBox', 'Manufacturer': 'AVM', 'Model Name': 'FBox', 'Model Number': '0000', 'Primary Device Type': 'AP (oui:0050f204)', 'RF Bands': '2.4Ghz', 'Response Type': 'AP', 'Serial Number': '0000', 'State': 'Configured', 'UUID-E': '133567cc5f3d5060000000000000000', 'Version': '2.0'}, 'clients': [], 'handshake': True}
    # talk the hostname after event.wav is played
    play_my_sound(sys._getframe().f_code.co_name, str(access_point["hostname"]))


# callend when the agent is deauthenticating a client station from an AP
def on_deauthentication(agent, access_point, client_station):
    play_my_sound(sys._getframe().f_code.co_name)


# called to setup the ui elements
def on_ui_setup(ui):
    play_my_sound(sys._getframe().f_code.co_name)


# called when the ui is updated
def on_ui_update(ui):
    play_my_sound(sys._getframe().f_code.co_name)


# called when the hardware display setup is done, display is an hardware specific object
def on_display_setup(display):
    play_my_sound(sys._getframe().f_code.co_name)


# called when everything is ready and the main loop is about to start
def on_ready(agent):
    play_my_sound(sys._getframe().f_code.co_name)


# called when the AI finished loading
def on_ai_ready(agent):
    play_my_sound(sys._getframe().f_code.co_name)


# called when the AI finds a new set of parameters
def on_ai_policy(agent, policy):
    play_my_sound(sys._getframe().f_code.co_name)


# called when the AI starts training for a given number of epochs
def on_ai_training_start(agent, epochs):
    play_my_sound(sys._getframe().f_code.co_name)


# called after the AI completed a training epoch
def on_ai_training_step(agent, _locals, _globals):
    play_my_sound(sys._getframe().f_code.co_name)


# called when the AI has done training
def on_ai_training_end(agent):
    play_my_sound(sys._getframe().f_code.co_name)


# called when the AI got the best reward so far
def on_ai_best_reward(agent, reward):
    play_my_sound(sys._getframe().f_code.co_name)


# called when the AI got the best reward so far
def on_ai_worst_reward(agent, reward):
    play_my_sound(sys._getframe().f_code.co_name)


# called when a non overlapping wifi channel is found to be free
def on_free_channel(agent, channel):
    play_my_sound(sys._getframe().f_code.co_name)


# called when the status is set to bored
def on_bored(agent):
    play_my_sound(sys._getframe().f_code.co_name)


# called when the status is set to sad
def on_sad(agent):
    play_my_sound(sys._getframe().f_code.co_name)


# called when the status is set to excited
def on_excited(agent):
    play_my_sound(sys._getframe().f_code.co_name)


# called when the status is set to lonely
def on_lonely(agent):
    play_my_sound(sys._getframe().f_code.co_name)


# called when the agent is rebooting the board
def on_rebooting(agent):
    play_my_sound(sys._getframe().f_code.co_name)


# called when the agent is waiting for t seconds
def on_wait(agent, t):
    play_my_sound(sys._getframe().f_code.co_name)


# called when the agent is sleeping for t seconds
def on_sleep(agent, t):
    play_my_sound(sys._getframe().f_code.co_name)


# called when the agent refreshed its access points list
def on_wifi_update(agent, access_points):
    play_my_sound(sys._getframe().f_code.co_name)


# called when the agent is sending an association frame
def on_association(agent, access_point):
    play_my_sound(sys._getframe().f_code.co_name)


# callend when the agent is tuning on a specific channel
def on_channel_hop(agent, channel):
    play_my_sound(sys._getframe().f_code.co_name)


# called when an epoch is over (where an epoch is a single loop of the main algorithm)
def on_epoch(agent, epoch, epoch_data):
    play_my_sound(sys._getframe().f_code.co_name)


# called when a new peer is detected
def on_peer_detected(agent, peer):
    play_my_sound(sys._getframe().f_code.co_name)


# called when a known peer is lost
def on_peer_lost(agent, peer):
    play_my_sound(sys._getframe().f_code.co_name)
