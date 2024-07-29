<!-- RATING: Easy -->
<!-- NAME: Checkdifference -->
<!-- GENERATOR: generator.py -->
# Checkdifference

A "checkdifference" is like a checksum, but different.  Start with 255, subtract the first byte, then add the second, subtract the third, and so on.  The result at the end is the checkdifference.  The input is a list of strings with their checkdifferences appended with a colon.  The colon is not part of the data.  The output is whether the checkdifference is correct or not.

# Example Input
```
[?|"~0KORaatT?|T&DLL:66
2R) xB2/UjM2wEpXEQEe:187
.z^%csYtb{6fG"=wRPCp:451
UadYL]>hT#2Zp7-.xLh\:194
```

# Example Output:
```
True
False
False
True
```
