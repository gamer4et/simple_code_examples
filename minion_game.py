"""
The exercise was taken from HackerRank
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Sample Input:
BANANA
Sample Output:
Stuart 12

"""
def minion_game(string):
    alph = "AEIOU" #vowels
    stuart_count = 0
    kevin_count = 0
    max_len = len(string)
    for i in range(max_len):
        if string[i] in alph:
            kevin_count +=  max_len -i #count of words starting from a vowel
        else:
            stuart_count += max_len-i #count of words starting from consonant
        
    if kevin_count > stuart_count:
        print('Kevin',kevin_count)
        return
    if kevin_count < stuart_count:
        print('Stuart',stuart_count)
        return
    print("Draw")
        

if __name__ == '__main__':
    s = input()
    minion_game(s)
