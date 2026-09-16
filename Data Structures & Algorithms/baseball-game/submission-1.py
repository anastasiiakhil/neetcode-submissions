class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        score = []
        score_sum = 0

        for i in operations:

            if i == '+' and len(score) >= 2:
                score_sum += score[-1] + score[-2]
                score.append(score[-1] + score[-2])
                
            elif i == 'C' and len(score) >= 1:
                removed_score = score.pop(-1)
                score_sum -= removed_score
                
            elif i == 'D' and len(score) >= 1:
                score_sum += 2*score[-1]
                score.append(2*score[-1])

            else:
                score.append(int(i))
                score_sum += int(i)

        return score_sum
