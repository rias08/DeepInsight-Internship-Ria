name = 'kesha'
new_name = ''
for c in name:
    if c == 'e':
        c = '3'
    if c == 's':
        c = '$'
    if c == 'a':
        c = '@'
    new_name += c
    
print(new_name)