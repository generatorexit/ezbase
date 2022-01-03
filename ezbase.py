try:
    import os
    import sys
    import base64

except ModuleNotFoundError:
        print("Loading the missing module")
        os.system("pip install base64")
        os.system("clear")
        print("Please try again")

def usage():
	print("Base64 encoder-decoder")
	print(f'{sys.argv[0]} -e or --encode <"encode"> >> Encrypts text')
	print(f'{sys.argv[0]} -d or --decode <"decode"> >> Decrypts text')
	print(f"{sys.argv[0]} -fe or --fileencode <encode.txt> >> Encrypts text in file")
	print(f"{sys.argv[0]} -fd or --filedecode <decode.txt> >> Decrypts text in file")
	sys.exit(1)

if len(sys.argv) <3:
	usage()

elif sys.argv[1] in ["-e","--encode"]:
	character = sys.argv[2]
	change = character.encode("utf-8")
	show = base64.b64encode(change)
	string = show.decode("utf-8")
	print(string)

elif sys.argv[1] in ["-d","--decode"]:
        character = base64.b64decode(sys.argv[2])
        print(character.decode("utf-8"))

elif sys.argv[1] in ["-fe","--fileencode"]:
	try:
		file = open(sys.argv[2])
		open = file.readlines()
		for read in open:
			character = read.encode("utf-8")
			show = base64.b64encode(character)
			string = show.decode("utf-8")
			print(string)
	except FileNotFoundError:
		print("There is no such file")

elif sys.argv[1] in ["-fd","--filedecode"]:
	try:
		file = open(sys.argv[2])
		open = file.readlines()
		for oku in open:
			character = base64.b64decode(oku)
			print(character.decode("utf-8"))
	except FileNotFoundError:
		print("There is no such file")

else:
	print(f"The parameter: ({sys.argv[1]}) is wrong")
	usage()