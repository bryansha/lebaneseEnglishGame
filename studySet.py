import ast

filename = 'file/Notepads/studySet.txt'
with open(filename, 'r') as inn:
    studySetString = inn.read()
    
if studySetString == "":
    studySetPairs = {}
else:
    studySetPairs = ast.literal_eval(f"{studySetString}")

showStudySetPairs = studySetPairs