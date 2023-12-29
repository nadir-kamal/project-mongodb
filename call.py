import requests
import json

# URLs
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

def get_document_by_employee_id(employee_id):
    try:
        # Payload for MongoDB API request (find)
        filter_criteria = {"tag_data": employee_id}
        find_payload = {
            "collection": collection_name,
            "database": database_name,
            "dataSource": "Cluster0",
            "filter": filter_criteria
        }

        # Find a document in MongoDB
        find_response = requests.post(url_find, headers=headers, json=find_payload)

        if find_response.status_code == 200:
            found_document = find_response.json()
            print("Found document:")
            print(json.dumps(found_document, indent=2))
            return found_document
        else:
            print(f"Error querying MongoDB. Status Code: {find_response.status_code}")
            return None

    except KeyboardInterrupt:
        print("\nScript interrupted by user.")
        return None

# Example usage of the function
employee_id_to_search = "123456789"  # Replace with the employee_id you want to search
found_document = get_document_by_employee_id(employee_id_to_search)
