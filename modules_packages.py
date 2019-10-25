import module_largest
from module_largest import smallest

from package_print import sample_package
from package_print.sample_package import pick_lane

num = [1,5,9,2,0,1,2]
print(module_largest.largest(num))
print(smallest(num))

print(pick_lane('Right'))
x = sample_package.pick_colour(0)
print(x)