class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        l=len(nums)//2
        a=[]
        b=[]
        c=[]
        i=0
        j=0
        for x in range(l):
            a.append(nums[x])
        for y in range(l,len(nums)):
            b.append(nums[y])
        for z in range(len(nums)):
            if z%2==0:
                c.append(a[i])
                i+=1
            else:
                c.append(b[j])
                j+=1
        return c
