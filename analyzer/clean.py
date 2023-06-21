import re 

file1 = open("analyzer/inputCode.txt", "r")
fileInfo = file1.read()
file1.close()

singleLineComments=re.sub("#(.+?)[\n$]","\n", fileInfo)
# print(singleLineComments)
regex = re.compile("\"\"\"(.+?)\"\"\"", re.DOTALL)
multilineComments = re.sub(regex, "", singleLineComments)
# print(multilineComments)
linesWithBlanks =re.split("\n", multilineComments)

finalLines = [line for line in linesWithBlanks if line.strip() != ""]
finalCode = "\n".join(finalLines)
print(finalCode)
f = open("cleanCode.txt", "w")
f.write(finalCode)
f.close()