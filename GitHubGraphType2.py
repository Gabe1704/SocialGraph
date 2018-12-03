from github import Github, BadCredentialsException
from itertools import zip_longest
import webbrowser
import csv
import matplotlib.pyplot as plt
import numpy as np

UserIsLogIn = False

while not UserIsLogIn:
    try:
        username = input("Please Enter Your Username for Github")
        password = input("Please Enter Your Password for that Account: ")
        gha = Github(username, password)
        user = gha.get_user(login="spotify")
        #user = gha.get_user(login = username)
        UserIsLogIn = True

    except BadCredentialsException:
        print("Either your Github Username or Password is entered incorrectly")

#for repo in user.get_repos():
#        myList = list()
#        myList.append(repo.language)

mylist1 = list()
mylist2 = list()

repo = user.get_repo("luigi")
line = 0
for contributors in repo.get_stats_contributors():
    if line >= 91:
        mylist1.append(contributors.author.login)
        mylist2.append(contributors.total)
    line +=1
d = [mylist1, mylist2]


with open('Information.csv', 'w') as f:
      writer = csv.writer(f)
      writer.writerows(zip(mylist1, mylist2))
f.close()

webbrowser.open("SocialGraph1.html")
