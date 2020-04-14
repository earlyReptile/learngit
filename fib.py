# 斐波那契数列实现
# 生成器实例

def fib(n):
	a = 0
	b = 1
	count = 0
	while count < n:
		tmp = a
		a = b
		b = tmp + b
		#print(b)
		yield b     # 生成器，与return相似 功能是暂停函数执行
		count += 1
f = fib(10)		
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
while True:
	try:
		print(next(f))
	except StopIteration as e:
		print('Generator return value:', e.value)
		break