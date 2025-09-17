def solution(word):
    dictionary = dict()
    i = 0
    
    words = ['A', 'E', 'I', 'O', 'U']
    for word1 in words :
        i += 1
        dictionary[word1] = i
        for word2 in words :
            i += 1
            dictionary[word1+word2] = i
            for word3 in words :
                i += 1
                dictionary[word1+word2+word3] = i
                for word4 in words :
                    i += 1
                    dictionary[word1+word2+word3+word4] = i
                    for word5 in words :
                        i += 1
                        dictionary[word1+word2+word3+word4+word5] = i
                        
    return dictionary[word]