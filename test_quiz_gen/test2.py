#!/usr/bin/env python3
"""
This script will create an html file with question, options and answer hidden from view

This script is useful for generating questions for distributing to a diverse audience.py

TODO: GUI for naming output 
TODO: better formatting of content

"""


import  pandas as pd
import random
#import os
import sys


def main(sample_length=2, database="question_bank.csv"):
    """takes two parameters
        first parameter is number of questions to output
        second parameter is the name of the target database
         """

    #print("sample length", sample_length, "type:", type(sample_length))
    #SAMPLE_LENGTH = 2
    # open csv file
    df = pd.read_csv(database)
    list_of_unique_cat =df['CATEGORY'].unique()
    # idea: gui to select categories and number of items from category
    #write to file
    output = []
    # create loop
    #counter = 0
    samples_list = []
    for one_category in list_of_unique_cat:
        lines_of_this_cat = df[df['CATEGORY'] == one_category]
        #print("CATEGORY:", one_category,"LEN:",len(lines_of_this_cat))
        samples = lines_of_this_cat.sample(sample_length)
        #print(samples)
        samples_list.append(samples)
        #samples.to_csv(f"temp_{counter}.csv")
        #tempfiles.append(f"temp_{counter}.csv")
        #counter+=1
        #for line in samples:
        #    output.append(line)
    #print("----- all tempfiles are  written ------")
    result_file =  pd.concat(samples_list, ignore_index=True)
    # delete tempfiles
    #for file in tempfiles:
    #    os.remove(file)
    #print("---- all tempfiles deleted ----")
    result_file.to_csv("resultfile.csv")
    print("----- result csv is ready ----")

    # now make the result markdown
    #df = pd.read_csv("resultfile.csv")  # file with 2 examples per cat
    df = result_file
    full_toc = f"<p id='top'></p><h1>Table of Content:</h1><details open='true'><summary>{len(list_of_unique_cat)} categories (click to show/hide)</summary>"
    full_toc += "<ul>"
    list_of_unique_cat =df['CATEGORY'].unique()
    clean_cat_list = []
    questions = ""
    for one_category in list_of_unique_cat:
        lines_of_this_cat = df[df['CATEGORY'] == one_category]
        #toc.append(f"<a href=#{once_category}")
        # one_category can have spaces, we need underscorse for the internal anchor link
        clean_cat = "_".join(one_category.split(" "))
        clean_cat_list.append(clean_cat)
        full_toc += f"<li><a href='#{clean_cat}'>{one_category}</a></li>"
        questions += f"<p id='{clean_cat}'></p><h3><a href='#top'>&uarr;</a> {one_category}:</h3>"
        for i, line in enumerate(lines_of_this_cat.iterrows(),1):  # iterrows gives back a tuple :( line_number, data_dict )

            questions += f"<br><hr><br>this is task {i}/{len(lines_of_this_cat)} of category {line[1]['CATEGORY']} <i>(unique question number: {line[1]['UNIQUE_ID']})</i><br>" # column 0 is unique ID
            questions += f"<i>question type</i>: {line[1]['TYPE']}<br><i>instructions</i>: {line[1]['help text']}<br>"
            questions += f"<i>the question is:</i><b>{line[1]['QUESTION']}</b><br>"
            list_of_possible_answers = line[1]['all_answers'].split("|")
            list_of_possible_answers = [text.strip() for text in list_of_possible_answers if len(text.strip())> 0]
            random.shuffle(list_of_possible_answers)
            possible_answers_textfield = "<i><ul>" +  "".join(["<li>" + answer + "</li>" for answer in list_of_possible_answers]) + "</ul></i>"
            questions += f"possible answers are: <br> {possible_answers_textfield} <br></i>"
            questions += f"<details><summary>correct answer:</summary>{line[1]['correct answers texts(optional)']}</details><br>"

        #print("first line", lines_of_this_cat.head(1))
        #print("last line", lines_of_this_cat.tail(1))
        #print("line#0", lines_of_this_cat.loc[0:1])
        #print("line#1", lines_of_this_cat.loc[1:2])


    full_toc += "</ul></details><br><br><br>"

    # --- write output file (html) ----
    with open("output.html", "w") as html_file:
        html_file.write(full_toc)
        html_file.write(questions)
    print("ready!!!")




if __name__ == "__main__":
    main(*sys.argv[1:]) # dont forget the star to unpack the list as arguments!