import json
import os



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
story_word = []
temp_name = "make_me_a_video_game_template.json"

def getStory_template(name, path=None):
        path="/home/noor/AdvPy-401/madlib-cli/assets"
        if not path:
            path = path
        fpath = os.path.join(path, name)
        # print(os.path.exists(fpath))
        with open(fpath, "r") as f:
            data = json.load(f)  # load take the file path
        Story_word = data
        return Story_word

def get_StoryWord_from_user():
    story_sentence = getStory_template(temp_name)["story_sentence"]
    for word in story_sentence:
        input_sentence = input(word + " ")
        story_word.append(input_sentence)
    return story_word

def build_Story():

        Story = getStory_template(temp_name)["story_template"].format(*story_word)
        return (Story)

def show_Story():
        with open("/home/noor/AdvPy-401/madlib-cli/assets/output.txt",'w') as file:
            file.write(Storyfinal)
        print("\n")
        print (Storyfinal)


if __name__ =="__main__":

 welcomemsg()

 words = get_StoryWord_from_user()
 Storyfinal = build_Story()
 show_Story()



  
    