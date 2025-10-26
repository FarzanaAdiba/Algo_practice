def LIS_len(nums):
    if not nums:
        return 0,[]  # Return 0 and an empty list if the input is empty
    
    n = len(nums)
    dp = [1] * n  # Initialize the dp array with 1s

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:  # Check if we can extend the subsequence
                dp[i] = max(dp[i], dp[j] + 1)

    #return max(dp)  # The length of the longest increasing subsequence

    max_length = max(dp)  # Store the maximum length of the longest increasing subsequence
    # To reconstruct the longest increasing subsequence, we can backtrack through the dp array
    end_idx=-1
    #go backward
    for i in range(n-1, -1, -1):
        if dp[i] == max_length:
            end_idx = i
            break
    #store in a list
    lis_sub=[]
    current_len=max_length
    for i in range(end_idx, -1, -1): #it checks from the end index to the beginning of the list, looking for elements that are part of the longest increasing subsequence. If it finds an element that has a dp value equal to the current length of the subsequence, it adds that element to the lis_sub list and decrements the current length by 1. This process continues until it has found all elements of the longest increasing subsequence.
        if dp[i] == current_len:
            lis_sub.append(nums[i])
            current_len -= 1
    #reverse the list
    lis_sub.reverse()
    return max_length, lis_sub  # Return both the length and the longest increasing subsequence

if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print("Length of the longest increasing subsequence is:", LIS_len(nums))
    length, subsequence = LIS_len(nums)
    print("Longest increasing subsequence is:", subsequence)
    
