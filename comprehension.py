### List Comprehension ###

## Square of each number
# numbers = [1,2,3,4]
# new_number = [number**2 for number in numbers]
# print("Square >>", new_number)

## Uppercase
# small_cased = ["a","b","c","d","e",]
# upper_cased = [letter.upper() for letter in small_cased]
# print('Upper cased >>', upper_cased) 

## Even Numbers
# numbers = [1,24,35,67,81,2,45,89,12]
# even_numbers = [number for number in numbers if number % 2 == 0]
# print("Even Numbers are >>", even_numbers)

## Make list, from dictionary keys using list comprehension
# employees_hours = {
#     "Alice": 45,
#     "Bob": 39,
#     "Clara": 41,
#     "Dave": 38,
#     "Eve": 42,
#     "Frank": 44
# }

# overtime_employee = [name for ( name, hours) in employees_hours.items() if hours > 40]
# overtime_employee = [[name, hours] for (name,hours) in employees_hours.items()]
# print("Over time employees >> ", overtime_employee)

### Set Comprehension ###

## Capitalized the first letter
# words = set(["KING", "QUEEN", "MEN", "DREAMS", "MEN", "king"])
# capitalized_words = {each_word.title() for each_word in words}
# print("Capitalized Words:", capitalized_words)

## Even Numbers
# numbers = [1,24,35,12,67,2,24,81,2,45,89,12]
# even_numbers = {number for number in numbers if number%2 == 0}
# print("Even numbers >>", even_numbers)

### Dictionary Comprehension ###

## Use dictionary comprehension to apply a 10% discount to each price
# products = {"laptop": 1200, "Phone": 700, "table": 450, "monitor": 300}
# discount_products ={product: price * 0.9 for product, price in products.items()}
# discount_products ={product: price * 0.9 for product, price in products.items() if price * 0.9 > 500}
# print("discounted products >> ", discount_products)

## Nesting Comprehension
# scores = [["dennis", 10], ["david", 12], ["Joseph", 13]]
# scores_dict = {name: score for name, score in scores if score > 10}
# scores_dict = {name: score for name, score in [each_score for each_score in scores if each_score[1] > 10]}
# print("Score board >>", scores_dict)


# book_time = [
#     ['The Great Gatsby', '10:30'], 
#     ['To kill a Mockingbird', '11:15'], 
#     ['1984', '14:20',],
#     ['The Great Gatsby', '16:00'], 
#     ['The Catcher in the Rye', '18:50'], 
#     ['1984', '09:00'], 
#     ['To Kill a Mockingbird', '13:00'], 
#     ]

# shifts = [
#     ("Alice", "Monday", "Morning"),
#     ("Frank", "Monday", "Morning"),
#     ("Bob", "Monday", "Evening"),
#     ("Charlie", "Tuesday", "Afternoon"),
#     ("David", "Tuesday", "Morning"),
#     ("Eve", "Wednesday", "Evening"),
#     ("Frank", "Wednesday", "Morning"),
#     ("Grace", "Thursday", "Afternoon"),
#     ("Alice", "Friday", "Morning"),
#     ("Bob", "Friday", "Afternoon"),
#     ("Charlie", "Monday", "Afternoon"),
# ]
# organized_shifts = {day: {
#     shift: [employee for employee, shift_day, shift_time in shifts if shift_day == day and shift_time == shift] for shift in {"Morning", "Afternoon", "Evening"}
# } for day in set(day for employee, day, shift in shifts)
# }
# print(organized_shifts)

# grades = [
#     ("Alice", "Math", 90),
#     ("Bob", "Math", 85),
#     ("Charlie", "Science", 92),
#     ("Alice", "Science", 88),
#     ("Bob", "History", 75),
#     ("Charlie", "Math", 82),
#     ("Alice", "History", 78),
#     ("Bob", "Science", 90),
#     ("Charlie", "History", 85),
# ]
# organized_grades = { name : {
#         subject: [mark for student_name, student_subject, mark in grades if student_name == name and student_subject == subject] for subject in {'Math', 'Science', 'History'}
# } for name in set(name for name, subject, marks in grades)}
# # print([name for name in grades])
# print("organized_grades", organized_grades)

shifts = [
    ("Alice", "Monday", "Morning"),
    ("Frank", "Monday", "Morning"),
    ("Bob", "Monday", "Evening"),
    ("Charlie", "Tuesday", "Afternoon"),
    ("David", "Tuesday", "Morning"),
    ("Eve", "Wednesday", "Evening"),
    ("Frank", "Wednesday", "Morning"),
    ("Grace", "Thursday", "Afternoon"),
    ("Alice", "Friday", "Morning"),
    ("Bob", "Friday", "Afternoon"),
    ("Charlie", "Monday", "Afternoon"),
]
 
sorted_shifts = { day: {
     shift : [name for name, day, employee_shift in shifts if employee_shift == shift and day == day] for shift in {'Morning', 'Evening', 'Afternoon'}
 } for day in set(day for name, day, time in shifts)
}

# print([name for name, employee_shift, time in shifts  ])
print("Sorted shifts >> ", sorted_shifts)