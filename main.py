from vosk import Model, KaldiRecognizer
import pyaudio
import json
import random
import os
import pyttsx3
import urllib.parse
import webbrowser
import pyautogui

goodbye_phrases = [
    # English
    "goodbye",
    "bye",
    "bye bye",
    "see you",
    "see you later",
    "see you soon",
    "see ya",
    "later",
    "catch you later",
    "talk to you later",
    "take care",
    "farewell",
    "so long",
    "adios",
    "peace out",
    "out",
    "i'm out",
    "gotta go",
    "got to go",
    "have to go",
    "i'm leaving",
    "leaving now",
    "shutting down",
    "exit",
    "quit",
    "stop",
    "end",
    "finish",
    "done",
    "over and out",
    "until next time",
    "til next time",
    "stay safe",
    "have a good day",
    "have a nice day",
    "good night",
    "see you tomorrow",
    "bye for now",
    "ciao",
    "hasta luego",
    "au revoir",
    "bon voyage",
    "goodbye world",
    "signing off",
    "logging off",
    "system off",
    "power down",
    
    # Funny/Informal
    "peace",
    "smell you later",
    "catch you on the flip side",
    "later gator",
    "take it easy",
    "chill out",
    "live long and prosper",
    "may the force be with you",
    "until we meet again",
    "party on",
    "rock on",
    "keep it real",
    "later skater",
    "bye felicia",
]
filler_words = [
    # Basic fillers
    "um",
    "uh",
    "er",
    "ah",
    "hmm",
    "like",
    "you know",
    "i mean",
    "actually",
    "basically",
    "literally",
    "seriously",
    "honestly",
    "frankly",
    "essentially",
    "virtually",
    "practically",
    "obviously",
    "clearly",
    "definitely",
    "absolutely",
    "totally",
    "completely",
    "really",
    "very",
    "quite",
    "just",
    "so",
    "well",
    "now",
    "then",
    "thus",
    "hence",
    "accordingly",
    "consequently",
    "accordingly",
    "additionally",
    "again",
    "almost",
    "also",
    "anyway",
    "approximately",
    "as",
    "as well",
    "at all",
    "at least",
    "at the end of the day",
    "basically",
    "because",
    "being",
    "believe me",
    "by the way",
    "certainly",
    "clearly",
    "completely",
    "consequently",
    "definitely",
    "due to",
    "during",
    "even",
    "eventually",
    "ever",
    "every",
    "everyone",
    "everything",
    "exactly",
    "fairly",
    "finally",
    "first",
    "for",
    "for example",
    "for instance",
    "frankly",
    "generally",
    "given",
    "great",
    "hence",
    "honestly",
    "however",
    "i guess",
    "i suppose",
    "i think",
    "in addition",
    "in case",
    "in fact",
    "in general",
    "in my opinion",
    "in other words",
    "in particular",
    "in short",
    "in summary",
    "in the meantime",
    "in the process",
    "in the same way",
    "in total",
    "incredibly",
    "indeed",
    "interestingly",
    "incredibly",
    "just",
    "kind of",
    "largely",
    "literally",
    "mainly",
    "maybe",
    "meanwhile",
    "moreover",
    "mostly",
    "namely",
    "naturally",
    "nevertheless",
    "next",
    "nonetheless",
    "notably",
    "now",
    "obviously",
    "of course",
    "on the other hand",
    "otherwise",
    "overall",
    "particularly",
    "perhaps",
    "plainly",
    "plus",
    "precisely",
    "previously",
    "primarily",
    "practically",
    "probably",
    "quite",
    "rather",
    "really",
    "regarding",
    "relatively",
    "respectively",
    "seriously",
    "significantly",
    "similarly",
    "simply",
    "since",
    "so",
    "so to speak",
    "specifically",
    "still",
    "strictly",
    "subsequently",
    "substantially",
    "such",
    "sure",
    "thankfully",
    "then",
    "thereafter",
    "thereby",
    "therefore",
    "thus",
    "to be honest",
    "to be sure",
    "to put it bluntly",
    "to some extent",
    "totally",
    "truly",
    "ultimately",
    "understandably",
    "undoubtedly",
    "unfortunately",
    "unsurprisingly",
    "usually",
    "very",
    "virtually",
    "well",
    "who knows",
    "without a doubt",
    "y'know",
    "you see",
    
    # Conversation fillers
    "actually",
    "alright",
    "anyway",
    "basically",
    "believe me",
    "by the way",
    "frankly",
    "honestly",
    "i guess",
    "i mean",
    "i suppose",
    "i think",
    "if you will",
    "in a manner of speaking",
    "in my view",
    "in reality",
    "in truth",
    "it seems",
    "kind of",
    "let's see",
    "like",
    "look",
    "mind you",
    "more or less",
    "now",
    "okay",
    "right",
    "see",
    "so",
    "sort of",
    "to tell the truth",
    "well",
    "you know",
    "you see",
    
    # Transition fillers
    "additionally",
    "again",
    "also",
    "besides",
    "consequently",
    "finally",
    "firstly",
    "furthermore",
    "however",
    "in addition",
    "in conclusion",
    "in summary",
    "indeed",
    "lastly",
    "likewise",
    "meanwhile",
    "moreover",
    "nevertheless",
    "next",
    "nonetheless",
    "otherwise",
    "overall",
    "secondly",
    "similarly",
    "subsequently",
    "then",
    "therefore",
    "thus",
    
    # Qualifiers (weaken statements)
    "almost",
    "apparently",
    "approximately",
    "arguably",
    "basically",
    "essentially",
    "fairly",
    "generally",
    "largely",
    "mainly",
    "mostly",
    "partially",
    "practically",
    "presumably",
    "probably",
    "relatively",
    "somewhat",
    "virtually",
    
    # Extra fillers
    "blah",
    "blah blah",
    "etc",
    "et cetera",
    "stuff",
    "things",
    "whatever",
    "whatnot",
    "yeah",
    "nah",
    "ok",
    "okay",
    "k",
    "mm",
    "okie",
    "yep",
    "yup",
    "nope",
    "uh huh",
    "uh uh",
    "huh",
    "eh",
]
hello_phrases = [
    # English
    "hello",
    "hi",
    "hey",
    "hey there",
    "hi there",
    "hello there",
    "greetings",
    "good day",
    "good morning",
    "good afternoon",
    "good evening",
    "what's up",
    "sup",
    "yo",
    "howdy",
    "howdy partner",
    "what's good",
    "welcome",
    "hello world",
    "hey you",
    "hiya",
    "how are you",
    "how are you doing",
    "nice to see you",
    "good to see you",
    "pleasure to meet you",
    "it's me",
    "your assistant",
    "jarvis here",
    "ready to help",
    "listening",
    "i'm listening",
    "what can i do for you",
    "how can i help",
    "help you",
    "at your service",
    
    # Foreign
    "hola",
    "bonjour",
    "salut",
    "hallo",
    "ciao",
    "aloha",
    "namaste",
    "konnichiwa",
    "salaam",
    "shalom",
    "marhaba",
    "sawubona",
    "kaixo",
    "halo",
    "merhaba",
    "olá",
    
    # Informal/Slang
    "hey man",
    "hey girl",
    "hey buddy",
    "hey pal",
    "hey friend",
    "what it do",
    "how goes it",
    "what's happening",
    "how's it going",
    "how's life",
    "long time no see",
    "what's new",
    "what's cooking",
    "what's shaking",
    "how's everything",
    "how's things",
    
    # Wake/Activation
    "wake up",
    "wakey wakey",
    "rise and shine",
    "are you there",
    "you there",
    "hey computer",
    "hey assistant",
    "hello assistant",
    "okay jarvis",
    "hey jarvis",
    "jarvis",
]
didnt_undr = ["couldn't hear that", "sorry can you repeat it", "sorry, couldn't understand", "pardon me"]
all_file_formats = [
    # Document & Text Files
    '.doc', '.docx', '.odt', '.pdf', '.rtf', '.txt', '.wpd',
    '.csv', '.xls', '.xlsx', '.ods',
    '.ppt', '.pptx', '.odp',
    '.htm', '.html', '.xml', '.md',
    
    # Image & Graphics Files
    '.bmp', '.gif', '.jpg', '.jpeg', '.png', '.tif', '.tiff', '.webp',
    '.svg', '.ai', '.eps', '.psd',
    
    # Audio Files
    '.aif', '.aiff', '.flac', '.mp3', '.wav', '.wma', '.aac', '.ogg',
    
    # Video Files
    '.avi', '.mov', '.qt', '.mp4', '.mpeg', '.mpg', '.wmv', '.flv', '.mkv', '.webm',
    
    # Compressed & Archive Files
    '.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.iso',
    
    # Executable & System Files
    '.exe', '.msi', '.bat', '.cmd', '.sh', '.bash', '.app', '.dmg',
    '.dll', '.sys', '.ini', '.cfg', '.conf',
    
    # Programming & Code Files
    '.py', '.js', '.java', '.c', '.cpp', '.h', '.cs', '.rb', '.go', '.rs',
    '.php', '.swift', '.kt', '.ts', '.json', '.yaml', '.yml',
    
    # Database Files
    '.db', '.sqlite', '.sql', '.mdb', '.accdb',
    
    # Font Files
    '.ttf', '.otf', '.woff', '.woff2',
    
    # 3D & CAD Files
    '.stl', '.obj', '.fbx', '.dwg', '.dxf', '.blend', '.3ds',
    
    # Design & Publishing Files
    '.indd', '.pub', '.qxp',
    
    # E-book Files
    '.epub', '.mobi', '.azw', '.azw3',
    
    # Disk Image Files
    '.iso', '.img', '.dmg',
    
    # Backup Files
    '.bak', '.backup', '.tmp',
    
    # Miscellaneous
    '.log', '.dat', '.key', '.pem', '.crt', '.cer',
    '.lic', '.reg', '.torrent', '.part'
]
thankyou_phrases = [
    # English
    "thank you",
    "thanks",
    "thanks a lot",
    "thank you very much",
    "thank you so much",
    "many thanks",
    "thanks a bunch",
    "much appreciated",
    "appreciate it",
    "i appreciate you",
    "you're the best",
    "you're amazing",
    "you're awesome",
    "you rock",
    "you rule",
    "big thanks",
    "huge thanks",
    "thank you kindly",
    "thanks a million",
    "thanks in advance",
    "thanks for your help",
    "grateful",
    "i'm grateful",
    "i owe you one",
    "cheers",
    "ta",
    "gracias",
    
    # Foreign
    "gracias",
    "merci",
    "danke",
    "arigato",
    "domo arigato",
    "shukran",
    "muito obrigado",
    "takk",
    "kiitos",
    "salamat",
    "dhanyavad",
    "bedankt",
    "efharisto",
    "dakujem",
    "hvala",
    "tak",
    
    # Informal
    "thanks man",
    "thanks bro",
    "thanks sis",
    "thanks buddy",
    "thanks friend",
    "appreciate it man",
    "you're a lifesaver",
    "saved my day",
    "you came through",
    "you're a star",
    "good looking out",
    "props to you",
    "hats off to you",
    "you deserve a medal",
    "you're the goat",
    "not all heroes wear capes",
    "legend",
    "my hero",
    "you're a legend",
    "appreciate you",
]
import os

