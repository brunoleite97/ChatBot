import subprocess

import nltk
nltk.download('punkt')

subprocess.run(["python", "train.py"])

subprocess.run(["python", "chat.py"])