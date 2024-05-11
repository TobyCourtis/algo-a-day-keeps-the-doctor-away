Approach:

Followed Neetcode tutorial without looking at the code, then implemented both the linear and constant memory solutions (
fairy trivial in the end)

See iPad notes for step by step approach of below:

arr =  [1, 2, 3, 4]

pre =  [1, 2, 6, 24]

post = [24, 24, 12, 4]


out[0] = prefix[0 - 1] = default "1" * postfix[1] = "24"
    = 1 * 24 = 24
out[1] = prefix[0] = "1" * postfix[2] = "12"
    = 1 * 12 = 12
out[2] = prefix[1] = "2" * postfix[3] = "4"
    = 2 * 4 = 8
out[3] = prefix[2] = "6" * postfix[4] = default "1"
    = 6 * 1 = 6

output = [24, 12, 8, 6]