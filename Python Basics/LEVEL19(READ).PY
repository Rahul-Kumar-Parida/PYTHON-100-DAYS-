f = open("myfile.txt" ,'r')

i = 0
while True:
    i =i+1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of the student {i} in maths is : {m1}")
    print(f"Marks of the student {i} in eng is : {m2}")
    print(f"Marks of the student {i} in sst is : {m3}")
    print(line)

# f = open("myfile2.txt", "w")
# lines = ['line 1', 'line 2', 'line 3']
# f.writelines(lines)
# f.close()