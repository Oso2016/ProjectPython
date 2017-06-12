# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

#
#

name = raw_input("Enter a your name:")
print name
age= raw_input("Enter your age:")
print age
if int(age) < 100:
    birthday = raw_input("Have you had a birthday already this year? yes or no:")
    print birthday
    if birthday == "yes":
        print name + " will turn 100 in the year",
    print 100 - int(age) + 2017
    if birthday == "no":
        print name + " will turn 100 in the year",
    print 100 - int(age) + 2016
if int(age) < 13:
    print " You can watch G movies, and PG movies with parental guidance."
if int(age) == 13 or int(age) > 13:
    print " You can watch G, PG, and PG13 movies."
if int(age) == 17 or int(age) > 17:
    print "You can watch G, PG, PG13, and R movies."


