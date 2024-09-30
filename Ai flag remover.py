import tkinter as tk
from tkinter import scrolledtext
from nltk.corpus import wordnet
import random
import nltk

# Make sure to download the WordNet dataset the first time you run the script
nltk.download('wordnet')
nltk.download('omw-1.4')

# Function to find synonyms using WordNet
def find_synonym(word):
    synonyms = wordnet.synsets(word)
    if synonyms:
        lemmas = synonyms[0].lemmas()  # Get the first set of synonyms
        if len(lemmas) > 1:
            return random.choice(lemmas).name()  # Choose a random synonym
    return word

# Function to paraphrase certain phrases and replace synonyms
def remove_ai_flags(text):
    # Common AI phrases to paraphrase or modify
    replacements = {
        "As an AI": "From a computational perspective",
        "In conclusion": "To sum up",
        "AI-generated": "computer-produced",
        "machine learning model": "intelligent system",
        "it is important to note": "it should be considered",
    }

    # Replace phrases in the text
    for key, value in replacements.items():
        text = text.replace(key, value)

    # Replace individual words with synonyms
    words = text.split()
    modified_words = []
    for word in words:
        if random.random() < 0.2:  # Randomly change 20% of words to synonyms
            modified_words.append(find_synonym(word))
        else:
            modified_words.append(word)
    
    return " ".join(modified_words)

# Function to get input text and output modified text
def process_text():
    input_text = input_box.get("1.0", tk.END)  # Get the text from input box
    modified_text = remove_ai_flags(input_text)  # Process the text
    output_box.delete("1.0", tk.END)  # Clear the output box
    output_box.insert(tk.END, modified_text)  # Insert modified text into output box

# Create the main window
root = tk.Tk()
root.title("AI Flag Remover")

# Create a label and input text box
input_label = tk.Label(root, text="Enter AI-generated Text:")
input_label.pack(pady=5)
input_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
input_box.pack(pady=5)

# Create a button to process the text
process_button = tk.Button(root, text="Remove AI Flags", command=process_text)
process_button.pack(pady=10)

# Create a label and output text box
output_label = tk.Label(root, text="Modified Text (AI flags removed):")
output_label.pack(pady=5)
output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
output_box.pack(pady=5)

# Run the Tkinter loop
root.mainloop()
