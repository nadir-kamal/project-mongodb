from pymongo import MongoClient




client= MongoClient("mongodb+srv://soadmongo:souad2002@cluster0.kfqnwbu.mongodb.net/?retryWrites=true&w=majority")

db = client.get_database('students')
studentsCol = db.colstud

#print(studentsCol.count_documents({}))

#nv_etud = {'nom':'outharout','prenom':'hamza','num':111,'classe':'Informatique'}
nv_etud = {'nom':'outharout','prenom':'mouad','num':333,'classe':'Informatique'}
studentsCol.insert_one(nv_etud)