# n = int(input())
# word_list = []
#
# for i in range(n):
#     word = input()
#     word_list.append(word)
#
# for i in range(1, n):
#     for j in range(i):
#         # list 앞의 단어가 더 긴 경우 순서를 바꿔준다.
#         if len(word_list[i]) < len(word_list[j]):
#             temp = word_list[j]
#             word_list[j] = word_list[i]
#             word_list[i] = temp
#
#         elif len(word_list[i]) == len(word_list[j]):
#             if word_list[i] != word_list[j]:
#                 for k in range(len(word_list[i])):
#                     if ord(word_list[i][k]) < ord(word_list[j][k]):
#                         temp = word_list[j]
#                         word_list[j] = word_list[i]
#                         word_list[i] = temp
#                         break
#                     elif ord(word_list[i][k]) > ord(word_list[j][k]):
#                         break
#             else:
#                 word_list[i] = ''
#
# for w in word_list:
#     if w is not '':
#         print(w)

def convert_word(word):
    result = 0
    for k in range(len(word), 0, -1):
        result += (ord(word[k-1]) - ord('a') + 1)*pow(26, len(word)-k)
    return result


n = int(input())
word_list = {}
len_list = []

for i in range(n):
    w = input()
    word_len = convert_word(w)

    word_list[word_len] = w
    len_list.append(word_len)

len_list = list(set(len_list))
len_list.sort()

for j in len_list:
    print(word_list[j])

