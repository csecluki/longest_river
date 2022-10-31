# Longest river finder
Program generates random area of given width and height filled with 'river' or 'land' fields. Then algortihm looks for longest river of that area. As a river we consider every river field with its neighours on left and right, above and below, but not diagonally.


# Requirements:
* python 3.10
* colorama 0.4.5

`pip install -r requirements.txt`

# Output

User receives as output in console colored rectangle, where red tiles represents land and blue ones - rivers. In addition, the longest river is marked in green, so user can easily spot where exactly it is placed. In addition, there are printed some basic statistics about processing time. As an example, here you can see output for command:

`python3 main.py -f example_data/data.csv`

![image](https://user-images.githubusercontent.com/49252352/199008685-ae877cc3-26fe-4363-b3f9-d836d94ec456.png)

Full option description you can find of course under:

`python3 main.py --help`

# To do / work in progress

In future, I'm planning to add loading problem data from ~~.csv file~~ and/or in other way. Also implementing more algorithms is considered.
