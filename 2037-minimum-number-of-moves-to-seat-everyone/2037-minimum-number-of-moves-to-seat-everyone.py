class Solution:
    def minMovesToSeat(self, a: List[int], b: List[int]) -> int:
        return sum(map(abs,map(sub,sorted(a),sorted(b))))