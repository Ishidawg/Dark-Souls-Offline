# Dark Souls 2 Offline 💀
> **Software thats make Dark Souls 2 Offline.**

I decided to do this simple GUI off/on toggle dark souls network mode, to make easier as possible to use mods without being banned. Just start the app, browse to .exe, toggle the option and boom! easy!.

## Software GUI
<div align="center">
  <img alt="Ishidaw-HTML" src="https://github.com/Ishidawg/Dark-SoulsII-Offline/blob/main/images/Capture1.PNG?raw=true">
  <img alt="Ishidaw-CSS" src="https://github.com/Ishidawg/Dark-SoulsII-Offline/blob/main/images/Capture2.PNG?raw=true">
  <img alt="Ishidaw-Js" src="https://github.com/Ishidawg/Dark-SoulsII-Offline/blob/main/images/Capture3.PNG?raw=true">
</div>

## What I used to make it 📑
- **Code editor:** VSCODE
- **Language:** Python
- **Library:** customtkinter, subprocess, sys, ctypes and nuitka to make it .exe

## Logo or Icon 🎨
![dark-souls-logo](https://github.com/Ishidawg/Dark-SoulsII-Offline/blob/main/images/icon.png?raw=true)

## IMPORTANT!
To use, execute as administrator!
Why: cuz the software create a rule on firewall to make ds2.exe offline, and this require elevated privileges.

Another important note is: microsoft windows defender detects as a virus, false positive, cuz its was python file thats is now compiled to .exe.
I already submitted to microsoft that is a false positive, so maybe in four weeks (march 15) it will be solved, for now, just allow it on windows defender.

## How it works?
By now, u can just read the code and understand by ursef. But its basically some functions to check if a rule in firewall by name "Block Dark Souls" exists, if not, the status (if file founded) will be ONLINE (if rule not exists) and OFFLINE (if rule exists). The are three buttons, one to browse through game executable if its not on default steam installation folder, and both other to make it online and offline.
