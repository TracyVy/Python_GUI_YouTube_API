
from tkinter import *
from googleapiclient.discovery import build
import json
import traceback

api_key = 'AIzaSyBaJMheuIniSippMYMj-xPF0lsZOKDBsrw'

youtube = build('youtube', 'v3', developerKey=api_key)

# Simple Ui


def click():
    entered_text = textentry.get()
    output.delete(0.0, END)
    msg = ""
    try:
        # Get the Youtube username from textfield
        youtube_username = entered_text
        print(youtube_username)

        # Call the google api to get the youtube
        request = youtube.channels().list(
            part='statistics',
            forUsername=youtube_username
        )
        response = request.execute()

        # Store json string in tmp variables
        json_str = response

        # Parse json object to get subscriber count
        tmp = json_str["items"][0]["statistics"]["subscriberCount"]
        print(tmp)
        msg = (f"This YouTube channel has {tmp} subscribers.")
        # print(json_str["statistics"])
    except:
        traceback.print_exc()

        msg = "Sorry, either that Username does not exist or you may have entered the Display Name."

    output.insert(END, msg)


# main:
window = Tk()
window.title("YouTube Subscribers Lookup")
window.configure(background="#233067")

# create label
Label(window, text="\nEnter the YouTube's channel username, NOT the display name.", bg="#233067", fg="white",
      font="none 12 bold") .grid(row=1, column=0, sticky=W)

# create user input field
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

# add a submit button
Button(window, text="SUBMIT", width=6, command=click) .grid(
    row=3, column=0, sticky=W)

# create a textbox for output
output = Text(window, width=50, height=6,
              wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

# run the main loop
window.mainloop()
