#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Book():
    
    def __init__(self, id, name, author):
        self.id = id
        self.name = name
        self.author = author
        self.reviews = []

    def __str__(self):
        return f"{self.id}, {self.name}, {self.author}, {self.reviews}"

    def add_review(self, review):
        self.reviews.append(review)


class Review:
    def __init__(self, id, description, rating):
        self.id = id
        self.description = description
        self.rating = rating

    def __str__(self):
        return f"{self.id},{self.description},{self.rating}"


book = Book(123, 'Object Oriented Programming with Python', 'Ranga')
print(book)


# In[30]:


# Student Mark details:- input -> Name and Marks -> Create a Method call len, count, max, min 
                        # and avg of marks.


class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_number_of_marks(self):
        return len(self.marks)

    def get_total_sum_of_marks(self):
        return sum(self.marks)

    def determine_maximum_mark(self):
        return max(self.marks)

    def determine_minimum_mark(self):
        return min(self.marks)

    def determine_average(self):
        return self.get_total_sum_of_marks()/self.get_number_of_marks()

    def add_new_mark(self, new_mark):
        self.marks.append(new_mark)

    def remove_mark_at_index(self, index):
        del self.marks[index]


student = Student ("Ranga", [23, 45, 56, 75])
number = student.get_number_of_marks()

sum_of_marks = student.get_total_sum_of_marks()
maximum_mark = student.determine_maximum_mark()
minimum_mark = student.determine_minimum_mark()
average = student.determine_average()

student.add_new_mark(35)
student.remove_mark_at_index(2)

print(student.marks)
print('===================================')
print(f"""Student[
               number_of_marks:   {number},
                  sum_of_marks:   {sum_of_marks},
                  maximum_mark:   {maximum_mark},
                  minimum_mark:   {minimum_mark},
                  average     :   {average}
       ] """)


# In[ ]:



        

