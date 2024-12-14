lines=None
with open('data.txt') as file:
    lines=file.readlines() #read txt file line by line and assign for lines

if not lines: #check that file has lines or not.If don't have lines,print as something went wrong
    print("Something went wrong")
    exit() #exist after occur

marks_lines=lines[1:] #assign lines from 2nd line to last line for marks_lines

subject_marks={}

for line in marks_lines: #(praneeth,science,75),(Saman,Science,89).....
    entries=line.split(',') #avid commas haven between 2 values and assign for entries

    name=entries[0].strip() 
    subject=entries[1].strip()
    marks=int(entries[2].strip())

    if subject not in subject_marks:
       subject_marks[subject]={}

    subject_marks[subject][name]=marks

print(subject_marks)





    
    