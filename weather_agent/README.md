# Weather Agent

A command-line weather agent that uses Gemini through its OpenAI-compatible API and retrieves current conditions from wttr.in.

## Requirements

- Python 3.10 or later
- A Gemini API key

## Setup (Windows PowerShell)

From this folder, create and activate a virtual environment, then install the dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Create a `.env` file in this folder and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Do not commit `.env` or share your API key.

## Run

```powershell
python main.py
```

Enter a weather question when prompted, for example: `What is the weather in Delhi?`
