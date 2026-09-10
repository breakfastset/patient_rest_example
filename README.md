# patient_rest_example

For learning purposes
- Simple REST service using Python
- Simple class building

TODO:
Create the following:
a) a simple web application in python flask to consume the web service
b) a simple java application to consume the web service
[optional] c) another application in another language (php / C#) to consume the web service



Question 1:
JSON is used as a format for data exchange. 
a) Demonstrate how to read a simple JSON file using Python and load it into a custom object. 
b) Given information: There are multiple Person objects with different ids, surnames, given names and ages. -> Create a Person class

c) Store this information in JSON and load into a list of Person objects in Python. 

d) Display the information in a nicely formatted output.


Question 3:
Extend Question 1 to build a Patient. Use the patient details to build 
a) a Web Flask project to create a web service to expose the details of a Patient object by 
b) searching his/her patient id or identity card number. 
     Expose the Patient object’s details and his/her ward details via json.
The Patient has the following details:
a.	Surname
b.	Given name
c.	Date of birth
d.	Gender
e.	Patient id
f.	Identity card number
g.	Address
h.	Current ward
The Ward has the following details:
a.	Ward number
b.	Class type
c.	Bed number
