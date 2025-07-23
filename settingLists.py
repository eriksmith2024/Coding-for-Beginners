party_goers = {'Andrew','Barbara','Carole','David'}
print('\nparty_goers:', type(party_goers))

print('\nDid David go to the party?','David' in party_goers)

print('\nDid Kelly go to the party', 'Kelly' in party_goers)

students = {'Andrew', 'Kelly', 'Lynn', 'David'}

commons = party_goers.intersection(students)
party_students = list( commons)

print('\nStudents at the party:', party_students)
print('First student at the party:', party_students[0], '\n')