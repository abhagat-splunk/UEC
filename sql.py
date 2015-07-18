import sys
import mysql.connector
import os
from try2 import main

def SQLQueries():
	try:
		conn = mysql.connector.connect(host='localhost',port='8889',database='UEC',user='root',password='root')
		if conn.is_connected():
			print "Connected"
		cs = conn.cursor()
		
		#sq1 = "select * from question"
		#cs.execute(sq1)
		#print cs.fetchall()
		sq2 = "select * from answer"
		cs.execute(sq2)
		d = cs.fetchall()
		#print d
		count_uid = 1
		for x in d:
			#print "SQL field"
			cs1 = conn.cursor()
			#print x
			f = open('new.txt','w')
			#print "Put in the file"
			a = str(x).split("'")[1]
			#print a
			f.write(a)
			f.close()
			#print "Answer file"
			#os.system('cat new.txt')
			marks = main()
			print str(marks)
			print count_uid
			sq3 = "update answer set marks="+str(marks)+" where aid="+str(count_uid)
			count_uid+=1
			cs1.execute(sq3)
			cs1.close()
		#print cs.fetchall()
		cs.close()
		conn.commit()
	except:
		print "Database not connected"
		exit 

SQLQueries()
