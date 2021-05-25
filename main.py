class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        # Method 1
#         count = 0
        
#         for i in stones:
#             if i in jewels:
#                 count += 1
                
#         return count



        # Method 2
#         jewelCount = {}
    
#         for i in jewels:
#             jewelCount[i] = stones.count(i)
            
#         return sum(jewelCount.values())



        # Method 3
        newSet = set(jewels)

        count = 0

        for i in stones:
            if i in newSet:
                count += 1

        return count
        

'''

U:

jewels = "Ain"
stones = "AAdSaffnnnNi"
output = 6

P:

iterate through stones; if i is in jewels, increase var count by 1

create dict jewelCount; for i in jewels, jewelCount[i] = stones.count(i); return sum(jewelCount.values())

'''

# ===============

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        # Method 1
#         counts = []

#         for i in nums:
#             x = 0
#             for j in nums:
#                 if j < i:
#                     x += 1
#                 else:
#                     continue

#             counts.append(x)            

#         return counts


        # Method 2

        counts = {}
    
        newList = sorted(nums)
        
        nums_2 = []
        
        for i in newList:
            counts[i] = newList.index(i)
            
        for i in nums:
            nums_2.append(counts[i])
            
            
        return nums_2
            
        
'''

U:

[1, 2, 3, 4, 5]
output = [0, 1, 2, 3, 4]

[1, 1, 1, 2, 3]
output = [0, 0, 0, 3, 4]

[5, 4, 3, 2, 1]
output = [4, 3, 2, 1, 0]

P:

create var x, which will count integers, less than i.  Iterate through nums, returning x for i.


create dict counts; create list newList = nums.sort(); for i in newList, counts[i] = newList.index(i)
'''

# ===============

