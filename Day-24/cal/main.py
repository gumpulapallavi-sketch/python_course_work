'''
import logic

logic.add(2,8)
logic.mul(2,8)
logic.sub(2,8)
logic.div(2,8)
logic.rem(2,8)
logic.exp(2,8)

# alias 

import logic as lg
lg.add(2,8)
lg.mul(2,8)
lg.sub(2,8)
lg.div(2,8)
lg.rem(2,8)
lg.exp(2,8)

# accessing few functions from the file 
from logic import add,sub

add(2,4)
sub(5,4)
'''
from logic import *

add(5,6)
sub(16,9)
mul(2,7)
div(3,8)
rem(4,9)
exp(4,7)
