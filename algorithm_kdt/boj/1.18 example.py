# 2789
strings = input()
new_list = []
for string in strings:
    if string not in 'CAMBRIDGE':
        new_list.append(string)
result = ''.join(new_list)
print(result)

# 2675
T = int(input())
for t in range(T):
    R, S = input().split()
    result = ""
    for s in S:
        result += s * int(R)
    print(result)

# 10988
word = input()
reverse_word = word[::-1]
print(int(word == reverse_word))

# 17249
string = input()
# print(string.index("("))  # 12
# print(string[:12].count("@"))  # 4
print(string[:string.index("(")].count("@"), string[string.index("("):].count("@"))

# 2941
string = input()
change = ["c=", "c-","dz=","d-","lj", 'nj', 's=','z=']

for i in change:
    new_string = string.replace(i,"*")
print(len(new_string))   

# 10809
S = input()
# print(ord("a"))  # 97
# print(ord("z"))  # 122

for i in range(97, 123):
    print(S.find(chr(i)), end=" ")