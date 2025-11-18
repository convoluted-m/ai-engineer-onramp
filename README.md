# OpenAI Chat Agent

Interactive command-line chat agent using OpenAI's API.

## Requirements

- Python 3.12.5+
- OpenAI API key
- pipenv

## Installation

1. Install dependencies:
   pipenv install

2. Create `.env` file with your API key:

## Usage

```bash
pipenv run python app.py
```

Type your questions and press Enter. Type `quit`, `exit`, or `q` to stop.

## Configuration

Default settings in `app.py`:

- Model: `gpt-4o-mini`
- Temperature: `0.7`
- Max Tokens: `200`
