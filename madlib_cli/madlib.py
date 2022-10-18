import re

def user_story():
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

    story_text = read_template("assets/make_me_a_video_game_template.txt")
    story_template , story_sentence = parse_template(story_text)
  
    story_word = list()

    for word in story_sentence:
        story_word.append(input(f"{word} > "))

    with open("/home/noor/AdvPy-401/madlib-cli/assets/make_me_a_video_game_output.txt",'w') as file:
        story = merge(story_template,(tuple)(story_word))
        file.write(story) 
        print(story)

def read_template(path):
    
    try:
        with open (path ,"r") as file:
            return file.read()
    except:
        raise FileNotFoundError 

def parse_template(story_template):
    
    story_sentence  = re.findall('{(.*?)}', story_template)
    edit_text = re.sub('{.+?}', '{}', story_template)  
    return edit_text,(tuple)(story_sentence) 

def merge (empty_text,story_sentence):
   
    return empty_text.format(*story_sentence) 

if __name__ =="__main__":
      user_story()  