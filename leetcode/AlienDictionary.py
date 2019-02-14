"""*Alien Dictionary
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you.
You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language.
Derive the order of letters in this language.
Example 1:
Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
Output: "wertf"
Example 2:
Input:
[
  "z",
  "x"
]
Output: "zx"
Example 3:
Input:
[
  "z",
  "x",
  "z"
]
Output: ""
Explanation: The order is invalid, so return "".
Note:
You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
*"""

class AlienOrder(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if words == None and len(words) == 0:
            return ""
        result = ""
        degree = {}
        mapdict = {}
        for word in words:
            for i in range(len(word)):
                degree[word[i]] = 0

        for i in range(len(words) - 1):
            currw = words[i]
            nextw = words[i + 1]
            lenw = min(len(currw), len(nextw))
            for j in range(lenw):
                chc = currw[j]
                chn = nextw[j]
                if chc != chn:
                    lst = []
                    if chc in mapdict:
                        lst = mapdict[chc]
                    if chn not in lst:
                        lst.append(chn)
                        mapdict[chc] = lst
                        degree[chn] = degree[chn] + 1
        q = []
        for key in degree.keys():
            if degree[key] == 0:
                q.append(key)

        while q:
            ch = q.pop()
            result += ch
            if ch in mapdict.keys():
                lstn = mapdict[ch]
                for i in range(len(lstn)):
                    degree[lstn[i]] = degree[lstn[i]] - 1
                    if degree[lstn[i]] == 0:
                        q.append(lstn[i])
        if len(degree) != len(result):
            return ""
        else:
            return result
alien = AlienOrder()
print(alien.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
