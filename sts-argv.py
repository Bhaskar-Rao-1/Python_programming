import sys
if len(sys.argv)<2:
    print("need one argv")
elif len(sys.argv)>2:
    print(" more indexses")
else:
    print("my name is",sys.argv[1])