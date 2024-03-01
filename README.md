# Dark Souls 2 Offline 💀
> **Software thats make Dark Souls 2 Offline.**

I decided to do this simple GUI off/on toggle dark souls network mode, to make easier as possible use mods without being banned. Just start the app, browse to .exe, toggle the option and boom! easy!.

## Software GUI
![dark-souls-GUI](https://cdn.discordapp.com/attachments/524370625167491073/1212997510541344798/Capture1.PNG?ex=65f3def6&is=65e169f6&hm=35af611f6ee9a80613837a9f8e2c6af4c9277c1da851822f04f732dd728b8bba&)
![dark-souls-GUI](https://cdn.discordapp.com/attachments/524370625167491073/1212997510868762674/Capture2.PNG?ex=65f3def6&is=65e169f6&hm=9a816ff68bd2fbae778d4376c5d119973ec0fe319fd5b4e470eaee947325fc2e&)
![dark-souls-GUI](https://cdn.discordapp.com/attachments/524370625167491073/1212997511245996113/Capture3.PNG?ex=65f3def7&is=65e169f7&hm=81fe3093399ceba1eece5dffbd1ba946e535007a60f9d1b951e4a369f069373a&)


## What I used to make it 📑
- **Code editor:** VSCODE
- **Language:** Python
- **Library:** customtkinter, subprocess, sys, ctypes and nuitka to make it .exe

## Logo or Icon 🎨
![dark-souls-logo](https://cdn.discordapp.com/attachments/524370625167491073/1212868773883809852/icon.png?ex=65f36711&is=65e0f211&hm=4217b642fb61fc27fe7fff3622610a77eb3292dcd7401cba5067f074c751696a&)

## IMPORTANT!
To use, execute as administrator!
Why: cuz the software create a rule on firewall to make ds2.exe offline, and this require elevated privileges.

Another important note is: microsoft windows defender detects as a virus, false positive, cuz its was python file thats is now compiled to .exe.
I already submitted to microsoft that is a false positive, so maybe in four weeks (march 15) it will be solved, for now, just allow it on windows defender.

## How it works?
By now, u can just read the code and understand by ursef. But its basically some functions to check if a rule in firewall by name "Block Dark Souls" exists, if not, the status (if file founded) will be ONLINE (if rule not exists) and OFFLINE (if rule exists). The are three buttons, one to browse through game executable if its not on default steam installation folder, and both other to make it online and offline.
