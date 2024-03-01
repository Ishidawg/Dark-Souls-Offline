import subprocess # to use firewall commands and find executable
import sys # to kill software if user wants to
import ctypes # to start with admin (make firewall changes possible)

from customtkinter import * # GUI   
import customtkinter

def isAdmin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def runAsAdmin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "".join(sys.argv), None, 1)

def ifNotAdminCheck(): # function to not repeat code like shit
    if not isAdmin():
        runAsAdmin()
        sys.exit()

def findDarkSouls():
    paths = [
        os.path.join(os.getenv("ProgramFiles"), "Steam", "steamapps", "common", "Dark Souls II Scholar of the First Sin", "Game", "DarkSoulsII.exe"),
        os.path.join(os.getenv("ProgramFiles(x86)"), "Steam", "steamapps", "common", "Dark Souls II Scholar of the First Sin", "Game", "DarkSoulsII.exe"),
        os.path.join(os.getenv("ProgramFiles(x86)"), "Steam", "steamapps", "common", "Dark Souls II Scholar of the First Sin", "Game", "DarkSoulsII.exe"),
    ]

    for path in paths:
        if os.path.isfile(path):
            return path

    return None

darkSoulsExe = findDarkSouls()

def selectfile():
    global darkSoulsExe
    filename = filedialog.askopenfilename()
    filenameFormated = filename.replace("/", '\\')
    fileFinalPath = filenameFormated.split('//')[-1]

    print(fileFinalPath)

    if darkSoulsExe:
        darkSoulsExe = findDarkSouls()
        pathLabel.configure(text="Dark Souls II founded on system!", text_color="#559854")
        print("Automatic")
    else:
        darkSoulsExe = filenameFormated
        pathLabel.configure(text="Dark Souls II found manually", text_color="#559854")
        pathLabel.place(x = 158, y = 128)
        
        if checkOutboundRuleExists(toCheck):
            status.configure(text="Status: Your game is OFFLINE!", text_color="#D13737")
            status.pack(padx = 10, pady = 10)
            status.place(y=230, x = 88)
        else:
            status.configure(text="Status: Your game is ONLINE!", text_color="#559854")
            status.pack(padx = 10, pady = 10)
            status.place(y = 230, x = 88)


        print("Manual")

def checkOutboundRuleExists(ruleName):
    try:
        # Show firewall rules
        result = subprocess.run(['netsh', 'advfirewall', 'firewall', 'show', 'rule', 'name=' + ruleName], capture_output=True, text=True, check=True)
        
        # Check if rule exists
        return ruleName.lower() in result.stdout.lower()
    
    except subprocess.CalledProcessError:
        # Just in case netsh fails
        print("Error executing 'netsh' command.")
        return False

toCheck = 'BlockDarkSouls' # Rule Name

def blockInternetAccess(programPath):
    ifNotAdminCheck()

    try:
        programName = programPath.split('\\')[-1] # Get the program executable name by remove double slash

        # Add rule
        subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule',
                        'name="BlockDarkSouls"', 'dir=out', 'action=block',
                        'program=' + programPath, 'enable=yes'], check=True)

        print(f"Internet access for '{programName}' blocked successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error blocking internet access: {e}")

def allowInternetAccess(programPath):
    ifNotAdminCheck()

    try:
        programName = programPath.split('\\')[-1]
        
        subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule',
                        'name="BlockDarkSouls"', 'program=' + programPath], check=True)

        print(f"Internet access for '{programName}' allowed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error allowing internet access: {e}")

def disableConnection():
    ifNotAdminCheck()

    #toBlock = 'C:\\Program Files (x86)\\Steam\\steam.exe' test
    toBlock = darkSoulsExe
    blockInternetAccess(toBlock)
    
    status.configure(text="Status: Your game is OFFLINE!", text_color="#D13737")

def enableConnection():
    ifNotAdminCheck()

    #toAllow = 'C:\\Program Files (x86)\\Steam\\steam.exe' test
    toAllow = darkSoulsExe
    allowInternetAccess(toAllow)

    status.configure(text="Status: Your game is ONLINE!", text_color="#559854")

# GUI
app = CTk()
app.title("Dark Souls Offline")
app.geometry("450x280")
app.resizable(False, False)
app.iconbitmap("icon.ico")

# Theme
customtkinter.set_appearance_mode("Dark")
#customtkinter.set_default_color_theme("custom.json")

#font
bigFont = customtkinter.CTkFont(size=20)
smallFont = customtkinter.CTkFont(size=16)
superTinyFont = customtkinter.CTkFont(size=10)

labelOne = CTkLabel(
    app, 
    text="Select your",
    font=bigFont,
    text_color="#E7EAEE",
    compound="left")
labelOne.pack(padx = 2, pady = 2)
labelOne.place(x = 100, y = 30)

labelTwo = CTkLabel(
    app, 
    text="DarkSoulsII.exe",
    font=bigFont,
    text_color="#559854")
labelTwo.pack(padx = 2, pady = 2)
labelTwo.place(x = 208, y = 30)

browseButton = CTkButton(app,
    text = "Browse",
    font=smallFont,
    command = selectfile)
browseButton.pack(padx = 25, pady = 25)
browseButton.place(y = 100, x = 150)

onlineButton = CTkButton(
    app, 
    text="Make it online",
    font=smallFont, 
    command=enableConnection)
onlineButton.pack(padx = 25, pady = 25)
onlineButton.place(y = 198, x = 68)

offlineButton = CTkButton(
    app, 
    text="Make it offline",
    font=smallFont,
    command=disableConnection)
offlineButton.pack(padx = 25, pady = 25)
offlineButton.place(y = 198, x = 235)

if darkSoulsExe:
    if checkOutboundRuleExists(toCheck):
        status = CTkLabel(
            app, 
            text="Status: Your game is OFFLINE!",
            font=bigFont,
            text_color="#D13737")
        status.pack(padx = 10, pady = 10)
        status.place(y=230, x = 60)
    else:
        status = CTkLabel(
            app, 
            text="Status: Your game is ONLINE!",
            font=bigFont,
            text_color="#559854")
        status.pack(padx = 10, pady = 10)
        status.place(y = 230, x = 88)

    print(f"Steam executable found at: {darkSoulsExe}")
    pathLabel = CTkLabel(
        app, 
        text="Dark Souls II founded on system!",
        font=superTinyFont,
        text_color="#559854")
    pathLabel.pack(padx = 2, pady = 2)
    pathLabel.place(x = 148, y = 128)
else:
    print("Steam executable not found.")
    pathLabel = CTkLabel(
        app, 
        text="Dark Souls II not found on system! Use browse button",
        font=superTinyFont,
        text_color="#D13737")
    pathLabel.pack(padx = 2, pady = 2)
    pathLabel.place(x = 108, y = 128)

    status = CTkLabel(
        app, 
        text="Status: NONE!",
        font=bigFont,
        text_color="#717274")
    status.pack(padx = 10, pady = 10)
    status.place(x = 155, y = 230)

    

#if checkOutboundRuleExists(toCheck):
#    status = CTkLabel(
#    app, 
#    text="Status: Your game is OFFLINE!",
#    font=bigFont,
#    text_color="#D13737")
#    status.pack(padx = 10, pady = 10)
#    status.place(y=230, x = 60)
# else:
#    status = CTkLabel(
#    app, 
#    text="Status: Your game is ONLINE!",
#    font=bigFont,
#    text_color="#559854")
#    status.pack(padx = 10, pady = 10)
#    status.place(y = 230, x = 60)

app.mainloop()
