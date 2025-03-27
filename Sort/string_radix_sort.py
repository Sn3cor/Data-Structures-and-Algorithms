def str_radix_sort(arr):
    max_len=len(max(arr,key=len))

    for i in range(max_len-1,-1,-1):
        arr = counting_sort(arr,i)

    return arr


def counting_sort(arr,index):
    output = [""]*len(arr)
    count = [0]* (26 + 1)
    min_ascii = ord('a')-1


    for string in arr:
        char = ord(string[index])-min_ascii if index < len(string) else 0
        count[char]+=1


    for i in range(1,27):
        count[i]+=count[i-1]

    for string in reversed(arr):
        char = ord(string[index])-min_ascii if index < len(string) else 0
        count[char]-=1
        output[count[char]]=string

    return output

strings = ["tygrys", "kot", "wilk", "trysyg", "wlik", "sygryt", "likw", "tygrys"]
sorted_strings = str_radix_sort(strings)
print(sorted_strings)
