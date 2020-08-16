filename = 'steve_jobs.txt'
with open(filename) as target:
    contents = target.read()

the_number = contents.lower().count('the')
print(the_number)
