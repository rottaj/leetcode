class BruteForce:
  def removeAnagrams(self, words):
    anagrams = []
    left, right = {}, {}

    '''
      If words[0] is getting removed, one loop wont work.
    '''
    while len(words) > 1:
      for c in words[0]:
        if c in left:
          left[c] +=1
        else:
          left[c] = 1 
      for c in words[1]:
        if c in right:
          right[c] +=1
        else:
          right[c] = 1
      print(left, right)
      if left == right:
        print("TRUE", left, words[0])
        anagrams.append(words[0])
      words.pop(0) 
      left, right = {}, {}
      print(anagrams)


if __name__ == '__main__':
  words = ["abba","baba","bbaa","cd","cd"]
  words = ["a","b","c","d","e"]
  BruteForce().removeAnagrams(words)
