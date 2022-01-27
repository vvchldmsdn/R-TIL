def group_anagrams(words):
    import copy

    new_words = []
    
    # 글자들 단어 단위로 쪼개서 리스트로 묶기
    for i in range(len(words)):
        a = []
        for j in range(len(words[i])):
            a.append(words[i][j])
        new_words.append(a)
    
    print(new_words)
    
    # 글자들 알파벳 순서대로 정렬하기
    new_words2 = copy.deepcopy(new_words)

    for i in range(len(new_words)):
        new_words2[i].sort()
        new_words[i].sort()
        new_words[i].append(words[i]) # 출신 명시

    new_words.sort()
    new_words2.sort()

    print(new_words2)
    print(new_words)


    # 그룹핑하기
    ans = []
    
    while len(new_words) > 0:
        a = []
        cnt = new_words2.count(new_words2[0])
        
        for i in range(cnt):
            a.append(new_words[0][-1])
            new_words.pop(0)
            new_words2.pop(0)
        ans.append(a)

    return ans


print(group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
    
