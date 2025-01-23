class Aluno:
    def __init__(self, name, registration):
        self.name = name
        self.registration = registration
        self.grade = []
    
    def add_grades(self, value):
        self.grade.append(value)

    def gradeAverage(self  ):
        count = sum(self.grade)
        average = count/len(self.grade)
        return average
    


aluno = Aluno('Paulo', 123)
aluno.add_grades(10)
aluno.add_grades(10)

print(f"Média: {aluno.gradeAverage()}")