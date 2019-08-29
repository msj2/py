"""" Sandeep said during lunch walk, running a loop in reverse is faster .
I decided to test it, Run the loop once with increasing counter, next time with decreasing counter
Does running the Loop in reverse, run faster
VS Code is helpful with it's autocomplete function names after dot.
"""
import time
limit = 1000
i = 0
for i in xrange(0, 100, 1):
	limit = limit * 10
	t1 = time.time()
	for x in xrange(1,limit):
		pass
	t2 = time.time()
	inc = t2 - t1

	t1 = time.time()
	for x in xrange(limit, 1, -1):
		pass
	t2 = time.time()
	dec = t2 - t1
	print (limit, " Increasing index = ", inc, '\nDecreasing index = ', dec)
  
  
  '''
  ('Increasing index = ', 0.227370023727417, '\nDecreasing index = ', 0.18471384048461914)
ekagga@ekagga-009:~/Desktop$ cd /home/ekagga/Desktop ; env "PYTHONIOENCODING=UTF-8" "PYTHONUNBUFFERED=1" /usr/bin/python /home/ekagga/.vscode/extensions/ms-python.python-2019.1.0/pythonFiles/ptvsd_launcher.py --default --nodebug --client --host localhost --port 43847 "/home/ekagga/Desktop/loop reverse.py"
('Increasing index = ', 0.2277538776397705, '\nDecreasing index = ', 0.18790197372436523)
ekagga@ekagga-009:~/Desktop$ cd /home/ekagga/Desktop ; env "PYTHONIOENCODING=UTF-8" "PYTHONUNBUFFERED=1" /usr/bin/python /home/ekagga/.vscode/extensions/ms-python.python-2019.1.0/pythonFiles/ptvsd_launcher.py --default --nodebug --client --host localhost --port 42329 "/home/ekagga/Desktop/loop reverse.py"
(10000, ' Increasing index = ', 0.00018906593322753906, '\nDecreasing index = ', 0.00021600723266601562)
(100000, ' Increasing index = ', 0.0019328594207763672, '\nDecreasing index = ', 0.0028312206268310547)
(1000000, ' Increasing index = ', 0.021467924118041992, '\nDecreasing index = ', 0.021695852279663086)
(10000000, ' Increasing index = ', 0.19319391250610352, '\nDecreasing index = ', 0.1841278076171875)
(100000000, ' Increasing index = ', 1.8491730690002441, '\nDecreasing index = ', 1.916248083114624)
(1000000000, ' Increasing index = ', 18.27824902534485, '\nDecreasing index = ', 18.73585605621338)

Just hung for 3+ min


Next run, Machine simply went out of power very rapidly, Looks this program is taxing the Laptop a lot


10000 	 Increasing index =  0.000237941741943 	 Decreasing index =  0.000231027603149

100000 	 Increasing index =  0.00261497497559 	 Decreasing index =  0.00260806083679

1000000 	 Increasing index =  0.0239720344543 	 Decreasing index =  0.0238080024719

10000000 	 Increasing index =  0.228687047958 	 Decreasing index =  0.225402116776

100000000 	 Increasing index =  2.26070809364 	 Decreasing index =  2.26172804832

1000000000 	 Increasing index =  22.4760560989 	 Decreasing index =  22.2716181278

10000000000 	 Increasing index =  221.816204071 	 Decreasing index =  215.736984968

Let me reboot.
'''
