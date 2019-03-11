#! python3
'''
https://leetcode.com/problems/group-anagrams/
--
anagram def: a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.
--
e.g. [ate, eat, tea] are all anagrams of each other.
'''

class Solution:
    def groupAnagrams(self, strs):
        cache = {}

        # for each word, sort all chars in the word
        for word in strs:
            key = ''.join(sorted(word))
            if cache.get(key) == None:
                cache[key] = []
                cache[key].append(word)
            else:
                cache[key].append(word)

        result = []

        # aggregate all 1D list's into a 2D list
        for key in cache:
            local_list = cache[key]
            result.append(local_list)

        return result

# def main():
#     test = Solution()
#     print("main solution....")
#
# main()
