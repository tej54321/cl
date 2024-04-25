import sys

current_key = None
current_values = []

for line in sys.stdin:
	key, value = line.strip().split('\t')


	if current_key == None:
		current_key = key
	if key != current_key:
		result = 0
		for value_pair in current_values:
			value1, value2 = value_pair.split(',')
			result += int(value1)*int(value2)
		print(f"{current_key}\t{result}")
		
		current_key = key
		current_values = []
		
	current_values.append(value)
	
result = 0

for value_pair in current_values:
	value1, value2 = value_pair.split(',')
	result += int(value1) * int(value2)
print(f"{current_key}\t{result}")





