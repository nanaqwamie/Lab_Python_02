#archibold_acheampong

primary_school_age=6
legal_voting_age=18
president_age=25
retirement_age=60
personsAge = input("Enter an age: ")
if personsAge<primary_school_age:
     print 'Too young'
else:
     print'fit for school'

if personsAge>=legal_voting_age:
     print'Remember to vote'

if personsAge>=president_age:
     print'Vote for me'

else:
     print'You can’t be president'

if personsAge>=retirement_age:
     print'Too old'
