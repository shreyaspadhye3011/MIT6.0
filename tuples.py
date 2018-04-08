test = (1, 2, 3, 4, 5);

# accessing
print test[1];		# prints 2
print test[-1];		# prints 5
# print test[6];	# throws error

# splicing
print test[1:3];	# first three elements
print test[:3];		# first three elements
print test[3:5];	# from 4th element till 5th element
print test[3:];		# from 4th element till 5th element

print test[3:4];	# IMP : gives (4,) - strange result. Keep in mind while programming
print test[3:3];	# gives ()
print test[3:9];	# no issues. Even if the last index surpasses, it will print output until it gets valid 					index. In this case - (4, 5)

print test[6:8];	# IMP - throws no error but gives (). Rememeber while debugging

test2 = (1, 2, 3, 4, 5, 6, 7, 8);
print test2[3:5];
print test2[2:5];

