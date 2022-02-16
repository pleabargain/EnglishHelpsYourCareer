# found here
# https://stackoverflow.com/questions/3368969/find-string-between-two-substrings


# # goal
# open file with mulitple headings extract 
# starting from msilib.schema import File
# from turtle import heading
# from the heading
# to the next heading
# the heading will be the name of the File
# the content between the headings will be the body of the file

#sample file
# # heading1
# * some text 
# * some more text 
# # heading2
# * some text2

# output 

# heading1.txt
# content
#  * some text 
#  * some more text 

# heading2.txt
# content
# * some text2






s = """# History & Current Events
* What is your favorite National Park?
* What Event in the Past Do You Wish You Could Have Witnessed?
* What Are the Most Important Changes, in Your Life and in the World, in the Last Decade?
* What National or International Events That You Lived Through Do You Remember Best?
* Why Should We Care About Events in Other Parts of the World?
* What News Stories Are You Following?
* How Do You Get Your News?
* Is Your Online World Just a 'Filter Bubble' of People With the Same Opinions?
* Do Your friends on Social Media All Have the Same Political Opinions You Do?



# If Only…
*some more text

# tes3
* here is some text

"""

target_file = "/home/dgd/Desktop/EnglishHelpsYourCareer/promptsfornarratives.md"

def open_file():
    with open(target_file) as myfile:
        lines=myfile.readlines()
        return lines
    # print(lines)



def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between_r( target_file, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""


print (find_between(s, "#", "#" ))


#print (find_between_r( s, "#", "#" ))
