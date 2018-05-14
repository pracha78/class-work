largest = None
for email in emaildict:
    count = emaildict[email]
    if largest is None or count > largest :
        largest = count
        largestemail = email
print('Largest:', largestemail, largest)