import json
import os
# I need (madlibs template, User Input, Build the story)

class Madlib_Story:
    path="/home/noor/AdvPy-401/madlib-cli/assets"
    def __init__(self, story_sentence , story_template ):
        self.story_sentence = story_sentence
        self.story_template = story_template
        self.story_word = []
        self.Story = None
      
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

    @classmethod
    def getStory_template(cls,name, path=None):
        if not path:
            path = cls.path
        fpath = os.path.join(path, name)
        # print(os.path.exists(fpath))
        with open(fpath, "r") as f:
            data = json.load(f)
         # print(data)
        user_Story = cls(**data)
        return user_Story

    def get_StoryWord_from_user(self):
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
        
        for word in self.story_sentence:
          input_sentence = input(word + " ")
          self.story_word.append(input_sentence)
        return self.story_word

    def build_Story(self):

        self.Story = self.story_template.format(*self.story_word)
        return (self.Story)

    def show_Story(self):
        with open("/home/noor/AdvPy-401/madlib-cli/assets/make_me_a_video_game_output.txt",'w') as file:
            file.write(Story)
        print("\n")
        print (Story)



temp_name = "make_me_a_video_game_template.json"
user_Story= Madlib_Story.getStory_template(temp_name)
sentences = user_Story.get_StoryWord_from_user()
Story = user_Story.build_Story()
user_Story.show_Story()