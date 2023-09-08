import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number=10):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self):
        """Resets the ith score, counting from 1."""
        for i in range(len(self.scores)):
            a = random.randrange(0, 100)
            self.scores[i] = a

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
    
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

def output(lys):
    print("Name                   Scores                                        Avg Score")
    print("—----------------------------------------------------------------------------")
    for i in lys:
        print(i.getName(), end="")
        c = ""
        for a in range(23 - len(i.getName())):
            print(" ", end="")
        for a in range(10):
            c += str(i.getScore(a)) + " "
        print(c,end="")
        for a in range(46 - len(c)):
            print(" ", end="")
        print(i.getAverage())

def main():
    """A simple test."""
    s1, s2, s3, s4, s5 = Student("Bradyn"),Student("Matt"),Student("Alex"),Student("Bob"),Student("Lucy"),
    s6, s7, s8, s9, s10 = Student("Ben"),Student("Mary"),Student("Quin"),Student("Vivian"),Student("Madison")
    s1.setScore(), s2.setScore(), s3.setScore(), s4.setScore(), s5.setScore()
    s6.setScore(), s7.setScore(), s8.setScore(), s9.setScore(), s10.setScore()
    lys = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
    output(lys)
    newLys = [s1.getAverage(),s2.getAverage(),s3.getAverage(),s4.getAverage(),s5.getAverage(),
              s6.getAverage(),s7.getAverage(),s8.getAverage(),s9.getAverage(),s10.getAverage()]
    newLys.sort()
    newArr = []
    for i in range(len(lys)):
        for a in range(len(lys)):
            if newLys[i] == lys[a].getAverage():
                newArr.append(lys[a])
                lys.pop(a)
                break
    print("\nSorted:")
    output(newArr)
    
        
if __name__ == "__main__":
    main()
