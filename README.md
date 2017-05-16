## Assumptions
* Assuming that test data would be in JSON
* There are two files for test Data
    -**test_data/inputs.json**: It contains the records of the students
    -**test_data/update.json**: It contains the records which user wants to update
* Python is installed in the system

## Data Structure
* **_Dictionary_ data structure is used for maintaing cache.**

## Implementation Strategy:
* On intialization, data from the inputs.json file is loaded into 'data' variable
* Every object from data will be mapped to each 'Student' object
* Class Mycache has the logic for implementing cache which includes LRU Algorithm & CRUD operations in cache.
* Mycache have the dictonary called 'cache' which will store student_id as key and value as object of 'Student' & 'Date_accessed'
* Every time user Display, Update, Add a new element to cache the 'Date_accessed will be updated'
* On exit which ever element is dirty will be updated to file.
    
## Steps for running the application
1. Enter student data in **input.json** file, the format should be:
```
[{
    id:<Student ID>,
    marks:<marks>,
    class_enrolled:<class>
}]
```
2. Run the **que1.py** file by writing: following statement in cmd for windows or terminal in linux.
```
python que1.py
```
3. Enter the data in **update.json** for updation.