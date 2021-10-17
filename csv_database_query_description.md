database query

I have dbXYZ.csv with categories A B C 
categories A B C all have a certain number unique entries

# dbXYZ.csv
A 
- apple
- actor

B
- boy
- bat

C 
- cat
- car 
  
---

I want to compare dbRST.csv to dbXYZ.csv
db RST has categories categories A B C 

# dbRST.csv
A 
- apple
- actor
- avalanche

B
- boy
- bat
- basket

C 
- cat
- car 
- cradle
---
I need to know which items appear in dbXYZ.csv and dbRST.csv

output would look like 
| dbRST.csv      | dbABC.csv | missing|
| -----------   | ----------- | -|
| boy           |boy|
| bat           |bat|
| basket|      |        |
|   |         |basket|


I would then take the missing output and evaluate it.