# Get username from environment variable
username = os.getenv("USERNAME")  # Windows

app_paths = {
    # ===== WINDOWS BUILT-IN APPS =====
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "cmd": "cmd.exe",
    "powershell": "powershell.exe",
    "explorer": "explorer.exe",
    "taskmanager": "taskmgr.exe",
    "controlpanel": "control.exe",
    "settings": "ms-settings:",
    "snippingtool": "SnippingTool.exe",
    "wordpad": "write.exe",
    "character map": "charmap.exe",
    "disk cleanup": "cleanmgr.exe",
    "defragment": "dfrgui.exe",
    "systeminfo": "systeminfo.exe",
    "resource monitor": "resmon.exe",
    "performance monitor": "perfmon.exe",
    "services": "services.msc",
    "computer management": "compmgmt.msc",
    "device manager": "devmgmt.msc",
    "disk management": "diskmgmt.msc",
    "event viewer": "eventvwr.msc",
    "task scheduler": "taskschd.msc",
    "registry editor": "regedit.exe",
    "group policy": "gpedit.msc",
    "system configuration": "msconfig.exe",
    "remote desktop": "mstsc.exe",
    "magnifier": "magnify.exe",
    "on screen keyboard": "osk.exe",
    "steps recorder": "psr.exe",
    "math input panel": "mip.exe",
    "print management": "printmanagement.msc",
    "windows firewall": "firewall.cpl",
    "internet options": "inetcpl.cpl",
    "mouse properties": "main.cpl",
    "sound": "mmsys.cpl",
    
    # ===== MICROSOFT OFFICE =====
    "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
    "powerpoint": r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE",
    "outlook": r"C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE",
    "access": r"C:\Program Files\Microsoft Office\root\Office16\MSACCESS.EXE",
    "publisher": r"C:\Program Files\Microsoft Office\root\Office16\MSPUB.EXE",
    "onenote": r"C:\Program Files\Microsoft Office\root\Office16\ONENOTE.EXE",
    "teams": rf"C:\Users\{username}\AppData\Local\Microsoft\Teams\Update.exe",
    "skype": r"C:\Program Files\Microsoft Office\root\Office16\SKYPE.EXE",
    "office": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    
    # ===== WEB BROWSERS =====
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "firefox": r"C:\Program Files\Mozilla Firefox\firefox.exe",
    "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "opera": r"C:\Program Files\Opera\launcher.exe",
    "brave": r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
    "vivaldi": r"C:\Program Files\Vivaldi\Application\vivaldi.exe",
    "tor": r"C:\Program Files\Tor Browser\Browser\firefox.exe",
    
    # ===== CODE EDITORS & IDES =====
    "vscode": rf"C:\Users\{username}\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "code": rf"C:\Users\{username}\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "visual studio": r"C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\devenv.exe",
    "pycharm": r"C:\Program Files\JetBrains\PyCharm Community Edition 2023.1\bin\pycharm64.exe",
    "intellij": r"C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2023.1\bin\idea64.exe",
    "webstorm": r"C:\Program Files\JetBrains\WebStorm 2023.1\bin\webstorm64.exe",
    "phpstorm": r"C:\Program Files\JetBrains\PhpStorm 2023.1\bin\phpstorm64.exe",
    "sublime": r"C:\Program Files\Sublime Text\sublime_text.exe",
    "atom": rf"C:\Users\{username}\AppData\Local\atom\atom.exe",
    "notepad++": r"C:\Program Files\Notepad++\notepad++.exe",
    "vim": r"C:\Program Files\Vim\vim90\gvim.exe",
    "emacs": r"C:\Program Files\Emacs\emacs-28.2\bin\runemacs.exe",
    "git": r"C:\Program Files\Git\git-bash.exe",
    "github desktop": rf"C:\Users\{username}\AppData\Local\GitHubDesktop\GitHubDesktop.exe",
    "postman": rf"C:\Users\{username}\AppData\Local\Postman\Postman.exe",
    "insomnia": r"C:\Program Files\Insomnia\Insomnia.exe",
    
    # ===== MEDIA & ENTERTAINMENT =====
    "spotify": rf"C:\Users\{username}\AppData\Local\Spotify\Spotify.exe",
    "vlc": r"C:\Program Files\VideoLAN\VLC\vlc.exe",
    "media player": r"C:\Program Files\Windows Media Player\wmplayer.exe",
    "movies": "ms-video:",
    "photos": "ms-photos:",
    "itunes": r"C:\Program Files\iTunes\iTunes.exe",
    "winamp": r"C:\Program Files\Winamp\winamp.exe",
    "audacity": r"C:\Program Files\Audacity\Audacity.exe",
    "obs": r"C:\Program Files\obs-studio\bin\64bit\obs64.exe",
    "streamlabs": r"C:\Program Files\Streamlabs OBS\Streamlabs OBS.exe",
    "twitch": rf"C:\Users\{username}\AppData\Local\Twitch\Bin\Twitch.exe",
    
    # ===== GRAPHICS & DESIGN =====
    "photoshop": r"C:\Program Files\Adobe\Adobe Photoshop 2023\Photoshop.exe",
    "illustrator": r"C:\Program Files\Adobe\Adobe Illustrator 2023\Support Files\Contents\Windows\Illustrator.exe",
    "premiere": r"C:\Program Files\Adobe\Adobe Premiere Pro 2023\Adobe Premiere Pro.exe",
    "after effects": r"C:\Program Files\Adobe\Adobe After Effects 2023\Support Files\AfterFX.exe",
    "lightroom": r"C:\Program Files\Adobe\Adobe Lightroom Classic\Lightroom.exe",
    "gimp": r"C:\Program Files\GIMP 2\bin\gimp-2.10.exe",
    "inkscape": r"C:\Program Files\Inkscape\bin\inkscape.exe",
    "blender": r"C:\Program Files\Blender Foundation\Blender 3.6\blender.exe",
    "figma": rf"C:\Users\{username}\AppData\Local\Figma\Figma.exe",
    "canva": rf"C:\Users\{username}\AppData\Local\Canva\Canva.exe",
    
    # ===== COMMUNICATION =====
    "discord": rf"C:\Users\{username}\AppData\Local\Discord\Update.exe",
    "slack": rf"C:\Users\{username}\AppData\Local\slack\slack.exe",
    "telegram": rf"C:\Users\{username}\AppData\Local\Telegram Desktop\Telegram.exe",
    "whatsapp": rf"C:\Users\{username}\AppData\Local\WhatsApp\WhatsApp.exe",
    "zoom": rf"C:\Users\{username}\AppData\Roaming\Zoom\bin\Zoom.exe",
    "google meet": "https://meet.google.com/",
    "webex": r"C:\Program Files\Webex\Webex.exe",
    
    # ===== GAMING =====
    "steam": r"C:\Program Files (x86)\Steam\steam.exe",
    "epic games": r"C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win64\EpicGamesLauncher.exe",
    "riot": rf"C:\Users\{username}\AppData\Local\Riot Games\Riot Client\RiotClientServices.exe",
    "overwatch": r"C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe",
    "minecraft": r"C:\Program Files\Minecraft Launcher\MinecraftLauncher.exe",
    "roblox": r"C:\Program Files (x86)\Roblox\Versions\RobloxPlayerLauncher.exe",
    "unity": r"C:\Program Files\Unity\Hub\Editor\2022.3.0f1\Editor\Unity.exe",
    "unreal": r"C:\Program Files\Epic Games\UE_5.2\Engine\Binaries\Win64\UnrealEditor.exe",
    
    # ===== UTILITIES & SYSTEM =====
    "winrar": r"C:\Program Files\WinRAR\WinRAR.exe",
    "7zip": r"C:\Program Files\7-Zip\7zFM.exe",
    "utorrent": rf"C:\Users\{username}\AppData\Roaming\uTorrent\uTorrent.exe",
    "qbtorrent": r"C:\Program Files\qBittorrent\qbittorrent.exe",
    "ccleaner": r"C:\Program Files\CCleaner\CCleaner64.exe",
    "malwarebytes": r"C:\Program Files\Malwarebytes\Anti-Malware\mbam.exe",
    "norton": r"C:\Program Files\Norton Security\NortonSecurity.exe",
    "windows defender": r"C:\Program Files\Windows Defender\MSASCui.exe",
    "taskbar settings": "ms-settings:taskbar",
    "display settings": "ms-settings:display",
    "sound settings": "ms-settings:sound",
    "network settings": "ms-settings:network",
    "bluetooth settings": "ms-settings:bluetooth",
    "printer settings": "ms-settings:printers",
    "date and time": "timedate.cpl",
    "region": "intl.cpl",
    "power options": "powercfg.cpl",
    "network connections": "ncpa.cpl",
    "programs and features": "appwiz.cpl",
    "windows update": "ms-settings:windowsupdate",
    "system properties": "sysdm.cpl",
    
    # ===== PROGRAMMING TOOLS =====
    "node": r"C:\Program Files\nodejs\node.exe",
    "python": rf"C:\Users\{username}\AppData\Local\Programs\Python\Python311\python.exe",
    "anaconda": rf"C:\Users\{username}\anaconda3\python.exe",
    "jupyter": rf"C:\Users\{username}\anaconda3\Scripts\jupyter-notebook.exe",
    "docker": r"C:\Program Files\Docker\Docker\Docker Desktop.exe",
    "mysql": r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe",
    "postgres": r"C:\Program Files\PostgreSQL\15\bin\psql.exe",
    "mongodb": r"C:\Program Files\MongoDB\Server\6.0\bin\mongod.exe",
    "redis": r"C:\Program Files\Redis\redis-server.exe",
    
    # ===== MISCELLANEOUS =====
    "adobe reader": r"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe",
    "foxit": r"C:\Program Files\Foxit Software\Foxit Reader\FoxitReader.exe",
    "pdf": r"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe",
    "eclipse": r"C:\Program Files\Eclipse Foundation\eclipse\eclipse.exe",
    "xampp": r"C:\xampp\xampp-control.exe",
    "wampserver": r"C:\wamp64\wampmanager.exe",
    "virtualbox": r"C:\Program Files\Oracle\VirtualBox\VirtualBox.exe",
    "vmware": r"C:\Program Files (x86)\VMware\VMware Workstation\vmware.exe",
}
def say(text):
    """Speak text using pyttsx3"""
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"❌ TTS Error: {e}")
# Load model (download and extract a model first)
model = Model("vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

# Set up microphone
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1,
                rate=16000, input=True, frames_per_buffer=4000)

