import tkinter as tk
from tkinter import messagebox

# Function to check if a number is prime
def is_prime(n):
	if n <= 1:
		return False
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
	return True

# Function to get all prime numbers up to a given number
def get_primes_up_to(n):
	primes = []
	for num in range(2, n + 1):
		if is_prime(num):
			primes.append(num)
	return primes

# Function to display prime numbers in the result text box
def show_primes():
	try:
		# Get user input and convert to integer
		user_input = int(entry.get())
		# Get all prime numbers up to the user input
		primes = get_primes_up_to(user_input)
		formatted_primes = ""
		# Format the prime numbers, 5 per line
		for i in range(len(primes)):
			if i > 0 and i % 5 == 0:
				formatted_primes += "\n"
			formatted_primes += str(primes[i]) + " "
		# Set the formatted prime numbers in the result text box
		result_text.set("enter Prime numbers:\n" + formatted_primes.strip())
	except ValueError:
		# Show error message if input is not a valid number
		messagebox.showerror("Invalid input", "Please enter a valid number")

# Set up the GUI
root = tk.Tk()
root.title("Prime Number Finder")
root.configure(bg="red")  # Set the background color to red


# Label for user instruction
tk.Label(root, text="Enter a number:").pack()

# Entry widget for user input
entry = tk.Entry(root)
entry.pack()

# StringVar to hold the result text
result_text = tk.StringVar()
# Label to display the result
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

# Button to trigger the prime number calculation
tk.Button(root, text="Find Primes", command=show_primes).pack()

# Button to close the application
tk.Button(root, text="Close", command=root.destroy).pack()

# Start the GUI event loop
root.mainloop()