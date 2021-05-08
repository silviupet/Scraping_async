from threading import Thread
import time
import random

counter = 0

def increment_counter():
	global counter
	time.sleep(random.randint(0, 2))
	counter += 1
	time.sleep(random.randint(0, 2))
	print(f'New counter value: {counter}')
	time.sleep(random.randint(0, 2))
	print('-----------')



for x in range(10):
	t = Thread(target=increment_counter)
	time.sleep(random.randint(0, 2))
	t.start()
	#t.join()
	#daca pun join() blocheaza tradul pana la executia lui si apoi trece la urmatorul thread.
# in acest caz nu se intercaleaza rezultatele
