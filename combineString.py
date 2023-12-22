def solveWordCombination(wordList, target):
    # initiate a dictionary to keep track of the words
    wordDict = {}
    # print('wordList', wordList)
    # print('target', target)
    for i in range(len(wordList)):
        # add the word to the dictionary
        wordDict[wordList[i]] = i
        # 
        # check the remaining string by removing the current word from the target
        remaining = target.replace(wordList[i], "")
        
        # check if the remaining string is in the dictionary
        if remaining in wordDict:
            return (wordList[i], remaining)
    return None
        
#test cases
print(solveWordCombination(["ab", "bc", "cd"], "abcd"))
print(solveWordCombination(["ab", "bc", "cd"], "cdab"))
print(solveWordCombination(["ab", "bc", "cd"], "abab"))
