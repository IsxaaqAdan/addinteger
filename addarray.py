cass Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """lYou are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        # start from the least significant digit
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                # if the current digit is less than 9, add 1 to it and return
                digits[i] += 1
                return digits
            else:
                # if the current digit is 9, set it to 0 and continue to the next digit
                digits[i] = 0
        # if all digits are 9, add 1 at the beginning and set all other digits to 0
        digits = [1] + [0] * n
        return digits
