# pip install speechrecognition to recognise what we speak using python
# pip install wikipedia to help import data from wikipedia
# pip install openai for using its api for ai
# Now importing

import openai
import speech_recognition as sr
import win32com.client
import webbrowser
import pygame
import os
from config import apikey
import datetime
import random

def ai(prompt):
    openai.api_key = apikey
    text= f"OpenAI response for Prompt: {prompt} \n ***********************\n\n"

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/prompt- {random.randint(1,2343434334)}","w") as f:
        f.write(text)

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis."

# main
speaker.Speak("Hello, I am Jarvis A.I. How may I help you?")


# Define a list of songs with their paths
# todo : Add a feature to play a specific song and also add more songs to the list of songs
songs = [
    {"title": "Save Your Tears - The Weeknd", "path": r"C:\Users\sanya\Downloads\Save Your Tears - The Weeknd(PagalWorld).mp3"},
    {"title": "Let Her Go - Passenger", "path": r"C:\Users\sanya\Downloads\Let Her Go - Passenger 320(PagalWorld).mp3"},
    {"title": "Your Eyes Got My Heart", "path": r"C:\Users\sanya\Downloads\Your Eyes Got My Heart Barney Sku_320(PagalWorld).mp3"}
]

pygame.init()
pygame.mixer.init()
playing = False
current_song_index = 0  # Index to track the currently playing song
volume_level = 5


while True:
    print("Listening...")
    query = takeCommand()
    # todo : Add more sites
    sites = [
        ["google", "https://www.google.com"],
        ["youtube", "https://www.youtube.com"],
        ["wikipedia", "https://www.wikipedia.com"],
        ["gmail", "https://www.gmail.com"]
    ]

    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            statement = f"Opening {site[0]} sir..."
            speaker.Speak(statement)
            webbrowser.open(site[1])

    if "play music" in query:
        if not playing:
            pygame.mixer.music.load(songs[current_song_index]["path"])
            pygame.mixer.music.play()
            playing = True
            speaker.Speak(f"Playing {songs[current_song_index]['title']}.")
        else:
            speaker.Speak("Music is already playing.")

    elif "pause music" in query:
        if playing:
            pygame.mixer.music.pause()
            playing = False
            speaker.Speak("Music paused.")
        else:
            speaker.Speak("No music is currently playing.")

    elif "resume music" in query:
        if not playing:
            pygame.mixer.music.unpause()
            playing = True
            speaker.Speak("Music resumed.")
        else:
            speaker.Speak("Music is already playing.")

    elif "stop music" in query:
        if playing:
            pygame.mixer.music.stop()
            playing = False
            speaker.Speak("Music stopped.")
        else:
            speaker.Speak("No music is currently playing.")

    elif "next song" in query:
        if playing:
            pygame.mixer.music.stop()
            playing = False
            current_song_index += 1
            if current_song_index >= len(songs):
                current_song_index = 0  # Loop back to the first song
            pygame.mixer.music.load(songs[current_song_index]["path"])
            pygame.mixer.music.play()
            playing = True
            speaker.Speak(f"Playing {songs[current_song_index]['title']}.")

    elif "volume" in query:
        # Parse the volume level from the query
        words = query.split()
        for i, word in enumerate(words):
            if word == "volume" and i + 1 < len(words):
                try:
                    new_volume = int(words[i + 1])
                    if 1 <= new_volume <= 10:
                        volume_level = new_volume
                        pygame.mixer.music.set_volume(volume_level / 10)  # Set volume (0.1 to 1.0)
                        speaker.Speak(f"Volume set to {volume_level}.")
                    else:
                        speaker.Speak("Please specify a volume between 1 and 10.")
                except ValueError:
                    speaker.Speak("Invalid volume level. Please specify a number between 1 and 10.")


    if "the time" in query:
            # **Fix:** Get the current time in the local time zone
            now = datetime.datetime.now()
            # Format the time as 12-hour clock with AM/PM
            strfTime = now.strftime("%I:%M %p")
            # Speak the time
            speaker.Speak(f"Sir, the time is {strfTime}")

    # todo : Add more apps to the list
    apps = [
        ["ms edge", "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"],
        ["git bash","C:\Program Files\Git\git-bash.exe"],
        ["steam", "C:\Program Files (x86)\Steam\steam.exe"],
        ["vscode", "C:\vs code\Microsoft VS Code\Code.exe"]
    ]

    for app in apps:
        if f"Open {app[0]}".lower() in query.lower():
            statement = f"Opening {app[0]} sir..."
            speaker.Speak(statement)
            webbrowser.open(app[1])


    if "Using artificial intelligence".lower() in query.lower():
          ai(prompt=query)









