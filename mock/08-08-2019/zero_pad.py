#!/usr/bin/env python3

# file: zero_pad.py
# date: 08-08-2019
# author: Timothy Siwula
# chmod +x zero_pad.py
# execute:
#           python3 zero_pad.py
#           python3 zero_pad.py "area 59" 4
#           echo "area 59" 4 | ./zero_pad.py

class ZeroPadder:
    def zeroPadInput(self, input, padSize) -> str:

        if not input:   # check valid inputs
            return "error"

        result = ""
        start = st = 0
        digit_flag = text_flag= False

        for i in range(len(input)):
            if input[i].isnumeric():    # is a digit
                if not digit_flag:
                    digit_flag = True
                    start = i
                else:
                    if i + 1 == len(input):         # is end of input
                        num = input[start:i + 1]
                        prefix = '0' * (padSize - (i - start) - 1)
                        new_num = prefix + num
                        result += new_num
                        digit_flag = False
                    elif not input[i + 1].isnumeric():      # is end of number
                        num = input[start:i + 1]
                        prefix = '0' * (padSize - (i - start) - 1)
                        new_num = prefix + num
                        result += new_num
                        digit_flag = False
            else:   # is text
                if not text_flag:   # is start of text
                    text_flag = True
                    st = i
                else:   # is end of input
                    if i+1 == len(input):
                        result += input[st:i+1]
                        return result
                    if input[i+1].isnumeric():  # is end of text
                        result += input[st:i+1]
                        text_flag = False
        return result

# run locally
zeroPadder = ZeroPadder()

# # test case 1
test1_param_a = "area 59"
test1_param_b = 4
test1_expected = "area 0059"
test1_actual = zeroPadder.zeroPadInput(test1_param_a, test1_param_b)
print("")
print("--------------------- test case 1 ---------------------------")
print("     input's:            {`"+ test1_param_a + "`, " + str(test1_param_b)+"}")
print("     expected result:    `" + str(test1_expected)+"`")
print("     actual result:      `" + str(test1_actual)+"`")
print("")

# test case 2
test2_param_a = "123 Foo st"
test2_param_b = 5
test2_expected = "00123 Foo st"
test2_actual = zeroPadder.zeroPadInput(test2_param_a, test2_param_b)
print("")
print("--------------------- test case 2 ---------------------------")
print("     input's:            {`"+ test2_param_a + "`, " + str(test2_param_b)+"}")
print("     expected result:    `" + str(test2_expected)+"`")
print("     actual result:      `" + str(test2_actual)+"`")
print("")

# # test case 3
test1_param_a = "123 Foo st"
test1_param_b = 2
test1_expected = "123 Foo st"
test1_actual = zeroPadder.zeroPadInput(test1_param_a, test1_param_b)
print("")
print("--------------------- test case 3 ---------------------------")
print("     input's:            {`"+ test1_param_a + "`, " + str(test1_param_b)+"}")
print("     expected result:    `" + str(test1_expected)+"`")
print("     actual result:      `" + str(test1_actual)+"`")
print("")

# # test case 4
test1_param_a = "Area59asdf234"
test1_param_b = 4
test1_expected = "Area0059asdf0234"
test1_actual = zeroPadder.zeroPadInput(test1_param_a, test1_param_b)
print("")
print("--------------------- test case 4 ---------------------------")
print("     input's:            {`"+ test1_param_a + "`, " + str(test1_param_b)+"}")
print("     expected result:    `" + str(test1_expected)+"`")
print("     actual result:      `" + str(test1_actual)+"`")
print("")
