morse_code = {
    'A': '•-', 'B': '-•••', 'C': '-•-•', 'D': '-••', 'E': '•', 'F': '••-•', 'G': '--•',
    'H':'••••', 'I': '••' , 'J' : '•---', 'K': '-•-', 'L': '•-••', 'M': '--', 'N': '-•',
    'O':'---', 'P':'•--•', 'Q': '--•-', 'R': '•-•', 'S': '•••', 'T': '-', 'U': '••-',
    'V':'•••-', 'W':'•--', 'X': '-••-', 'Y': '-•--', 'Z': '--••',
    '1':'•----','2': '••---','3':'•••--','4':'••••-','5':'•••••','6':'-••••',
    '7':'--•••','8': '---••','9':'----•','0':'-----',' ':' '
}

input = input("Enter a sentence\n").upper()
letters = len(input)
morsed_sentence = []
for i in range(letters):
    if input[i] in morse_code:
        key = morse_code[input[i]]
        morsed_sentence.append(key)
    else:
        morsed_sentence.append(input[i])

for i in morsed_sentence:
    print(i)
