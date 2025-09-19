h = input("Height:")

if not h.isdigit() or int(h) <= 0 or int(h) >= 9:
    h = input("Height:")
hh = int(h)
S = '  '
for i in range(1, hh+1):
    left = ' ' * (hh-i) + '#' * i
    right = '#' * i
    print(left+S+right)
