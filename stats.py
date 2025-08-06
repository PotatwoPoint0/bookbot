
def get_num_words(book):
        
        with open(book) as f:
            file_contents = f.read()
        words = file_contents.split()
        num_count = len(words)
        return num_count

def sort_on(items):
     return items["num"]

def get_num_characters(book):
      characters = {}
      with open(book) as f:
            file_contents = f.read().lower()
            for x in file_contents:
                if x.isalpha():
                    if x in characters:
                        characters[x] += 1
                    else:
                        characters[x] = 1
            char_list = []
            for char, val in characters.items():
                 char_list.append({"character":char, "num":val})
            char_list.sort(reverse=True,key=sort_on)
            return char_list