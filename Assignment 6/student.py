#oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day. 
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''

class student:
    def __init__(self,name,id,year,major,gpa):
        self.name=name
        self.id=id
        self.year=year
        self.major=major
        self.gpa=gpa

    def GPA(self):
        if self.id>3.5:
            return "true"
        else:
            return "false"

    def freeLunch(self):
        import random
        lunch = random.randint(1, 10)
        if self.id==lunch:
            return "Winner! "+self.name+" gets free lunch!"
        else:
            return "Loser"

def main():
    #create three students and check if they get free lunch and if they qualify for honors
    student1 = student("Billy", 4, "J", "Biology", 3.4)
    student2 = student("Ralph", 2, "S", "mathematics", 2.7)
    student3 = student("Jamie", 8, "F", "psychology", 4.0)
    print(student1.name,student1.GPA())
    print(student2.name,student2.GPA())
    print(student3.name,student3.GPA())
    print(student1.name,student1.freeLunch())
    print(student2.name,student2.freeLunch())
    print(student3.name,student3.freeLunch())
main()
