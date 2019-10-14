# pwna-sound
sound plugin for https://github.com/evilsocket/pwnagotchi

An sound plugin for https://github.com/evilsocket/pwnagotchi that plays an wav file with aplay on events and uses a text2speech engine

- tested with pnagotchi 1.0.0-RC5

- this plugin needs an soundcard/HAT or a connected bt-headset for output, like https://www.ebay.de/itm/NEU-Audio-DAC-HAT-Sound-Card-AUDIO-SPEAKER-MIC-For-Raspberry-Pi-Zero-A-B/133
059926731

- for enable text2speech on raspberry-pi-zero with debian buster to speak the SSID on handshake and others, you need to install "pico2wave" as root:
```Shell
   wget http://archive.raspberrypi.org/debian/pool/main/s/svox/libttspico-utils_1.0+git20130326-3+rpi1_armhf.deb
   wget http://archive.raspberrypi.org/debian/pool/main/s/svox/libttspico0_1.0+git20130326-3+rpi1_armhf.deb
   apt-get install -f ./libttspico0_1.0+git20130326-3+rpi1_armhf.deb ./libttspico-utils_1.0+git20130326-3+rpi1_armhf.deb
   # test:
   pico2wave -w lookdave.wav "Look Dave, I can see you're really upset about this." && aplay lookdave.wav
```

- with https://www.raspiaudio.com/promo you can use the button to shutdown your raspberry-pi. read shutdown_button.py for help

- add nedded config in /etc/pnagotchi/config.yml
```YAML
plugins:
      pwna-sound:
        enabled: true
        sound-dir: default
        text2speech-use: false
        text2speech-lang: en-US
```
