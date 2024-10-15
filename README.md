# WordGuesserWeb 
## Flask-based word-guessing game

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/LoVaKo/WordGuesserWeb.git
    ```
2. Navigate into the project directory:
   ```bash
   cd WordGuesserWeb
   ```
3. Install and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the app:
   ```bash
   python3 app.py
   ```
5. Open your browser and go to http://127.0.0.1:5000/
6. Enjoy!

### Features 
- 5 difficulty levels
- 10 rounds per game
- Highscore system

### Technologies used
- Python
- HTML/CSS
- Flask
- Redis

### File Structure
- `app.py` is the main application file
- `requirements.txt` project dependencies
- `controllers\` holds extra python files for game logic, highscore mechanisms etc.
- `data\` holds the json file with highscore data
- `static\` holds the CSS file
- `templates\` holds the html files
