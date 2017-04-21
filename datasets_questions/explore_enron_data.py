#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import math
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)
#length_dict = len(enron_data.values()[0])
#print length_dict

count = 0
for key, value in enron_data.items():
    count = count+1 if enron_data[key]["poi"]==1 else count

print count

#print "James Prentice's stock value is {}".format(enron_data["PRENTICE JAMES"]["total_stock_value"])
#print enron_data["COLWELL WESLEY"]
#print "Wesley Colwell to poi is {}".format(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

#print enron_data["SKILLING JEFFREY K"]["total_payments"]
#print enron_data["LAY KENNETH L"]["total_payments"]
#print enron_data["FASTOW ANDREW S"]["total_payments"]

salary_notNAN=0
email_notNAN=0
for key in enron_data:
    salary_notNAN = salary_notNAN+1 if enron_data[key]["salary"]!='NaN' else salary_notNAN
    email_notNAN = email_notNAN + 1 if enron_data[key]["email_address"] != 'NaN' else email_notNAN

print salary_notNAN
print email_notNAN

total_payments_NaN=0
for key in enron_data:
    total_payments_NaN = total_payments_NaN + 1 if enron_data[key]["total_payments"] == 'NaN' else total_payments_NaN
print total_payments_NaN/float(len(enron_data))
print (total_payments_NaN+10)
