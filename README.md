# Voice-Assistant
This Python voice assistant script continuously listens to the user's speech, converts it to text, and prints the recognized words. It uses the `speech_recognition` library and the Google Web Speech API for accurate speech recognition. The assistant adjusts for ambient noise and handles various errors, ensuring smooth operation. Users can stop the assistant by saying "exit." This simple yet effective script demonstrates the basics of creating a voice-activated assistant in Python.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Voice Commands](#voice-commands)
- [File Structure](#file-structure)
- [Contributing](#contributing)

## Features

Sure! Here are the features of the voice assistant in 5 points:

1. **Continuous Listening**: The assistant continuously listens for the user's speech until the "exit" command is given.
2. **Speech Recognition**: Utilizes the Google Web Speech API for accurate speech-to-text conversion.
3. **Ambient Noise Adjustment**: Adjusts for ambient noise to improve recognition accuracy.
4. **Error Handling**: Manages various errors, including timeouts, unrecognized speech, and API request failures.
5. **Voice Command Exit**: Allows the user to stop the assistant by saying "exit."

## Installation

1. **Clone the Repository**
    ```sh
    git clone https://github.com/Vishal2023c/Voice-Assistant-.git
    cd Voice-Assistant
    ```

2. **Create a Virtual Environment**
    ```sh
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    ```

3. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Application**
    ```sh
    streamlit run voice_assistant.py
    ```

2. **Interact with the Application**
    - Open a browser and navigate to the provided local URL (e.g., `http://localhost:8501`).
    - test voice assistant say any word .
  
## exit Commands
   say exit
## File Structure
Voice-Assistant/
    │
    ├── .gitignore
    ├── voice_assistant.py
    ├── README.md
    ├── requirements.txt
  
  
