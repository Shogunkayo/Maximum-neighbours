x = [1,1,1,2,3,3,4,4,4,5]

def address(num):
    count_left = [0 for _ in range(len(num))]
    count_right = [0 for _ in range(len(num))]
    first_shortlist = []
    second_shortlist = []
    
    for i in range(len(num)):
        for j in range(len(num)):
            if num[j] < num[i]:
                count_left[i] += 1
            elif num[j] > num[i]:
                count_right[i] += 1
    #print(count_left)
    #print(count_right)

    for i in range(len(num)):
        first_shortlist.append((count_left[i]-count_right[i])**2)
    #print(first_shortlist)
    
    least = min(first_shortlist)

    for i in range(len(num)):
        if first_shortlist[i] == least:
            second_shortlist.append(num[i])
    #print(second_shortlist)
    print("Person should stay at",min(second_shortlist))
    
address(x)
    
