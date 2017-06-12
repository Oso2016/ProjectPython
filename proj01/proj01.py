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
birthday = raw_input("Have you had a birthday already this year? yes or no:")
print birthday
if birthday == "yes":
    print name + " will turn 100 in the year",
    print 100 - int(age) + 2017
if birthday == "no":
    print name + " will turn 100 in the year",
    print 100 - int(age) + 2016
if age < "13":
    print ""

