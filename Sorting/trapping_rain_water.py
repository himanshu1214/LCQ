    max_left = [0]
    max_right = [0]
    i, j = 1, 1
    tot_area = 0
    k = 0
    while i < len(height): # max left
        max_left.append(max(max_left[i-1], height[i-1]))
        i += 1
    print(max_left)
            
    while j < len(height) : # max right
        # print(j)
        max_right.append(max(max_right[j-1], height[len(height) - j]))
        j += 1
    max_right.reverse()
    # print(f"length of right is {len(max_right)}")
    # print(f"lenght of left is : {len(max_left)}")
        
    #calculate area
    while k < len(height):
        ht_val = min(max_left[k], max_right[k]) - height[k]
        if ht_val > 0: 
            tot_area += ht_val

        k += 1
    return tot_area
