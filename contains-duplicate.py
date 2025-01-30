
'''
Mainly the trick is that they give you the window, basically r - l which abs value equals k, u basically search in the window
as u loop thru the array, if ur right pointer reaches past the window, we remove the left most variable and shrink our window
by incrementing the left pointer. after that we normally add our new value in the right pointer and if the value of the right pointer
already exists in array itll instantly return True, if not itll loop htru the array and won't find any duplicates within that window
returning False
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap = defaultdict(int)

        l = 0

        for r in range(len(nums)):
            if abs(r - l) > k:
                hashmap[nums[l]] -= 1
                l+=1
                
            hashmap[nums[r]] += 1
            if hashmap[nums[r]] > 1:
                return True
            
        return False
    
    '''
    Initially used a hashmap and what not but i should probably use set, it saves only the numbers and not the count, which does
    save memory even though the improvement is only by constant space. 
    Heres the solution with set
    '''

    class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashset = set()

        l = 0

        for r in range(len(nums)):
            if abs(r - l) > k:
                hashset.remove(nums[l])
                l+=1
            
            if nums[r] in hashset:
                return True
                
            hashset.add(nums[r])
            
            
        return False
            

            