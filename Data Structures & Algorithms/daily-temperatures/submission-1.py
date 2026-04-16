class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) # initialise array with deafault values 0 of length as same as temperatures

        stack = [] # contains pair of [temp, index]

        for index,value in enumerate(temperatures):
            while stack and value>stack[-1][0]:
                Stacktemp,stackInd = stack.pop()
                res[stackInd] = index - stackInd

            stack.append([value,index])

        return res