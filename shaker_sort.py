import random

def shaker_sort(list):
    
    upper = len(list) - 1
    lower = 0
    
    swap = not upper - lower < 1
    
    while(swap):
        swap = False
        
        for i in range(lower, upper, 1):
            if list[i+1] < list[i]: 
                list[i], list[i+1] = list[i+1],  list[i]
                swap = True
                
        if not swap:
            break
        
        upper = upper - 1
          
        for i in range(upper, lower, -1):
            if list[i-1] > list[i]:
                list[i], list[i-1] = list[i-1],  list[i]
                swap = True

        lower = lower + 1
        
    return list


list = random.choices(range(100),k=5) # test case
sorted_list = sorted(list.copy()) # correct result
finish = shaker_sort(list) # shaker sorted
if not sorted_list==finish: # not correct
    print(f"""Test:        {list}

Sorted:      {sorted_list}

ShakerSorted:{finish}""")

# shaker_sort([89, 88, 66, 13, 14, 10, 120])
