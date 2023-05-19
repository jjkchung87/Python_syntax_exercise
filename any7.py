def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    for num in nums:
        if num == 7:
            return True
        
    return False
    # YOUR CODE HERE 

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

nums_no_7 = [1,2,3,4,5]
nums_yes_7 = [1,2,3,7,5]