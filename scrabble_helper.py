"""
Developed mainly to help scrabble players to make the most score out a set of letters.
Checks what English words can be formed from given jumbled letters.
Reference for the valid English words is in dictionary.txt so make sure it is in the same directory as the script.
Input letters should only be alphabets and input blank tiles count should be a whole number.
Blank tiles act as any letter but they do not have score.
Output is displayed in two forms. (1) Sorted by highest score, and (2) sorted by word length
Program will loop until user input 'Y' when asked to exit.
"""

LETTER_SCORES = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
dictionary = []
end = False

with open('dictionary.txt') as f:
    dictionary = f.read().splitlines()

while not end:
    outputWords = []
    inputLetters, inputBlankTileCount = '', ''

    while not inputLetters.isalpha() and not inputBlankTileCount.isnumeric():
        inputLetters = input('Input letters: ').upper()
        inputBlankTileCount = input('How many blank tiles do you have? ')

    for word in dictionary:
        blankTileCount = int(inputBlankTileCount)
        isWordSubset = True
        wordScore = 0
        for letter in word:
            letterScore = LETTER_SCORES[ord(letter) - 65]
            if word.count(letter) > inputLetters.count(letter):
                if blankTileCount > 0:
                    blankTileCount -= 1
                    letterScore = 0
                else:
                    isWordSubset = False
                    break
            wordScore += letterScore
        if isWordSubset:
            outputWords.append([wordScore, word])

    print('Sorted by Score')
    for score, word in sorted(outputWords, key=lambda x: (x[0], len(x[1])), reverse=True)[0:19]:
        print('{score:02d}'.format(score=score), word)

    print('\nSorted by Length')
    for score, word in sorted(outputWords, key=lambda x: (len(x[1]), x[0]), reverse=True)[0:19]:
        print('{score:02d}'.format(score=score), word)

    end = True if input('Exit? [Y/N]: ').upper() == 'Y' else False
