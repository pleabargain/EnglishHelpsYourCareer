# generate ngrams in markdown
# scan markdown file
# takes headline (leading #) and the word (phrase) of this headline
# search next free line after headline
# insert ngram-png from google view (base64)
# generate html file

import sys
import requests
import base64


#google ngram example for png without iframe Python case-insensitive:
#ngram:
# suffix * : 10 most common sentences: "i got *" -> i got lost, i got drunk ...
# suffix _INF : inflection = all forms: "book_INF a hotel" -> booking a hotel, booked a hotel ...
"""
interactive, all:
https://books.google.com/ngrams/interactive_chart?content=Python&year_start=1989&year_end=2019&case_insensitive=on&corpus=26&smoothing=3&direct_url=t4%3B%2CPython%3B%2Cc0%3B%2Cs0%3B%3BPython%3B%2Cc0%3B%3Bpython%3B%2Cc0%3B%3BPYTHON%3B%2Cc0#t4%3B%2CPython%3B%2Cc0%3B%2Cs1%3B%3BPython%3B%2Cc0%3B%3Bpython%3B%2Cc0%3B%3BPYTHON%3B%2Cc0

png, static
https://books.google.com/ngrams/chart?content=Python&year_start=1989&year_end=2019&case_insensitive=off&corpus=26&smoothing=3

png https://books.google.com/ngrams/chart?content=Python

"""

def save_image_from_url(url):
    img_data = requests.get(url).content
    with open('tmp.png', 'wb') as handler:
        handler.write(img_data)

def main(filenames=None, start_year=1950):
    if filenames is None:
        raise ValueError("no markdown filename(s) passed")
    for one_filename in filenames:
        print("processing file:", one_filename)
        name = "".join(one_filename.split(".")[:-1])
        ext = one_filename.split(".")[-1]
        new_name = name+"_new.html"
        with open(one_filename) as tmp:
            lines = tmp.readlines()
        newlines = []
        img_lines = []
        for line in lines:
            #newlines.append(line)
            if not line.startswith("# "):
                newlines.append(line)
                continue
            #this is the phrase that ngram searches
            phrase = line[2:]
            print("found phrase:", phrase)
            newlines.extend(img_lines) # add previous image
            img_lines = []
            newlines.append("<h2>{}</h2>".format(phrase))

            # create tmp image
            url = "https://books.google.com/ngrams/{}chart?content={}&year_start={}&year_end=2019".format("", phrase, start_year)
            url2 = "https://books.google.com/ngrams/{}chart?content={}&year_start={}&year_end=2019".format("interactive_", phrase, start_year)
            save_image_from_url(url) # now in tmp.png
            print("saved image!")
            with open("tmp.png", "rb") as img_file:
                img_string = base64.b64encode(img_file.read())

            #img_data = requests.get(url).content
            url_string = img_string.decode("utf-8")
            img_lines.append('<br><a href="{}"><img src="data:image/png;base64,{}"></a><br>'.format(url2,url_string))
            img_lines.append('<small>made with <a href="https://books.google.com/ngrams/">Google ngram viewer</a> Click in the image for interactive/larger image</small>')
        newlines.extend(img_lines) # add last image

        with open(new_name,"w") as tmp:
            tmp.writelines(newlines)
        print("done  with file: "+new_name)





if __name__ == "__main__":
    main(sys.argv[1:])