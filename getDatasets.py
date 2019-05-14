import subprocess



def readAWS(appendinfo):
  cmd = 'aws s3 ls s3://narp-alext/' + appendinfo
  push = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
  text = push.communicate()[0].replace("PRE ", "").split("\n")   
  #text = push.communicate()[0].split()

  return [line.strip() for line in text]

#animals = ['10547', '10548', '10549', '10550', '10551', '10601']
animals = ['10547']

for animal in animals:
  datasets =  readAWS(animal + '/')  
  for d in datasets:
    if d.endswith(animal+'/'):
      trodefiles = readAWS(animal + '/' + d)
      print(animal+"/"+trodefiles[0])


  
