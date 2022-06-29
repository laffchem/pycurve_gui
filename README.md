# PyCurve

___

### Intro

PyCurve was made because I wanted a quick way to curve my exams. At first,
I made this as a cli app but figured it would be a fun project to practice
making a webapp and figured it could help people.

### Function

___

![Home Page!](/images/home.png "Home Page")

Currently, csv is the only input and output filetype. You can open this with
google sheets, excel, or libreoffice to see the column name to type in.

You can name the output file to whatever you want, it will add the .csv to it
when you download.

There are 3 curve options currently as they are the 3 I use depending on how bad
the students do on my chemistry exams.

1. Square Root Curve -> This will take the square root of the raw scores, and multiply
the result by 10. (This is the most generous)

2. Max Score Curve -> Not sure what this is called so named it this. This will take
the highest score and find the next highest grade percentage it is closest to. 
(score = 85, next letter grade = 90) Then, it will take the difference and add it
to every other score. (This is least generous but the one I use the most)

3. 10 point bump -> Exactly what it says, adds 10 points to all the scores.

### Downloads

___

![Downloads!](/images/home.png "Downloads")

This is pretty self explanatory. Download will allow you to download the file 
you specified on the home page. Curve another test will take you to the home page.

**Important** -> I know there are flash messages, but just so you are aware;
**ALL FILES** Uploaded and Downloaded are erased from the webserver. This happens 
on the local version as well.

### Suggestions

___

If you have any bug reports or suggestions, please let me know. I've only been
coding 3 months and this was a great learning experience for me.
