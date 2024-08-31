'''from meta_ai_api import MetaAI

ai = MetaAI()
response = ai.prompt(input("enter your qustion"))
print(response)

#print(ai.prompt("what is 2 + 2?"))
#print(ai.prompt("what was my previous question?"))'''








import streamlit as st
from meta_ai_api import MetaAI
ai = MetaAI()
def get_response(prompt):
    try:
        response = ai.prompt(prompt)
        return response
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    #st.title("🤖")
    #st.write(':heart: **Meesam** *Raza* :heart:')
    st.title("  :heart:  **Zeta** *AI*  ")
   # st.title("                    🤖")
    st.markdown(
        """
        <h1 style='text-align: center; font-size: 150px;'>
            🤖 
        </h1>
        """,
        unsafe_allow_html=True
    )

    # Input field for user to enter their question
    user_input = st.text_input("Enter your Prompt:")

    if st.button("Get Response"):
        if user_input:
            with st.spinner("Getting response..."):
                response = get_response(user_input)
                st.write("AI Response:")
                st.write(response)



        else:
            st.error("Please enter a question.")




if __name__ == "__main__":
    main()

