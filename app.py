import time
import random

import gradio as gr


def generate_music(song_name, description, genre):
    # Simulate a delay of 10 to 20 seconds
    delay = random.randint(10, 20)
    time.sleep(delay)
    # Return a fixed MP3 file
    return "ai_output.mp3"


demo = gr.Interface(
    fn=generate_music,
    inputs=[
        gr.Textbox(label="Song Name"),
        gr.Textbox(label="Music Description"),
        gr.Textbox(label="Music Genre")
    ],
    outputs=gr.Audio(label="Generated Music"),
    title="Rhythmic Intelligent Composition Kit",
    allow_flagging="never",
)

if __name__ == "__main__":
    demo.launch()