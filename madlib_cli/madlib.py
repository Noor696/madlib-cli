# I need (madlibs template, User Input, Build the story)

def welcomemsg():

    print ("""
    **************************************************************************************
    ** Mad Libs game contain short stories with many key words replaced with blanks.    **
    ** Beneath each blank is specified a category, such as noun, verb, place, Adjective **
    ** One player asks in turn, to contribute a word of the specified type for each     **
    ** blank, but without revealing the context for that word.                          **
    ** Finally, the completed story is read aloud. The result is usually a sentence     **
    ** which is comical, surreal and takes on somewhat of a nonsensical tone.           **
    ** _________________________________________________________________________________**
    **                     please provide the following words:                          **
    """)

def get_words_from_user(story_words):
 
    input_words= []
    for word in story_words:
        user_input = input(word + " ")
        input_words.append(user_input)
    return input_words

input_words = get_words_from_user(["Adjective" , "Adjective" , "A First Name", "Past Tense Verb", "A First Name" , "Adjective", "Adjective", "Plural Noun", "Large Animal", "Small Animal", "A Girl's Name", "Adjective", "Plural Noun" , "Adjective", "Plural Noun", "Number 1-50" , "First Name", "Number", "Plural Noun", "Number", "Plural Noun"])
print(input_words)
