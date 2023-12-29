import requests
import json
from datetime import datetime

# URLs
url_insert = "https://eu-west-2.aws.data.mongodb-api.com/app/data-fxpru/endpoint/data/v1/action/insertOne"
# Define the URL for finding a document
url_find = "https://eu-west-2.aws.data.mongodb-api.com/app/data-fxpru/endpoint/data/v1/action/findOne"

# Database and collection names
database_name = "students"
collection_name = "colstud"

# Common headers for MongoDB API requests
headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'r6sCYqd6LJ0PDvhq6zuS02zeeI8U9KKKWQs2RscJCQZnrlGj0uhIdd8mkeUE6YD5',
}

def get_employee_info_by_tag_data(tag_data):
    query = {"tag_data": tag_data}
    result = collection_name.find_one(query)

    if result:
        return result
    else:
        return None

try:
    # Simulate RFID tag data
    tag_data = "987654321"

    # Get user details
    user_name = input("Enter user name: ")
    employee_id = input("Enter employee ID: ")
    department = input("Enter department: ")
    position = input("Enter position: ")
    email = input("Enter email: ")

    # Get the current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Payload for MongoDB API request (insert)
    insert_payload = {
        "dataSource": "Cluster0",
        "database": database_name,
        "collection": collection_name,
        "document": {
            "tag_data": tag_data,
            "user_name": user_name,
            "employee_id": employee_id,
            "department": department,
            "position": position,
            "email": email,
            "attendance_time": current_time,
        }
    }

    # Insert attendance record
    insert_response = requests.post(url_insert, headers=headers, json=insert_payload)

    if insert_response.status_code == 201:
        inserted_id = insert_response.json().get("insertedId")
        print("Successfully recorded attendance for user:", user_name)
        print("Inserted document ID:", inserted_id)
        print("RFID Tag Data:", tag_data)

        # Query MongoDB for the inserted document
        find_payload = {
            "collection": collection_name,
            "database": database_name,
            "dataSource": "Cluster0",
            "projection": {"_id": 1}
        }

        find_response = requests.post(url_find, headers=headers, json=find_payload)

        if find_response.status_code == 200:
            found_document = find_response.json()
            print("Found document:")
            print(json.dumps(found_document, indent=2))
        else:
            print("Error querying MongoDB:", find_response.status_code, find_response.text)
    else:
        print("Response: ", insert_response.status_code)
        print("Error recording attendance:", insert_response.text)

except KeyboardInterrupt:
    print("\nScript interrupted by user.")
finally:
    # Cleanup (if needed)
    pass

