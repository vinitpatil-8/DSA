class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        for i in range(len(str(n))):
            digit = 0
            digit = n%10
            product = product * digit
            sum = sum + digit
            n = int(n/10)
        return product - sum