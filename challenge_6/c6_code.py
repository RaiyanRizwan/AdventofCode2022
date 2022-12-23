from pathlib import Path

# PUZZLE 1|2 - find first unique 4|14-digit sequence in str

def marker(path, size):

	ds, index = Path(path).read_text(), 0
	while index < len(ds) - size:
		packet = ds[index:index+size]
		if unique_characters(packet):
			return index + size
		index += 1

def unique_characters(s):

	for i in range(len(s)):
		for j in range(i + 1, len(s)):
			if s[i] == s[j]:
				return False

	return True
