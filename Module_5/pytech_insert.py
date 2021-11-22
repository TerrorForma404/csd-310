from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.rsnru.mongodb.net/cluster0?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
One = {
    "student_id": "1007",
    "first_name": "One",
    "last_name": "Won",
    "enrollments": [
        {
            "term": "Term 1",
            "gpa": "1.0",
            "start_date": "January 1, 2021",
            "end_date": "October 1, 2021",
            "courses": [
                {
                    "course_id": "Course 1",
                    "description": "One1",
                    "instructor": "Gumbo",
                    "grade": "F"
                },
                {
                    "course_id": "Course 2",
                    "description": "Two2",
                    "instructor": "Shrimp",
                    "grade": "F-"
                }
            ]
        }
    ]

}
Two = {
    "student_id": "1008",
    "first_name": "Two",
    "last_name": "Too",
    "enrollments": [
        {
            "term": "Term 2",
            "gpa": "2.00",
            "start_date": "February 02, 2022",
            "end_date": "September 22, 2022",
            "courses": [
                {
                    "course_id": "Course 2",
                    "description": "Doubledy",
                    "instructor": "Krispy",
                    "grade": "C"
                },
                {
                    "course_id": "Course 22",
                    "description": "Dee",
                    "instructor": "Kreme",
                    "grade": "F+"
                }
            ]
        }
    ]
}

# Frodo Baggins data document
Three = {
    "student_id": "1009",
    "first_name": "Three",
    "last_name": "Thirsty",
    "enrollments": [
        {
            "term": "Term 3",
            "gpa": "3.0",
            "start_date": "March 03, 2023",
            "end_date": "September 33, 2033",
            "courses": [
                {
                    "course_id": "Course 3",
                    "description": "You Just Got Dunked On",
                    "instructor": "Froggy Fresh",
                    "grade": "F-"
                },
                {
                    "course_id": "Course 4",
                    "description": "Batman 4: Batman fights off Vietnam era flashbacks",
                    "instructor": "Poison Ivy",
                    "grade": "F--"
                }
            ]
        }
    ]
}
students = db.students
print("\n  -- INSERT STATEMENTS --")
one_student_id = students.insert_one(one).inserted_id
print("  Inserted student record One Won into the students collection with document_id " + str(one_student_id))

two_student_id = students.insert_one(two).inserted_id
print("  Inserted student record Two Too into the students collection with document_id " + str(two_student_id))

three_student_id = students.insert_one(three).inserted_id
print("  Inserted student record Three Thirty into the students collection with document_id " + str(three_student_id))
