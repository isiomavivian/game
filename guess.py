import streamlit as st
import random

st.header("My Guessing Game")
st.image("dice.gif")
b = st.number_input("Please input a number from 1 -6")
a = random.randint(1,6)

def game (a,b):
 if b> 6:
    return("intalid input, please select a number between 1 and 6")
 else:
   if a ==b:
     print("correct")
   else:
     st.write(f"Your selected number is {b}")
     st.write(f"Random number is {a}")
     return("wrong try again")
   

if st.button("Try Your Luck"):
  st.write(game(a,b))