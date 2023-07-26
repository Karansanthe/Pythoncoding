str = 'ababcderdd'
max_len = 0
curr_len = 0
set_str = set()

for i in str:
    if i in set_str:
        curr_len = 0
    else:
        curr_len += 1
        set_str.add(i)
    max_len = max(max_len, curr_len)
print(max_len)