# MEE 12/09/21

def anagram_check(w1,w2):
    l1 = list(w1)
    l2 = list(w2)

    s1 = l1.copy()
    s2 = l2.copy()
    s1.sort()
    s2.sort()

    if s1 == s2:
        return("The words " + w1 + ' and ' + w2 + " are anagrams.")
    else:
        return("The words " + w1 + ' and ' + w2 + " are not anagrams.")

word_one = input("Input a word: ")
word_two = input("Input another word: ")

print(anagram_check(word_one,word_two))

print(anagram_check("race","acer") == "The words " + "race" + ' and ' + "acer" + " are anagrams.")
print(anagram_check("word","worde") == "The words " + "word" + ' and ' + "worde" + " are not anagrams.")
print(anagram_check("yet","yet") == "The words " + "yet" + ' and ' + "yet" + " are anagrams.")