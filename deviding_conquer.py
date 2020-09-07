# finding the highest number using dividing-conquer 
# split list in half and find the highest number (value)

list = [6, 4, 2, 8, 16, 12, 24, 20]

range_begin = 0
range_end = len(list) - 1
range_size = range_end

half_devider = 0

done = False

while(not done):

    sum_left = 0
    sum_right = 0
 

    half_devider = int(range_end - range_begin / 2)
    for i in range(range_begin, range_end):
        sum_left += list[i];
        sum_right += list[half_devider + i]
  
    
    if sum_right > sum_left:
        range_begin = half_devider
        range_end = range_begin + range_size
    else:
        range_begin = range_begin - range_size
        range_end = range_begin + range_size
      
          
    range_size = range_end - range_begin
    half_devider = int(range_size / 2)
    
    if half_devider < 1:
        done = True
