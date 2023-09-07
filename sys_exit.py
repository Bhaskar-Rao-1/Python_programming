import sys
if len(sys.argv)<2:
    sys.exit("need one argv")
elif len(sys.argv)>2:
    sys.exit(" more indexses")

print("my name is",sys.argv[1])