import string

with open("all_data.txt", "r+", encoding="utf8") as f:
   file_lines = f.readlines()

for line in f:
     result = line.split('.')

lines = set(file_lines)

new_file = (open('new_data.txt','w',encoding="utf8"))

for i in string.punctuation: #noktalama işaretlerini kaldırmak için
   line = line.translate(str.maketrans(i," "))

def all_data_words(line):
    local_text = local_text.replace("ş", "s").replace("ı", "i").replace("ö", "o").replace("ğ", "g").replace("ç", "c").replace("ü", "u")
    return local_text

