import streamlit as st
from gemini_client import generate_text
from prompt_builder import build_prompt

st.set_page_config(page_title="AI WRITING ASSISTANT", layout="centered" )

st.title("AI WRITING ASSISTANT")

user_input = st.text_area("Enter your content/idea")

tone = st.selectbox(
"Select Tone",
["Professional", "Casual", "Persuasive", "friendly", "Formal"]

)


audience = st.selectbox(
"Target  Audience",
["General Public", "Beginners", "Experts", "Business Executives"]

)

format_type = st.selectbox(
    "Content Format",
    ["email", "blog post", "social media post", "report", "product distribution"]
)

if st.button("Generate Content"):
    
    # if there is no prompt, show warning
    if not user_input.strip():
        st.warning("please enter some content")

    else:
        with st.spinner("Generating...."):

            # build the prompt
            prompt = build_prompt(user_input, tone, audience, format_type)

            # generate the content
            output = generate_text(prompt)
        st.subheader("Generated Output")
        st.write(output) # show the outpu