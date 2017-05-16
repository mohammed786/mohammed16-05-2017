#Created by Mohammed Modi. Dated: 15-05-2017

import datetime
import random
import json

"""
Student class will bind the data object from files to RAM as well as MyCache
"""
class Student:
    def __init__(self):
        self.id = 0
        self.class_enrolled = ""
        self.marks = 0
    def set_data(self,id,class_enrolled,marks):
        self.id = id;
        self.marks = marks
        self.class_enrolled = class_enrolled
    def get_id(self):
        return self.id
    
    def get_class_enrolled(self):
        return self.class_enrolled

    def get_marks(self):
        return self.marks

class MyCache:
    def __init__(self):
        self.cache = {}
        self.max_cache_size = 20
    """
    Returns True or False depending on whether or not the key is in the 
    cache
    """
    def __contains__(self,key):
        return key in self.cache

    def add(self,key,value):
        """
        Update the cache dictionary and optionally remove the oldest item
        """
        if key not in self.cache and len(self.cache) >= self.max_cache_size:
            self.remove_oldest()
 
        self.cache[key] = {'date_accessed': datetime.datetime.now(),
                           'value': value}
    
    def update(self,key,value):
        self.cache[key] = {'date_accessed': datetime.datetime.now(),'value': value}
        self.set_accessed_date(key)

    def remove_oldest(self):
        """
        Remove the entry that has the oldest accessed date
        """
        oldest_entry = None
        for key in self.cache:
            if oldest_entry is None:
                oldest_entry = key
            elif self.cache[key]['date_accessed'] < self.cache[oldest_entry][
                'date_accessed']:
                oldest_entry = key
        self.cache.pop(oldest_entry)

    def delete_record(self,key):
        if(key in self.cache):
            self.cache.pop(key)
        else:
            print("Record not found")

    def display_cache(self,key):
        if(key in cache):
            print("Student ID: " + str(self.cache[key]['value'].get_id()))
            print("Class Enrolled: " + str(self.cache[key]['value'].get_class_enrolled()))
            print("Marks:     " + str(self.cache[key]['value'].get_marks()))
            self.set_accessed_date(key)
        else:
            return False
        return True
    
    def set_accessed_date(self,key):
        self.cache[key]['date_accessed'] = datetime.datetime.now()
    

    def get_data(self,key):
        return self.cache[key]['value']
    
    def size(self):
        """
        Return the size of the cache
        """
        return len(self.cache)

if __name__ == '__main__':
    #Reading Test Data from input file
    with open('test_data/inputs.json') as json_file:
        data = json.load(json_file)
    # Test the cache
    cache = MyCache()
    for obj in data:
        student = Student();
        student.set_data(obj['id'],obj['class_enrolled'],obj['marks'])    
        key = obj['id']
        if key in cache:
            continue
        else:
            value = student
            cache.add(key, value)
    '''
    Provide to CRUD operations in cache and on EXIT the updated data will
    be stored in file.
    '''
    while(1):
        print("Enter Your Choice")
        print("1: Display\n2: Update\n3: Create\n4: Delete\n5: Exit")
        choice = int(input())
        if(choice == 1):
            print("Enter Student ID")
            input_key = int(input())
            if(not cache.display_cache(input_key)):
                print("Data not found in Cache..")
        elif(choice == 2):
            #Reading Test Data for updating Cache
            with open('test_data/update.json') as json_file:
                update_data = json.load(json_file)
            for obj in update_data:
                if obj['id'] in cache:
                    student = Student()
                    student.set_data(obj['id'],obj['class_enrolled'],obj['marks'])
                    key = obj['id']
                    cache.update(key, student)
                    print("Student Record for Student ID = %s is updated" % key)
                else:
                    print("Record not found in cache")
        elif(choice == 3):
            print("Enter Student ID to add in cache ")
            new_key = int(input())
            print("Updating Cache.....")
            for obj in data:
                if new_key not in cache:
                    if(obj['id'] == new_key):
                        student = Student()
                        student.set_data(obj['id'],obj['class_enrolled'],obj['marks'])
                        value = student
                        cache.add(new_key, value)
                        cache.display_cache(input_key)
        elif(choice == 4):
            print("Enter Student ID:")
            delete_key = int(input())
            cache.delete_record(delete_key)
            print("Student ID:%s Deleted from cache" % delete_key)            
        elif(choice == 5):
            for i in range(0,len(data)):
                key = data[i]['id']
                if key in cache:
                    data[i]['class_enrolled'] = cache.get_data(key).get_class_enrolled()
                    data[i]['marks'] = cache.get_data(key).get_marks()
            with open('test_data/inputs.json', 'w') as outfile:
                json.dump(data, outfile)
                print("File restored to disk")
            exit(0)

    



