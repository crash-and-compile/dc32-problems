<!-- RATING: Easy -->
<!-- NAME: Tracking 1 -->
<!-- GENERATOR: generate_gps.py -->
# Tracking 1

You are an employee of Moogle (pronounced “mogul”).  Our corporate slogan is “We aren’t too awfully evil, most of the time”.  Because Mogul owns both the most popular search engine and the most popular cell phone operating system, it is able to make money by correlating the data and targeting advertisements.

Your task is to take a string of user GPS pings gathered from their cell phone without their consent, and figure out what “places of interest” they have been.  

A place of interest is defined as a place where they spent 15 or more minutes in, within a 100 meter radius without leaving.  The list of potential places of interest is on the first line.  Each subsequent line in the input file represents one ping, pings are once per minute.  The output should be a list of POIs visited, in order that they visited them.

# Example Input

```
[[29.585351,-114.277807]]
[29.772300, -113.880326]
[29.768743, -113.887925]
[29.765186, -113.895524]
[29.761628, -113.903122]
[29.758069, -113.910720]
[29.754511, -113.918317]
[29.750951, -113.925914]
[29.747392, -113.933510]
[29.743832, -113.941106]
[29.740271, -113.948701]
[29.736710, -113.956295]
[29.733149, -113.963889]
[29.729587, -113.971483]
[29.726025, -113.979076]
[29.722462, -113.986668]
[29.718899, -113.994260]
[29.715336, -114.001851]
[29.711772, -114.009442]
[29.708207, -114.017032]
[29.585311, -114.277794]
[29.585316, -114.277826]
[29.585346, -114.277883]
[29.585287, -114.277799]
[29.585335, -114.277775]
[29.585271, -114.277849]
[29.585345, -114.277702]
[29.585380, -114.277832]
[29.585353, -114.277795]
[29.585360, -114.277826]
[29.585356, -114.277787]
[29.585249, -114.277808]
[29.585305, -114.277868]
[29.585313, -114.277797]
[29.585293, -114.277772]
[29.585365, -114.277769]
[29.585344, -114.277807]
[29.585335, -114.277798]
[29.708207, -114.017032]
[29.711772, -114.009442]
```

#Example Output:
```
[29.585351, -114.277807]
```
