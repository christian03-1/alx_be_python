task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

print(f"Reminder: '{task}' is a {priority} priority task" + (" that requires immediate attention today!" if time_bound == "yes" else ". Consider completing it when you have free time."))
