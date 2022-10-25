# Longest river finder
Program generates random area of given width and height filled with 'river' or 'land' fields. Then algortihm looks for longest river of that area. As a river we consider every river field with its neighours on left and right, above and below, but not diagonally.


# Requirements:
* python 3.10
* colorama 0.4.5

`pip install -r requirements.txt`

# Output

User receives as output in console colored rectangle, where red tiles represents land and blue ones - rivers. In addition, the longest river is marked in green, so user can easily spot where exactly it is placed. In addition, there are printed some basic statistics about processing time. As an example, here you can see output for command:

`python3 main.py 40 40`

![image](https://user-images.githubusercontent.com/49252352/197853753-9d43f459-67b8-47b0-a767-f3426ce31b4b.png)

Full option description you can find of course under:

`python3 main.py --help`

# To do / work in progress

In future, I'm planning to add loading problem data from .csv file and/or in other way. Also implementing more algorithms is considered.
