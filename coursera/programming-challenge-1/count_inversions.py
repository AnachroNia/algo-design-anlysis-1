#Simple brute force method, runs in O(n^2), to get a feel for the problem.
def brute_force():
    inversions = 0
    for i in xrange(len(numbers)):
        print str(i)+" --- "+str(numbers[i])
        for j in xrange(i):
            if(numbers[i] < numbers[j]):
                inversions+=1

    print "There are "+str(inversions)+" inversions"


def sort_and_count_inversions(list):
    length = len(list)
    if(length<2):
        #Lists of length 0 or 1 have 0 inversions
        return list, 0

    first_half, second_half = split_list(list)

    sorted_first_half, left_inversions = sort_and_count_inversions(first_half)
    sorted_second_half, right_inversions = sort_and_count_inversions(second_half)
    sorted_list, split_inversions = merge_and_count_split_inversions(sorted_first_half, sorted_second_half)

    return merge_sort(list), left_inversions + right_inversions + split_inversions

def merge_and_count_split_inversions(first_half, second_half):
    inversions = 0

    sorted = []
    i = 0
    j = 0
    for num in xrange(len(first_half)+len(second_half)):
        if(i == len(first_half)):
            #all elements in first_half have been merged, add the rest of second_half
            sorted += second_half[j:]
            #Stop looping, we have a complete output
            break

        if(j == len(second_half)):
            #all elements in second_half have been merged, add the rest of first_half
            sorted += first_half[i:]
            #Stop looping, we have a complete output
            break


        if(first_half[i] < second_half[j]):
            #Add first_half[i] to sorted
            sorted.append(first_half[i])
            i+=1

        else:
            #Add second_half[j] to sorted
            sorted.append(second_half[j])
            #If we are at index i, first_half[i] is the next element to be added from first_half to sorted
            #len(first_half) - i is the amount of elements remaining in first_half (can be 0)
            #When we add an element from second_half, we increment inversions by this amount
            inversions += (len(first_half) - i)
            j+=1

    return sorted, inversions





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
            #all elements in first_half have been merged
            output += second_half[j:]
            break

        if(j == len(second_half)):
            #all elements in second_half have been merged
            output += first_half[i:]
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


numbers = [int(num.strip()) for num in open('IntegerArray.txt')]
print sort_and_count_inversions(numbers)