import csv
from person import Person

def main():
    file = input("filename:")

    records = read_records_from_file(file)
    print("persons: " + str(len(records)))
    print("persons:")
    for person in records:
        print(person)

def read_records_from_file(file):
    records = []
    # write here the code for reading from file
    # and printing the read records
    with open(file) as f:
        data = csv.reader(f, delimiter=',')
    return data

if __name__ == '__main__':
    main()
