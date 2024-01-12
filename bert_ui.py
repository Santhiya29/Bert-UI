import streamlit as st
 
def main():
    st.title("BERT")
 
    # Textbox for user input
    user_input = st.text_input("Type something:")
 
    # Submit button
    if st.button("Submit") and user_input:
        st.write("You typed:", user_input)
        st.write("Bert Response:", user_input)
    
 
if __name__ == "__main__":
    main()
 