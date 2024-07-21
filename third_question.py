def get_weight(a):
    n = len(a)
    max_weight = float('-inf')
    
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + a[i]

    for i in range(n):
        for j in range(i, n):
           
            subsequence = a[i:j + 1]
            k = len(subsequence)
            subsequence_sorted = sorted(subsequence)
            # calculate mean
            sum_subseq = prefix_sums[j + 1] - prefix_sums[i]
            mean = sum_subseq / k
            
            # calculate median 
            if k % 2 == 1:
                median = subsequence_sorted[k // 2]
            else:
                median = (subsequence_sorted[k // 2 - 1] + subsequence_sorted[k // 2]) / 2
            
            # calcalate weight and update
            weight = mean - median
            if weight > max_weight:
                max_weight = weight
    
    return max_weight

if __name__ == '__main__':
    # Sample test
    n = 4
    a = [1, 3, 5, 9]
    result = get_weight(a)
    print(result)
