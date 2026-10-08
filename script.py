name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))

annual_salary = salary * 12
salary_after_tax = annual_salary * 0.87

print("Hello, " + name)
print("Next year you will be", age + 1)
print("Annual salary:", annual_salary)
print("Salary after tax:", round(salary_after_tax, 2))

text = "Python is easy and Python is interesting"

print("First occurrence of Python:", text.find("Python"))
print("Last occurrence of Python:", text.rfind("Python"))
print("First word:", text[0:6])
print("Reversed text:", text[::-1])

print("Your name has", len(name), "characters")

search_word = input("Enter a word to search: ")
occurrences = text.lower().count(search_word.lower())

print("Number of occurrences:", occurrences)
