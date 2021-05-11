# elementary-math
To generate some math examinations for elementary school students.

## usage
```shell
$>python3 plus.py -h
usage: plus.py [-h] [-l LIMIT] [-c COLUMN [COLUMN ...]] [-n NUMS] [-p PAGES]

optional arguments:
  -h, --help            show this help message and exit
  -l LIMIT, --limit LIMIT
                        set the limit of plus method, etc. 20
  -c COLUMN [COLUMN ...], --column COLUMN [COLUMN ...]
                        set the column of plus method, etc. "2 3 3 4"
  -n NUMS, --nums NUMS  set how many items will be generated in one page, etc. 100
  -p PAGES, --pages PAGES
                        set how many pages will be generated, etc. 30
```

## showcase

```shell
$> python3 plus.py -l 50 -p 5 -n 20
```

```
Page 1    Date:___________     Name:____________

11+24=        2+16-6=       7+3+6=        23-8-11-1=
39+4=         22+2-21=      35-7-13=      32-26+34-30=
7+28=         40-1-13=      24+24-37=     28+5+16-25=
15-10=        2+39-25=      45-24+10=     11-1+30-14=
32+6=         39-21+25=     47-37+29=     13+31-4+5=

Page 2    Date:___________     Name:____________

16+16=        29+11+3=      13+13-24=     9+34-26-6=
21+6=         16+25-12=     26+19-30=     13+36-11-30=
16-3=         33-19+1=      7-3+4=        7+40-41+17=
6+23=         21+14-5=      5+20+7=       11+36-18-11=
38-14=        10+28-22=     35-10+7=      43-33+11+20=

Page 3    Date:___________     Name:____________

2+4=          4+16-11=      1+40-7=       13+2+32-11=
28-12=        24+16-5=      1+14-11=      29-24+27-29=
35+6=         34-27+37=     38+2-37=      17+25-2-5=
23-11=        26+15+2=      21-10+17=     16-11-4+6=
27-6=         22-16-5=      47-42+16=     23-19+43-12=

Page 4    Date:___________     Name:____________

44-28=        43-16+14=     4+8+37=       21+7-2-20=
34-8=         34+13-23=     41-2-5=       33-14-7-4=
25+7=         44+4-33=      34-32+44=     20-13+5+13=
38-18=        15+2+1=       34-25+2=      15+29-16+19=
16-6=         9-8+35=       7+38-23=      47-11+1-12=

Page 5    Date:___________     Name:____________

45-23=        27-22+25=     42-15+8=      12+27+4-26=
36+4=         14-5+15=      8+22-12=      41-40+25+5=
45-17=        8+35-5=       17-2-11=      16+17-4-10=
14+31=        24+23-24=     9+3+22=       6+8+2+23=
43-25=        16+2+28=      27-11+12=     11-6+44-36=
```

Copy and paste all texts to Word(or other rich text editor) and then adjust space of line, font size so that it can show right format in one page.
