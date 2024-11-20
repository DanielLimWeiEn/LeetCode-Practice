class Solution:
    def addBinary(self, a: str, b: str) -> str:
        deltas = {
            ("0", "0") : ("0", "0"),
            ("0", "1") : ("1", "0"),
            ("1", "0") : ("1", "0"),
            ("1", "1") : ("0", "1")
        }

        len_a, len_b = len(a), len(b)

        if len_a < len_b:
            a = (len_b - len_a) * "0" + a
        elif len_b < len_a:
            b = (len_a - len_b) * "0" + b
        
        sol = ""
        carry = "0"

        for i in range(len(a) - 1, -1, -1):
            if carry == "0":
                cur_sum, cur_carry = deltas[(a[i], b[i])]
                sol = cur_sum + sol
                carry = cur_carry
            else:
                if a[i] == "1" and b[i] == "1":
                    intermediate_sum, final_carry = deltas[(a[i], b[i])]
                    final_sum, _ = deltas[(intermediate_sum, carry)]
                    sol = final_sum + sol
                    carry = final_carry
                else:
                    intermediate_sum, _ = deltas[(a[i], b[i])]
                    final_sum, final_carry = deltas[(intermediate_sum, carry)]
                    sol = final_sum + sol
                    carry = final_carry
        
        return carry + sol if carry == "1" else sol

"""
Iterate through both the strings from the back.

str1 = "1010"
           ^
str2 = "0011"
           ^
           i
Keep track of the carry and set it to 0 first.

To make it easier, pad the shorter one with 0s in front.

So using an i pointer

you sum str1[i] and str2[i]

if "0" + "0" == "0"
if "1" + "0" == "1"
if "0" + "1" == "1"
if "1" + "1" == "0" + "1" carry

"""
