# Activity 4- Python List
# Autumn Skaalen
# ISQA 3900 Web Application Developement
# February 20, 2022

# activity 4b

    from statistics import mean

    def main():
        grades = getScores()
        grade = mean(grades)
        abcGrade = getGrade(grade)
        print("\nScores: ",grades)
        print("Total: ",sum(grades))
        print("Number of Scores: ",len(grades))
        print("Average Score: ",grade)
        print ("Letter grade: ",abcGrade)
        print("\nBye!")

    def getScores():
        grades = []
        while True:
            grade = int(input("Enter test score(-1 to quit): "))
            if grade == -1: return grades
            grades.append(grade)
            for grade in grades:
                if grade < 0 or grade >= 101:
                    print("You must enter values >=0 and <=100 or -1 to quit. Try again.")
                    grades.remove(grade)

    def getGrade(grade):
        best = 100
        if grade >= best - 8:
            return 'A'
        elif grade >= best - 12:
            return 'B+'
        elif grade >= best - 18:
            return 'B'
        elif grade >= best - 22:
            return 'C+'
        elif grade >= best - 30:
            return 'C'
        elif grade >= best - 40:
            return 'D'

        else:
            return 'F'

    main()
