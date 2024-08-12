import streamlit as st
import random

class ran():
    def __init__(self):
        self.u=None
        self.com =None
    def s_p_s(self,user_num):
        # st.write("Welcome to game stone paper scissor")
        # st.write('select the options\n', '1 for the stone\n' , '2for the paper\n', '3 for the scissor')
        self.u= int(user_num)
        self.com=random.randint(1,3)
        if self.com==1 and self.u==1:
            st.write('computer choosen value',self.com)
            st.write(' Both choose Stone')
            st.write(' Congratulation  you ties a Match')
        elif self.com==1 and self.u ==2:
            st.write('computer choosen value', self.com)
            st.write ("You choose Paper and Computer choose Stone")
            st.write(' Congratulations  You win ')
        elif self.com==1 and self.u ==3:
            st.write('computer choosen value', self.com)
            st.write('You choose scissor and Computer choose Stone')
            st.write(' oops!!  You loose')
        elif self.com==2 and self.u ==1:
            st.write('computer choosen value', self.com)
            st.write('You choose Paper and Computer choose Stone')
            st.write(' Congratulations  You win ')
        elif self.com==2 and self.u ==2:
            st.write('computer choosen value', self.com)
            st.write(' Both choose Paper')
            st.write(' Congratulation  you ties a Match')
        elif self.com==2 and self.u ==3:
            st.write('computer choosen value', self.com)
            st.write('You choose Scissor and Computer choose Paper')
            st.write(' Congratulations  You win ' )
        elif self.com==3 and self.u ==1:
            st.write('computer choosen value', self.com)
            st.write('You choose Stone and Computer choose Scissor')
            st.write(' Congratulations  You win ')
        elif self.com==3 and self.u ==2:
            st.write('computer choosen value', self.com)
            st.write('You choose Paper and Computer choose Scissor')
            st.write(' oops!!  You loose')
        elif self.com==3 and self.u ==3:
            st.write('computer choosen value', self.com)
            st.write(' Both choose Scissor')
            st.write(' Congratulation  you ties a Match')

game=ran()

st.title('Stone_Paper_Scissor Game')
st.write("Welcome to game stone paper scissor")
st.write('select the options \n', '1 for the stone ', '2for the paper \n', '3 for the scissor'  )
user_input = st.number_input('Enter the number  :', min_value=1, max_value=3)
if st.button('play'):
    game.s_p_s(user_input)
