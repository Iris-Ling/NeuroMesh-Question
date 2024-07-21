def get_num_of_subsequences(source: str, target: str) -> int:
    if source == None or target == None:
        return -1 # if source or target is none, return -1
    m = len(source) # length of source str
    n = len(target) # length of target str
    i = 0
    result = 0

    for char in target:
        # iterate through every char in target
        if char not in source:
            return -1 
        while i < m and source[i] != char:
            i += 1
        if i == m:
            result += 1
            i = 0
            # restart from the begining
            while i < m and source[i] != char:
                i+=1
            if i == m:
                return -1
        i+=1
    result+=1
    return result


if __name__ == '__main__':
    # Create some sample test
    source  = "abc"
    target = "abcbc"
    result1 = get_num_of_subsequences(source, target)
    print(result1)

    source = "abc"
    target = "acdbc"
    result2 = get_num_of_subsequences(source, target)
    print(result2)

    source = "xyz"
    target = "xzyxz"
    result3 = get_num_of_subsequences(source, target)
    print(result3)