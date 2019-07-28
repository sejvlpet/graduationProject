"""
Here we'll compare and test correctness of refernce solution (read form file) and
any file given on standard input.
""" 
refResult = [x.strip() for x in open('testResults.txt', 'r').readlines()]

countFalse = 0
for i in range(len(refResult)):
	if(input() != refResult[i]):
		countFalse += 1

print("Testů proběhlo celkem: ", len(refResult))
print("Testů celkem neprošlo: ", countFalse)