
# Word replacement program

def replace_word():
    
    str = "Hi guys, and hi hi hi"
    word_to_replace = input("Enter the word you want to replace: ")
    word_replacement = input("Enter the word to replce it with: ")
    
    print(str.replace(word_to_replace, word_replacement))
    
replace_word()