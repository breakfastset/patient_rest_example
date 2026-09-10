from person import Person
import json

def load_data(filename="patients.json"):
    """Load data from json file to list of Person objects and return."""
    people = []

    # start of reading from json
    people_db_file = open(filename, "r")
    json_data = json.load(people_db_file)
    people_list_of_dict = json_data["people"]  # list of dictionaries loaded from json

    for person_dict in people_list_of_dict:
        pid = person_dict["id"]
        surname = person_dict["surname"]
        given_name = person_dict["given_name"]
        age = person_dict["age"]
        new_person = Person(pid, surname, given_name, age)   # create a Person obj
        people.append(new_person)

    people_db_file.close()
    # end of file reading

    return people

def display_people(people_list):
    """Display Person objects in a nicely formatted list."""
    for index in range(len(people_list)):
        text = people_list[index].__str__()
        print(f"{index + 1:3}) {text}")

def main():
    """Test load_data()"""
    people_list = load_data("people.json")
    display_people(people_list)

if __name__ == '__main__':
    main()
