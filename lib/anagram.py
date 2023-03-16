# your code goes here!
class Anagram:
    
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        anagram_list = []
        for word in word_list:
            if sorted([letter for letter in word]) == sorted([letter for letter in self.word]):
                anagram_list.append(word)
        if len(anagram_list) == 0:
            return []
        else: 
            return anagram_list

        #         None
        # if len(anagram_list) == 0:
        #     return []
        # else:
        #     return anagram_list


Anagram("enlist").match(["listen", "silent", "hippopotamus"])