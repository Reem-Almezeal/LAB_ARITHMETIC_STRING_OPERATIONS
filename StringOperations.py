print("Welcome in String Operations System\n")

sentence="hi my name is Reem Almezeal , I am a software enigineer , I am a student at the Tuwaiq Academy , I am learning full stack web development by using python language"
word="Reem"


print("The length of the sentence is:",len(sentence))
print("First index of the word is:",sentence.find(word))
print("word count in the sentence is:",sentence.count(word),"\n")
print("The sentence in uppercase is:",sentence.upper(),"\n")
print("The sentence in lowercase is:",sentence.lower(),"\n")

replace_sentence=sentence.replace(word,"Eng.Reem")
print("The sentence after replacement is:",replace_sentence,"\n")

print("last character of the sentence is:",sentence[-1])