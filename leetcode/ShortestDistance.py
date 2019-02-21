"""* Shortest Word Distance
 * Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
 * Example:
 * Assume that words = [practice, makes, perfect, coding, makes].
 * Input: word1 = coding, word2 = practice
 * Output: 3
 * Input: word1 = makes, word2 = coding
 * Output: 1
 * Note:
 * You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
 * Time Complexity: O(n); Space Complexity: O(1)
"""
class ShortestDistance(object):
    def distance(self, words, word1, word2):
        mindistance = len(words)
        index1 = -1
        index2 = -1
        for i in range(len(words)):
            if word1 == words[i]:
                index1 = i
            if word2 == words[i]:
                index2 = i
            if index1 >= 0 and index2 >= 0:
                mindistance = min(abs(index1-index2), mindistance)
        return mindistance

sd = ShortestDistance()
words = ["practice", "makes", "perfect", "coding", "makes"]
print(sd.distance(words, "coding", "practice"))
print(sd.distance(words, "makes", "coding"))
