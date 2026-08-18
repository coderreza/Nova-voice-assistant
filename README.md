# Nova-voice-assistant
This is a voice assistant called Nova made by codderreza(me).
| Feature | Description |
|---------|-------------|
| 🗣️ **Voice Recognition** | Offline speech recognition using Vosk |
| 📁 **File Management** | Open and delete files with voice commands |
| 🚀 **App Launcher** | Launch 100+ applications |
| 🔍 **Web Search** | Google search integration |
| 📂 **Navigation** | Navigate directories |
| ✍️ **Voice Typing** | Type text with voice commands |
| 💬 **Text-to-Speech** | Voice feedback using pyttsx3 |
| 🎯 **Greetings** | Recognizes hello, goodbye, thank you |
_______________________________________________________________________________
## 🛠️ Technologies Used

- **Python 3.11+** - Core programming language
- **Vosk** - Offline speech recognition
- **PyAudio** - Microphone input
- **pyttsx3** - Text-to-speech
- **PyAutoGUI** - Voice typing/automation
- **JSON** - Command parsing
- ________________________________________________________________________________
- NOVA requires a Vosk speech recognition model to work offline. Download the small English model:

Download Link: https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip

Or browse all models here: https://alphacephei.com/vosk/models
nova-voice-assistant/
├── main.py
├── vosk-model-small-en-us-0.15/   <-- Put it here
__________________________________________________________________________________
markdown
## 🎯 How to Use NOVA

### Basic Usage

1. **Run the program:**
   ```bash
   python main.py
Wait for the "Listening..." message and speak clearly into your microphone.

Use voice commands to control your computer.

📝 Command Examples
Opening Files
text
"open file mydocument"     → Opens mydocument.txt, mydocument.docx, etc.
"open file report dot pdf" → Opens report.pdf
Deleting Files
text
"delete file mydocument"   → Deletes mydocument.txt, mydocument.docx, etc.
"delete file image dot png" → Deletes image.png
Launching Apps
text
"open spotify"             → Opens Spotify
"open chrome"              → Opens Google Chrome
"open vscode"              → Opens VS Code
"open notepad"             → Opens Notepad
"open calculator"          → Opens Calculator
Searching the Web
text
"search python tutorial"   → Opens Google search for "python tutorial"
"search cute cats"         → Searches Google for "cute cats"
Navigating Folders
text
"go to downloads"          → Navigates to Downloads folder
"go to documents"          → Navigates to Documents folder
"show files"               → Lists all files in current folder
"go back"                  → Goes to parent folder
"where am i"               → Shows current folder path
Voice Typing
text
"write hello world"        → Types "hello world" at cursor position
"write I love Python"      → Types "I love Python"
Conversations
text
"hello"                    → NOVA responds "hi there"
"thank you"                → NOVA responds "you're welcome"
"who are you"              → NOVA introduces itself
"goodbye"                  → Exits the program
💡 Tips for Best Results
Speak clearly - NOVA uses offline speech recognition, so clear speech works best.

Use the right format:

For files with extensions: Say "open file document dot pdf"

For files without extensions: Say "open file mydocument" (NOVA will find any matching file)

Wait for the response - NOVA will speak back after each command.

Press Ctrl+C or say "goodbye" to stop NOVA at any time.
