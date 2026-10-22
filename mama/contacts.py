contacts = {
    'number': 4,
    'students': 
    [
        {'name': 'Alice', 'phone': '123-456-7890'},
        {'name': 'Bob', 'phone': '987-654-3210'},
        {'name': 'Charlie', 'phone': '555-555-5555'},
        {'name': 'David', 'phone': '111-222-3333'}
    ]
}

phones = [student['phone'] for student in contacts['students']]
print(phones)