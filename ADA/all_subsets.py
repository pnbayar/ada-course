def find_all_subsets(nums):
    subsets = []
    n = len(nums)
    
    # Generate all 2^n subsets
    for i in range(2 ** n):
        subset = []
        for j in range(n):
            subset.append(nums[j])
        subsets.append(subset)
    
    return subsets


# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3]
    result = find_all_subsets(nums)
    
    print(f"Subsets of {nums}:")
    for subset in result:
        print(subset)