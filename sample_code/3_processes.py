from multiprocessing import Process
import time

# cand avem un task care asteapta userul sa tasteze si unul care face calcule complexe vom aplica multithreading
# cand vom avea 2 sarcini de calcule complexe vom aplica multiprocessing (practic se da un nou core la al 2-lea proces si se fac in paralel

####### SINGLE PROCESS

def ask_user():
	start = time.time()
	user_input = input('Enter your name: ')
	greet = f'Hello, {user_input}'
	print(greet)
	print('ask_user: ', time.time() - start)

def complex_calculation():
	print('Started calculating...')
	start = time.time()
	[x**2 for x in range(20000000)]
	print('complex_calculation: ', time.time() - start)
# doar pt utilizatorii windows
if __name__ =="__main__":
# With a single thread, we can do one at a time—e.g.
	start = time.time()
	ask_user()
	complex_calculation()
	print('Single thread total time: ', time.time() - start, '\n\n')


####### TWO PROCESSES


# With two processes, we can do them both at once...

# With two processes, we can do them both at once...
	process = Process(target=complex_calculation)
	process2 = Process(target=complex_calculation)


	process.start()
	process2.start()

	start = time.time()



	process.join()  # this waits for the process to finish
	process2.join()

	print('Two process total time: ', time.time() - start)

# Run this and see what happens!

