x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("List X contains %d objects" % len(x_list))
print("List Y contains %d objects" % len(y_list))
print("Therefore, our Big List contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Loading...")
if big_list.count(x) == 10 and y_list.count(y) == 10:
    print("Great!")
