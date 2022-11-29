from words import words
import random
import string


def get_valida_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

get_valida_word(words)

def bienvenida():
    print("_" * 50)
    print("Bienvenido al juego del ahorcado")
    print("_" * 50)
bienvenida()
   



def hangman():
    lives = 6
    word = get_valida_word(words)
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #letras que el usuario ya ingreso

    

   
    while len(word_letters) > 0 and lives > 0:
        # letras usadas
        print('tienes', lives, 'vidas restantes y has usado estas letras: ', ' '.join(used_letters))

        
        word_list = [letter if letter in used_letters else '-' for letter in word]
       
        print('palabra actual: ', ' '.join(word_list))

        user_letter = input('digita una letra: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1 
                #resta una vida si la letra es incorrecta 
                print('\n La letra,', user_letter,  " no esta en la palabra.")

        elif user_letter in used_letters:
            print('\n ya usaste esa letra, intenta con otra.')

        else:
            print('\n No es una letra valida.')
        if lives == 6:
            print(""""
               |
               |
               |
               |
               |""") 
        elif lives == 5:  
            print("""
                ___________
               | /        
               |/        
               |          
               |          
               |
            """)    
        elif lives == 4:
            print( """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,)
        elif lives == 3:
            print("""
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """)   
        elif lives == 2: 
            print("""
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """) 
        elif lives == 1:
            print("""
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """)       
    #cuando se terminan las vidas pasa aqui
    if lives == 0:
        print("""
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
           """)
        print('Moriste, la palabra era: ', word)
    else:
        print('adivinaste, la palabra: ', word)


if __name__ == '__main__':
    hangman()