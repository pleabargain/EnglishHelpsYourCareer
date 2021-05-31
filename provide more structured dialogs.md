# goal provide more structured dialogs
reason: incomplete sentences are too hard for my students to finish

students like the structure but the dialogs are not complete enough for them. They struggle too much.

# idea:
combine my random functions with dialogs that I have already gathered and/or written

# idea to implement?
Write out the dialog first to an output file and then edit.

Possible work flow described below. First get the functions that I have available.

```
dialog_list =[
r_sorry_late,
r_starting_the_meeting,
r_closing_the_meeting,

]
```
to become
where XXX is the function output with the name of the function

```
output_dialog_list =[
r_sorry_late, "r_sorry_late: XXXXXXXX",
r_starting_the_meeting, "r_starting_the_meeting:XXXXXXXXX,
r_closing_the_meeting, "r_closing_the_meeting: XXXXXXXXXXXXXX"

]
```

# human edits added

```
human_output_dialog_list =[
r_sorry_late, "r_sorry_late: XXXXXXXX",
"Not a problem. How are you?",
r_starting_the_meeting, "r_starting_the_meeting:XXXXXXXXX,
"Straight to business!",
r_closing_the_meeting, "r_closing_the_meeting: XXXXXXXXXXXXXX"
"That was fast!"

]
```
Names are machine generated.

```
human_output_dialog.html
bob: r_sorry_late, "r_sorry_late: XXXXXXXX",
ana: "Not a problem. How are you?",
bob: r_starting_the_meeting, "r_starting_the_meeting:XXXXXXXXX,
ana: "Straight to business!",
bob: r_closing_the_meeting, "r_closing_the_meeting: XXXXXXXXXXXXXX"
ana: "That was fast!"
```