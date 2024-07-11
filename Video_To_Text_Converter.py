import speech_recognition as sr
import moviepy.editor as me
# these are the libraries that helps us to convert video to text
# We need to specified, video_file, output_audio_file, and output_text_file where we store
#the files for this code

VIDEO_FILE = "www.mp4"
OUTPUT_AUDIO_FILE = "converter.wav"
OUTPUT_TEXT_FILE = "text.txt"

# The concept will be like this: the script will convert the mp4 file to a wav file, and from that
#file, it will output text file.

#Let's do that - Extracting audio from video
try:
video_clip = me.VideoFileClip(r"{}".format(VIDEO_FILE))

# The next thing we need to do is define the recognizer.

video_clip.audio.write_audiofile(r"{}".format(OUTPUT_AUDIO_FILE))
recognizer = sr.Recognizer()

# We need to import audio file for recognition

audio_clip = sr.AudioFile("{}".format(OUTPUT_AUDIO_FILE))

# we will start the conversion to text

with audio_clip as source:

audio_file = recognizer.record(source)
print("Please wait ...")
result = recognizer.recognize_google(audio_file)
with open(OUTPUT_TEXT_FILE, 'w') as file:
file.write(result)
print("Speech to text conversion successfull.")
except Exception as e:
print("Attempt failed -- ", e)

# For longer videos, WE can split audio data into chunks.