Assumptions:
Assuming that test data would be in JSON

Dictionary data structure is used for maintaing cache.

Implementation Strategy:

    - On intialization, data from the inputs.json file is loaded into 'data' variable
    - Every object from data will be mapped to each 'Student' object
    - Class Mycache has the logic for implementing cache which includes LRU Algorithm & CRUD operations in cache.
    - Mycache have the dictonary called 'cache' which will store student_id as key and value as object of 'Student' & 'Date_accessed'
    - Every time user Display, Update, Add a new element to cache the 'Date_accessed will be updated'
    - On exit which ever element is dirty will be updated to file.
    

There are two files in Test data
    1) inputs.json