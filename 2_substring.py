str_x = "Emma is a good developer. Emma is a writer"
substring = "Emma"
count = 0
for i in range(len(str_x)):
    if str_x [i:i+len(substring)]==substring:
        count+=1
print("Emma appeared",count,"times")
