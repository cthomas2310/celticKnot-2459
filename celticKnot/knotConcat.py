# run from /cs410
# parses folders with name convention: AaaAnnnn
# concats lines between <script> tags to index.html
# between header.html and footer.html

import re
import os

folder_format = "^....{4}[0-9]"
paths = []
output = open(r"index.html", 'w')
header = open(r"header.html", 'r')
output.write(header.read())
header.close()

for filename in os.listdir():
    x = re.search(folder_format, filename)
    if (x != None and os.path.isdir(filename)):
        paths.append(filename)

for path in paths:
    index = open(path + "/index.html", 'r')
    write = False
    for line in index:
        if "<script>" in line:
            write = True
            continue
        elif "</script>" in line:
            write = False
            break
        elif write:
            output.write(line)
    index.close()

footer = open(r"footer.html", 'r')
output.write(footer.read())
footer.close()




