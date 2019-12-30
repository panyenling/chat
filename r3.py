def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8') as f:#encoding='utf-8-sig'編碼問題
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	a_word_count = 0
	a_sticker_count = 0
	a_image_count = 0
	y_word_count = 0
	y_sticker_count = 0
	y_image_count = 0
	for line in lines:
		s = line.strip('\n').split(' ')
		time = s[0]
		name = s[1]
		if name == 'Annie':
			if s[3] =='貼圖':
				a_sticker_count += 1
			if s[3] =='圖片':
				a_image_count += 1
			for m in s[3:]:
				a_word_count += len(m)
		elif name == 'Y-Ling':
			if s[2] =='貼圖':
				y_sticker_count += 1
			if s[2] =='圖片':
				y_image_count += 1
			for m in s[2:]:
				y_word_count += len(m)

	print('Annie Wang說了', a_word_count, '個字')
	print('Annie Wang傳了', a_sticker_count, '個貼圖')
	print('Annie Wang傳了', a_sticker_count, '個圖片')
	print('Y-Ling說了', y_word_count, '個字')
	print('Y-Ling傳了', y_sticker_count, '個貼圖')
	print('Y-Ling傳了', y_sticker_count, '個圖片')			 


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('AnnieWang.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)

	
main()