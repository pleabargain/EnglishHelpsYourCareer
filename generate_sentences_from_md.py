#!/usr/bin/env python3
# this will open an md file

import random

NAMES = "/home/dgd/Desktop/EnglishHelpsYourCareer/db_names_male.md"
FOOD = "/home/dgd/Desktop/EnglishHelpsYourCareer/db_food.md"
COUNTRIES = "/home/dgd/Desktop/EnglishHelpsYourCareer/db_countries.md" 

# open the files
# create a function

def get_content(filename): 
    """
    returns list of items from filenames
    remove empty lines 
    remove duplicate entries
    """
    
    # set will make sure that there are no dupes
    stuff = set()
    with open(filename) as tmp:
        lines = tmp.readlines()
    for one_line in lines:
        line = one_line.strip()
        if len(lines)> 0:
            stuff.add(line)
            #create a list out of the set
    return list(stuff)


def main(output_file_name ="randomfood.md",
        how_many_sentences=3,
        super_headline="food",
        headline="""Horst is a great and patient teacher! Thank you!"""):
    """
    generates random combination of sentences
    uses get_content func
    takes four params
    """

    names = get_content(NAMES)
    foods = get_content(FOOD)
    countries = get_content(COUNTRIES)
    
    # create the md
    output = """# {}\n## {}\n\n""".format(super_headline,headline)

    for x in range(how_many_sentences):
        # Carl from Vienna loves hotdogs.
        output += "{} from {} loves {}.\n\n".format(random.choice(names),
                                                  random.choice(countries),
                                                  random.choice(foods))

        
    print (output)

    #write markdown
    with open (output_file_name , "w") as temp:
        temp.write(output)
    print("file written as ",output_file_name)


if __name__=='__main__':
    main()






         













