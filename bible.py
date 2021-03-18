#
# This script fetches data from the bible easily and quickly.
#

import requests
import json
import sys

border = "***"

q = input("> ") if len(sys.argv) < 2 else ' '.join(sys.argv[1:])
# get data
base = "https://getbible.net/json?"
url = base + "passage=" + q + "&" + "v=kjv"
r = requests.get(url)
t = r.text[1:-2]
j = json.loads(t)

print(border)

# main loop
print("Book: " + j["book"][0]["book_name"])
for ch in j["book"]:
    print("Chapter: " + str(ch["chapter_nr"]))
    for vn in ch["chapter"]:
        v = ch["chapter"][vn]
        print(str(v["verse_nr"]) + " " + str(v["verse"].strip()))

print(border)

