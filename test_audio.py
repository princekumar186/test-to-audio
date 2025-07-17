import pyttsx3

def text_to_audio(text, output_file):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Save the audio to a file
    engine.save_to_file(text, output_file)

    # Run the engine in the background
    engine.runAndWait()

# Example usage
text = '''Good moring, how are you, I thiank you are good. I am Prince roy form bhabhua kaimur. I am present hear for some urgent project, this project is related to hacking.
And i am sure you know this, you know hacker main three types,
first is what hat hacker.
second is black hat hacker.
third is gray hat hacker.

'''
output_file = "hack2.mp3"

text_to_audio(text, output_file)