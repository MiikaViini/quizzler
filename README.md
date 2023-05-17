![quizzler](https://github.com/MiikaViini/quizzler/blob/master/quizzler.png?raw=true)

# Quizzler
Quiz game from Python Course
#

I have been doing 100 days of Python -course in Udemy and this project is from day 35.
It introduces use of API Endpoints and rehearse multiple basic consepts in Python, fe. OOP and importing modules.
The program is developed with PyCharm and intrepreter that i was using were version 3.11.

Questions are fetched from here: 
`https://opentdb.com/` and manipulating ether the `parameters` or endpoint URL, you
can change amount of questions and category.
For now it is only supporting True/False questions.

You need `requests` module, which is used to get the data from endpoint.
```
pip install requests
```
If you dont have pip installed, look it for here:
``` 
https://pip.pypa.io/en/stable/installing/
```

1. Go to your console and clone repository
```
git clone https://github.com/MiikaViini/quizzler.git
```
2. Go to the directory and type to your console:
```
python3 main.py
```
