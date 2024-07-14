<!-- RATING: Medium -->
<!-- NAME: Obsolete -->
<!-- GENERATOR: rll.py -->
# Obsolete

We have acquired a legacy media company with a large digitized back catalog.  One problem, it's encrypted, and their previous IT director took a path of security by obscurity, storing the keys on a ReaLLy obsolete hard disk, and the computer it was attached to has failed.

We can't even find a compatible controller for this WD5011 series disk, but we were able to find a tool that will dump the raw magnetic transistions from the disk as a string of ones and zeros.  We do know that each key will begin with "Key:" when decoded.


# Example Input

```
00010000010010000010000010010001001000100000100100001000010001000010010010010000001000001001000000100000100010010001000010000100000010000010010000010001000010010001000010000001001000010000100000100000100100001001000000100001000010001001000100010000010010000010001001000001000100000100000100001000000100100100100000010000001000100010010000100001000100010000100010010010010010000100100100100010000010010010000100001001000100001001000100001000010010010001000010000001000100100000100100010001000010010010001001000100

```

#Example Output:
```
Key: dlN2QMsdG1KaI44xu08yqE8MYQb
```
