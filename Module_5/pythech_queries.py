from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.rsnru.mongodb.net/Cluster0?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db.students
student_list = students.find({})
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")
one = students.find_one({"student_id": "1007"})
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + one["student_id"] + "\n  First Name: " + one["first_name"] + "\n  Last Name: " + one["last_name"] + "\n")
