#! /usr/bin python
#liyong time.slepp  mofang thread
from	time	import	sleep, ctime

def	loop0():
	print	'status loop  0  at:', ctime()
	sleep(4)
	print 'loop 0  done at:', ctime()

def	loop1():
	print	'status loop 1	at:', ctime()
	sleep(2)
	print	'loop 1	done	at:', ctime()

def	main():
	loop0()
	loop1()
	print	'statusing at:', ctime()


if __name__ =='__main__':
	main()
	
	
