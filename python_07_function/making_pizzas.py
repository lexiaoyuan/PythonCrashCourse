import pizza2
from pizza import make_pizza3
from pizza import make_pizza2 as mp2
import pizza as p

pizza2.make_pizza(16, 'pepperoni')
pizza2.make_pizza(18, 'mushrooms', 'green peppers', 'extra cheese')
make_pizza3(22, 'mushrooms', 'green peppers', 'extra cheese')
mp2('pepperoni')
mp2('mushrooms', 'green peppers', 'extra cheese')
p.make_pizza3(26, 'mushrooms', 'green peppers', 'extra cheese')