print("Listening... (Ctrl+C to stop)")

while True:
    try:
        data = stream.read(4000)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            command = (result["text"])
            commandstr = str(command)
            print(f"you: {commandstr}")
            if commandstr.startswith("open file "):
                filename = commandstr.replace("open file ", "")
                filename = filename.replace("dot",".")
                filename = filename.replace(" ","")
                for i in filler_words:
                    if i in filename:
                        filename = filename.replace(i, "")
                found = False
                for i in all_file_formats:
                    full_name = f"{filename}{i}"
                    if os.path.exists(full_name):
                        os.system(f"code {full_name}")
                        say("file opened")
                        found = True
                        break
                
                if not found:
                    print(f"❌ File not found: {filename}. so i created one")
                    say("file not found. so i created one")
                    os.system(f"code {filename}")
                
                                
                
            elif commandstr.startswith("delete file "):
                
                filename = commandstr.replace("delete file ", "")
                filename = filename.replace("dot",".")
                filename = filename.replace(" ","")
                for i in filler_words:
                    if i in filename:
                        filename = filename.replace(i, "")
                found = False
                for i in all_file_formats:
                    full_name = f"{filename}{i}"
                    if os.path.exists(full_name):
                        os.remove(f"{full_name}")
                        say("file deleted")
                        found = True
                        break
                            
                if not found:
                    say("file not found")
            elif commandstr.startswith("open "):
                
                appname = commandstr.replace("open ", "")
                appname = appname.replace("dot",".")
                appname = appname.replace(" ","")
                for i in filler_words:
                    if i in appname:
                        appname = appname.replace(i, "")
                if appname in app_paths.keys():
                    say(f"{appname} opened")
                    os.system(f'"{app_paths[appname]}"')
                    
            elif commandstr.startswith("go to "):
                dirname = commandstr.replace("go to ", "")
                dirname = dirname.replace("dot",".")
                dirname = dirname.replace(" ","")
                for i in filler_words:
                    if i in dirname:
                        dirname = dirname.replace(i, "")
                os.chdir(f"{os.getcwd()}\{dirname}")
                say("did it")
            elif commandstr == "show files":
                os.system("powershell ls")
                say("here they are")
            elif commandstr == "go back":
                os.chdir("..")
                say("did it")
            elif commandstr == "where am i":
                print(os.getcwd())
                say(f"you are at {os.getcwd()}")
            elif commandstr == "who are you":
                say("im a talking tool named Nova made by coderreza")
            elif commandstr == "":
                continue
            elif commandstr in hello_phrases:
                say("hi there")
            elif commandstr in goodbye_phrases:
                say("goodbye")
                exit()
            elif commandstr in thankyou_phrases:
                say("yourwelcome")
            elif commandstr.startswith("search "):
                wsearch = commandstr.replace("search ", "").strip()
                for i in filler_words:
                    if i in wsearch:
                        wsearch = wsearch.replace(i,"")
                encoded = urllib.parse.quote_plus(wsearch)
                url = f"https://www.google.com/search?q={encoded}"
                webbrowser.open(url)
                
                print(f"Searching: {wsearch}")
                say(f"searching for {wsearch}")
            elif commandstr.startswith("write "):
                text = commandstr.replace("write ", "")
                for i in filler_words:
                    if i in text:
                        text = text.replace(i, "")
                pyautogui.write(text)

    except KeyboardInterrupt:
        say("goodbye")
        exit()

                    



        


        