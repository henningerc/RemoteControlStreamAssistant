# RemoteControlStreamingAssistant

# What's that?
In short, this is a streamdeck and chatbot for twitch you can start on a PC.
It allows to change scenes, show overlays or mute sound on keypresses (only F-Keys for now) and shows the chat. It also plays a sound on every message if the file is given.

# Installation
Download the package, unzip it and start the program 
```
pip3 install -r requirements.txt
``` 
in the main folder to install all requirements. 

To start the software go to the folder and start with
```
python main.py
```

# Configuration
The software is configured by a file named settings.json in the starting folder. It is a json-file and there is an example provided.

You should at least give it your Twitch- and OBS-data. You can change any button that is on there easily by the corresponding map from the json-file.

## Commands
---
### switch_scene
This command allows you to switch to another scene on OBS  
* **scene:** The name of the scene as written in OBS
---
### switch_overlay
Will be renamed to toggle_overlay soon, lets you toggle the overlays visibility on and off  
* **scene:** The name of the scene the overlay is in
* **source:** The name of the overlays source
---
### set_mute
Mutes an audiosource  
* **source:** The audiosource that will be muted
---
### set_unmute
Unmutes an audiosource
* **source:** The audiosource that will be unmuted
---
### toggle_mute
Toggles the mute of an audiosource
* **source:** The audiosource that will be toggled
---

There are also "statuslamps" indicators. You can configure them with operators. There are three by now:
## Statuslamps
### scene_active
Shows which scene is active. Can have several colors.
* **scenes:** The map of the scenes with corresponding colors (HTML-Format)
---
### scene_item_visible
Shows if an overlay is visible or not.
* **scene:** The scene the overlay is on
* **source:**  The source the overlay is in
---
### audio_muted
Shows if the audio is muted
* **source:** The audiosource of that should be muted
---

# Bugreports and feature-requests
You can send bugreports and requests for features to the github issue-tracker found at https://github.com/henningerc/RemoteControlStreamAssistant/issues