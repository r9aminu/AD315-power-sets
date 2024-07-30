def subsets(nums): 
    res = [[]]
    for num in nums:
        new_res = []
        for e in res:
            new_res.append(e.copy()) 
            e.append(num) 
            new_res.append(e) 
        res = new_res 
    return res 




