from threading import Thread
import time
import random
import queue

counter = 0
# Create a queue object
job_queue = queue.Queue() #thinks to be printed out
counter_queue = queue.Queue()  #amounts by whivj we increase the counter


def increment_manager():
	global counter
	while True:
		increment = counter_queue.get()  # this waits until an item is available and locks the queue
		time.sleep(random.random())
		old_counter = counter
		time.sleep(random.random())
		counter = old_counter + increment
		time.sleep(random.random())
		job_queue.put((f'New counter value {counter}', '------------')) #punem ceva in job_queue
		time.sleep(random.random())
		counter_queue.task_done()  # this unlocks the queue
# 		task_done este o metoda a obiectului Queue Indicate that a formerly enqueued task is complete.
# 		For each get() used to fetch a task,
#         a subsequent call to task_done() tells the queue that the processing on the task is complete.


# printer_manager and increment_manager run continuously because of the `daemon` flag.
Thread(target=increment_manager, daemon=True).start()



def printer_manager():
	while True:
		for line in job_queue.get():
			time.sleep(random.random())
			print(line)
		job_queue.task_done()

# printer_manager and increment_manager run continuously because of the `daemon` flag.
Thread(target=printer_manager, daemon=True).start()


def increment_counter():
	counter_queue.put(1)
	time.sleep(random.random())


worker_threads = [Thread(target=increment_counter) for thread in range(10)]

for thread in worker_threads:
	time.sleep(random.random())
	thread.start()

for thread in worker_threads:
	thread.join()  # wait for it to finish

counter_queue.join()  # wait for counter_queue to be empty
job_queue.join()  # wait for job_queue to be empty