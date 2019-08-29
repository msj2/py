import time

#  Your duty is to generate a list where each item is a product of the multiplication of the items of another list by two. You can either use a for loop or a list comprehension. 
start = time.time()
a = range(100000)
b = []
for i in a:
    b.append(i*2)
end = time.time()
print(end - start)
#   0.0200550556183 seconds

#    instead of using a for loop we will use a list comprehension:
start = time.time()
a = range(100000)
b = [i*2 for i in a]
end = time.time()
print(end - start)
#   0.00908303260803 seconds


'''
Marcelo Rossi
February 12, 2019 at 6:19 am
append is way faster, at least in python 3*
you should put also the range directly in the for without using the a auxiliary variable, so it yields directly de values…

my two cents

https://stackoverflow.com/questions/673523/how-do-i-measure-execution-time-of-a-command-on-the-windows-command-line

https://pythonhow.com/category/uncategorized/


https://pythonhow.com/link-python-challenges/


https://mail.google.com/mail/u/0/#inbox
https://docs.google.com/document/d/1ENyLb8sARcTMdbhR7X3tr6K3A4VxWLzERer5n9kItK4/edit
https://docs.google.com/spreadsheets/d/1R7lulTnkBY77mZpQTt6hr_sfrfNBDtdvaxTzaRp5420/edit#gid=719947419
https://docs.google.com/spreadsheets/d/1R9w_tTCSLAqDeQVVExW4809l8i_ADZjVeW59motFfoo/edit#gid=0
http://35.237.23.84:7081/offers
http://test.platify.co:7007/api-collections-offers/#/Brand/get_admin_offers_getBrands
https://stackoverflow.com/questions/39037049/how-to-upload-a-file-and-json-data-in-postman
https://blog.getpostman.com/2018/08/09/postman-release-6-2/
https://learning.getpostman.com/docs/postman/sending_api_requests/debugging_and_logs/
https://www.getpostman.com/resources/videos-tutorials/
https://learning.getpostman.com/docs/postman/collection_runs/debugging_a_collection_run/
https://docs.postman-echo.com/?version=latest
https://dzone.com/articles/sorting-dictionaries-in-python
https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/
https://codingbat.com/python
https://www.edureka.co/blog/interview-questions/python-interview-questions/
http://www.pythonchallenge.com/
https://coderbyte.com/challenges
https://pythonhow.com/instructions/
https://pythonhow.com/what-can-i-do-with-python/
https://pythonhow.com/correct-way-fix-python-error/
https://stackoverflow.com/questions/25535325/python-3-4-1-print-new-line
https://github.com/msj2/py/tree/master


http://www.pythonchallenge.com/pc/def/0.html

https://stackoverflow.com/questions/25535325/python-3-4-1-print-new-line
'''
