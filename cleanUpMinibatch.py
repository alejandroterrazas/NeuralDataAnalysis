fin = open('./minibatch.txt')
fout = open('./cleanbatch.txt', 'w')

for line in fin.readlines():
  outline = "10551/" + line.replace('PRE', "").lstrip()
  fout.write(outline)

fin.close()
fout.close()
