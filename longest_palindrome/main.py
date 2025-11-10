import math

class Solution:

    def is_palindrome(self, s: str):
        center = len(s) / 2
        if len(s) == 1:
            return True
        elif center.is_integer():
            center = int(center)
            left = s[0:center] 
            right = s[center:]
            return left == right[::-1]
        else:
            center = math.floor(center)
            left = s[0:center] 
            right = s[center + 1:]
            return left == right[::-1]

    def get_character(self, index: int, s: str):
        if index < len(s) and index >= 0:
            return s[index]
        return None

    def palindrome_search(self, n: int, s: str) -> str:
        palindrome = self.get_character(n, s)
        left_index = n - 1
        right_index = n + 1
        while True:
            left = self.get_character(left_index, s)
            right = self.get_character(right_index, s)

            if left != None and right != None and self.is_palindrome(left + palindrome + right ):
                left_index -= 1
                right_index += 1
                palindrome = left + palindrome + right
            elif left != None and self.is_palindrome(left + palindrome):
                palindrome = left + palindrome
                left_index -= 1
            elif right != None and self.is_palindrome(palindrome + right):
                palindrome = palindrome + right
                right_index += 1
            else:
                break
        return palindrome

    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            new = self.palindrome_search(i, s)
            if len(new) > len(longest):
                longest = new
        return longest


def main():
    my_solution = Solution()
    STRING_WITH_PALINDROME = "aba"
    answer = my_solution.longestPalindrome(STRING_WITH_PALINDROME)
    print("IS PALINDROME: ", answer)

main()
