def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    print(count)

count_substring("ABCDCDC","CDC")
#for i in range(0, len(s)):
#    print (s[i])