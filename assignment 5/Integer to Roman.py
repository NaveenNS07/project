class Solution:
    def intToRoman(self, num: int) -> str:
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        r = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                r += syms[i]
                num -= val[i]
            i += 1
        return r