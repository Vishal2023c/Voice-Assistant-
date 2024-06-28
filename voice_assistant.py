import streamlit as st
import pandas as pd
import speech_recognition as sr

def listen_and_recognize():
    # Initialize recognizer class (for recognizing the speech)
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        # Adjust the recognizer sensitivity to ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1)
        st.write("Voice Assistant is now listening... (say 'exit' to stop)")

        while True:
            st.write("Listening...")
            try:
                # Capture the audio from the microphone
                audio = recognizer.listen(source, timeout=5)
                # Recognize speech using Google Web Speech API
                st.write("Recognizing...")
                text = recognizer.recognize_google(audio)
                st.write(f"You said: {text}")

                # Save the recognized text to a file
                with open("recognized_text.txt", "a") as file:
                   file.write(text + "\n")
                # for x in data :
                #     st.write(x)
                    # st.write(pd.DataFrame({x}))
                if text.lower() == "exit":
                    st.write("Exiting voice assistant. Goodbye!")
                    break

            except sr.WaitTimeoutError:
                st.write("Listening timed out while waiting for phrase to start")
            except sr.UnknownValueError:
                st.write("Sorry, I could not understand the audio.")
            except sr.RequestError as e:
                st.write(f"Could not request results from Google Web Speech API; {e}")

if __name__ == "__main__":
    listen_and_recognize()

