class Solution(object):
    def backtrack(self, candidates, temp, remaining, idx, answer):
        if idx == len(candidates):
            if remaining == 0:
                answer.append(temp[:])
            return

        if candidates[idx] <= remaining:
            temp.append(candidates[idx])
            self.backtrack(candidates, temp, remaining - candidates[idx], idx, answer)
            temp.pop(-1)
        self.backtrack(candidates, temp, remaining, idx + 1, answer)

        return answer

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ## TC = O(2^(T/M)) T = target, M = minimum candidate
        ## SC = O(T/M) + O(T/M)

        answer = self.backtrack(candidates, [], target, 0, [])
        return answer   