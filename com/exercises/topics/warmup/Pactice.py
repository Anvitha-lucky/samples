import random
from collections import Counter

ll=[random.randrange(1,25,3) for i in range(1,20)]
print(ll)

print(Counter(ll))
dd=dict(Counter(ll))
