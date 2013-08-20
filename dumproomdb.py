import sys
import sqlite3
import os
import os.path

def main(dbname):
	
	print 'start db dump'
	con = sqlite3.connect(dbname)
	
	
	with con:
		cur = con.cursor()
		qs = cur.execute("SELECT id, json FROM rooms")
		
		#data = cur.fetchone()
		rows = cur.fetchall()
		
		for row in rows:
			print row
	
	print 'end db dump'


if __name__ == "__main__":
  main('rooms.sqlite')
