class StudentManager:
    def __init__(self):
        self.students = {}
    def addStudent(self,rollnumber,studentname,marks):
        if rollnumber in self.students:
            print(f"{rollnumber} already exists")
        else:
            self.students[rollnumber] = {"studentname": studentname, "marks": marks}
            print(f"{rollnumber} for the student {studentname} has been added")
    def getstudent(self,rollnumber):
        if rollnumber in self.students:
            return self.students[rollnumber]
        else:
            return f"No student with rollnumber {rollnumber}"
    def gettopstudents(self,criteria):
        topstudents = [
            {"rollnumber": rollnumber, "studentname" :data["studentname"],"marks": data["marks"]}
            for rollnumber,data in self.students.items()
            if data["marks"] > criteria
        ]
        return topstudents
result = StudentManager()
students_data = [
    {"rollnumber":1234,"studentname":"job","marks":85},
    {"rollnumber": 2345, "studentname": "raj", "marks":75},
    {"rollnumber": 3456, "studentname": "alice", "marks": 81},
    {"rollnumber": 2345, "studentname": "hari", "marks": 92},
]
for student in students_data:
    result.addStudent(student["rollnumber"],student["studentname"],student["marks"])
print(result.getstudent(2345))
top_students = result.gettopstudents(76)
print(top_students)
for student in top_students:
    print(student)




