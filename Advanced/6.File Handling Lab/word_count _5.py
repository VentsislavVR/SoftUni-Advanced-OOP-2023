import os
import re
from collections import defaultdict
def read_content(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File does not exist")
        exit(0)




root_file = os.path.dirname(os.path.abspath(__file__))
words_file_name = "words.txt"
file_path = os.path.join(root_file,words_file_name)

words = read_content(words_file_name).lower().split()
text_file_name = "texxt.txt"

text_file_path = os.path.join(root_file,text_file_name)
text_content = read_content(text_file_path).lower()
text_content = re.sub(r"[^\w+\s]",'',text_content)
text_content_lines = text_content.split('\n')

words_count = defaultdict(lambda:0)
for word in words:
    for text_line in text_content_lines:
        if word in text_line:
            words_count[word] += 1
with open("output.txt", "w") as file:

    for key,value in sorted(words_count.items(),key=lambda kvp:-kvp[1]):
        file.write(f"{key} - {value}\n")
