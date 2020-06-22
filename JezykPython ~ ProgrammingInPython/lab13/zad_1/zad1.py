import sys
sys.path.append('build/lib.linux-x86_64-3.7')

import mod

print(mod.met(1,2))                       #3
print(mod.met(1,2,5))                    #8
print(mod.met(1,2,5,[2,3,4]))       #17