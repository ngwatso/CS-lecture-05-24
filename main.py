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