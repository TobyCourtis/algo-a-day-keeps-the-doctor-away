class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs: list) -> str:
        # write your code here
        out = ""
        for string in strs:
            # encode 'toby' as '4#toby'
            out += f"{len(string)}#{string}"
        return out

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str: str) -> list:
        out = []
        i = 0
        while i < len(str):
            # 1. find integer value before hastag e.g 4 or 10
            length = ""
            while str[i] != "#":
                length += str[i]
                i += 1
            length = int(length)
            # read the word after hashtag character of length 'length'
            out.append(str[i + 1: i + 1 + length])
            # increment counter to begin from next word
            i += length + 1

        return out


# write your code here


s = Solution()
input_list = ["lint", "code", "love", "you"]
out = s.encode(input_list)

print(out)

output_list = s.decode(out)
print(output_list)

assert input_list == output_list
