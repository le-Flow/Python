List = open("txt_aoc1.txt", "r")
content = List.readlines()
count=1
increase = 0
for count in range(0,len(content)): 
    try:
        if content[count] > content[count - 1]:
            increase += 1
    except:
        pass
    count += 1
    
print(str(increase))