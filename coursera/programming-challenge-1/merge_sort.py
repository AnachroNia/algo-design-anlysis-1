def split_list(list):
    length = len(list)
    if(length<2):
        #Lists of length 0 or 1 cannot be split
        return list

    half_length = length/2 #Rounded down if .5
    if(length % 2 == 0):
        #Length is even, we can have two equal lists
        first_half = list[:half_length]
        second_half = list[half_length:]
        

    else:
        #Length is odd, two differently sized lists, we make first_half 1 element larger than second_half
        first_half = list[:half_length+1]
        second_half = list[half_length+1:]

    return first_half, second_half


def merge_sort(list):
    length = len(list)
    if(length<2):
        #Lists of length 0 or 1 are considered to be sorted
        return list

    #If we get here, we have a list of length 2 or more, need to use merge sort
    #Our goal is to split the list into two halves, and then sort these recursively, assigning their sorted forms to first_half and second_half
    #We then merge these sorted lists to give us out sorted output

    first_half, second_half = split_list(list)

    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)

    return merge(first_half, second_half)

#Merge two half lists into one
def merge(first_half, second_half):
    output = []
    i = 0
    j = 0
    for num in xrange(len(first_half)+len(second_half)):
        if(i == len(first_half)):
            #all elements in first_half have been merged, add the rest of second_half
            output += second_half[j:]
            #stop looping, we have complete output
            break

        if(j == len(second_half)):
            #all elements in second_half have been merged, add the rest of first_half
            output += first_half[i:]
            #stop looping, we have complete output
            break


        if(first_half[i] < second_half[j]):
            #Add first_half[i] to output
            output.append(first_half[i])
            i+=1

        else:
            #Add second_half[j] to output
            output.append(second_half[j])
            j+=1

    return output

print merge_sort([9,4,6,2,0,3,-6])