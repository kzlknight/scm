本文实例讲述了Python实现的简单hangman游戏。分享给大家供大家参考。具体如下：

```python

    #!/usr/bin/env python
    import random 
    import cPickle 
    class Hangman(object):
      '''A simple hangman game that tries to improve your vocabulary a bit '''
      def __init__(self):
        # the variables used, this is not necessary
        self.dumpfile = ''    #the dictionary file
        self.dictionary = {}   #the pickled dict
        self.words = []     #list of words used
        self.secret_word = ''  #the 'key'
        self.length = 0     #length of the 'key'
        self.keys = []      #inputs that match the 'key'
        self.used_keys = []   #keys that are already used
        self.guess = ''     #player's guess
        self.mistakes = 0    #number of incorrect inputs
        return self.load_dict()
      #insert some random hints for the player
      def insert_random(self, length):
        randint = random.randint
        # 3 hints
        if length >= 7: hint = 3
        else: hint = 1
        for x in xrange(hint):
            a = randint(1, length - 1)
            self.keys[a-1] = self.secret_word[a-1]
      def test_input(self):
        #if the guessed letter matches
        if self.guess in self.secret_word:
          indexes = [i for i, item in enumerate(self.secret_word) if item == self.guess]
          for index in indexes:
            self.keys[index] = self.guess
            self.used_keys.append(self.guess)
            print "used letters ",set(self.used_keys),'\n'
        #if the guessed letter didn't match
        else:
          self.used_keys.append(self.guess)
          self.mistakes += 1
          print "used letters ",set(self.used_keys),'\n'
      # load the pickled word dictionary and unpickle them  
      def load_dict(self):
        try :
          self.dumpfile = open("~/python/hangman/wordsdict.pkl", "r")
        except IOError:
          print "Couldn't find the file 'wordsdict.pkl'"
          quit()
        self.dictionary = cPickle.load(self.dumpfile)
        self.words = self.dictionary.keys()
        self.dumpfile.close()
        return self.prepare_word()
      #randomly choose a word for the challenge
      def prepare_word(self):
        self.secret_word = random.choice(self.words)
        #don't count trailing spaces
        self.length = len(self.secret_word.rstrip())
        self.keys = ['_' for x in xrange(self.length)]
        self.insert_random(self.length)
        return self.ask()
      #display the challenge
      def ask(self):
        print ' '.join(self.keys), ":", self.dictionary[self.secret_word] 
        print 
        return self.input_loop()
      #take input from the player
      def input_loop(self):
        #four self.mistakes are allowed
        chances = len(set(self.secret_word)) + 4     
        while chances != 0 and self.mistakes < 5:
          try:
            self.guess = raw_input("> ")
          except EOFError:
            exit(1)
          self.test_input()
          print ' '.join(self.keys)
          if '_' not in self.keys:
            print 'well done!'
            break
          chances -= 1
        if self.mistakes > 4: print 'the word was', ''.join(self.secret_word).upper()
        return self.quit_message()
      def quit_message(self):
        print "\n"
        print "Press 'c' to continue, or any other key to quit the game. "
        print "You can always quit the game by pressing 'Ctrl+D'"
        try:
          command = raw_input('> ')
          if command == 'c': return self.__init__() #loopback
          else : exit(0)
        except EOFError: exit(1)
    if __name__ == '__main__':
      game = Hangman()
      game.__init__()
    
    
```

希望本文所述对大家的Python程序设计有所帮助。

