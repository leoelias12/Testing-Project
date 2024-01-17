import op_func
import text_func

text_func.text('Calculator to sum 2 numbers')
x = int(input('Input X: '))
y = int(input('Input Y: '))
text_func.text(f'The sum of the numbers {x} and {y} is: {op_func.numsum(x, y)}')
