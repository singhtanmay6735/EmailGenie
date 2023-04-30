import streamlit as st
from langchain import PromptTemplate
import openai
from langchain.llms import OpenAI
# from dotenv import load_dotenv
# import os

template = """
    Below is an email that may be poorly worded.
    Your goal is to:
    - Properly format the email
    - Convert the input text to a specified tone
    - Convert the input text to a specified language
    Here are some examples different Tones:
    Formal: I am writing to formally request a meeting with you.
    Informal: Hey there! Just wanted to check in and see how you're doing. 
    Persuasive: I strongly urge you to consider our proposal and take advantage of this limited-time offer.
    Apologetic: I apologize for the delay in getting back to you and any inconvenience it may have caused.
    Assertive: I need you to complete the report by Friday at the latest.
    Collaborative: Let's work together to find a solution that meets both of our needs.
    Humorous: I promise this email won't be as long as the last season of Game of Thrones. (I mean, seriously, what was that about?)
    Here are some examples of words in different languages:
    - English: Hello, Thank you, Goodbye, Please, Yes, No, Help, Love, Friend, Family.
    - Hindi: Namaste, Dhanyavaad, Alvida, Kripaya, Haan, Nahin, Madad, Pyar, Dost, Parivar.
    - French: Bonjour, Merci, Au revoir, S'il vous plaît, Oui, Non, Aide, Amour, Ami, Famille.
    - Dutch: Hallo, Dank je, Tot ziens, Alsjeblieft, Ja, Nee, Hulp, Liefde, Vriend, Familie.
    - Español: Hola, Gracias, Adiós, Por favor, Sí, No, Ayuda, Amor, Amigo, Familia.
    - Chinese (Traditional): 你好 (nǐ hǎo), 謝謝 (xiè xiè), 再見 (zài jiàn), 請 (qǐng), 是 (shì), 不是 (bú shì), 幫助 (bāng zhù), 愛 (ài), 朋友 (péng yǒu), 家人 (jiā rén).
    Example Sentences from each Language:
    - English: John is going to the store to buy some groceries. He needs to get milk, bread, and eggs. After he finishes shopping, he will head back home.
    - Hindi: राजेश बाजार से सब्ज़ियां लेने जा रहा है। उसे टमाटर, प्याज़, आलू और गाजर लेने हैं। जब वह शॉपिंग समाप्त करेगा तो वह अपने घर वापस जाएगा।
    - French: Julie a prévu de passer le week-end à la plage avec ses amis. Ils vont nager, bronzer et se détendre. Ils ont loué un appartement près de la mer pour pouvoir profiter de la vue.
    - Dutch: Bart heeft een nieuwe baan gevonden en begint binnenkort met werken. Hij is blij met de kans om zijn carrière te ontwikkelen. Hij zal hard werken om een goede indruk te maken op zijn nieuwe werkgever.
    - Español: Lucía quiere aprender a tocar la guitarra. Ha comprado un instrumento y está buscando un buen profesor. Espera poder tocar algunas canciones sencillas en unas pocas semanas.
    - Chinese (Traditional): 小明今天早上六點起床，因為他要去跑步。他喜歡在公園裡跑步，因為那裡的空氣很新鮮。跑步後，他會回家洗澡然後吃早餐。
    Please start the email with a warm introduction. Add the introduction if you need to. Also add the salutation in the ending.
    
    Below is the email, tone, and language:
    TONE: {tone}
    LANGUAGE: {language}
    EMAIL: {email}
    
    YOUR {language} RESPONSE:
"""

prompt = PromptTemplate(
    input_variables=["tone", "language", "email"],
    template = template,
)
# openai.api_key = os.getenv("API_KEY")

def load_LLM(openai_api_key):
    llm = OpenAI(temperature=.7, openai_api_key = openai_api_key)
    return llm

st.set_page_config(page_title = "Email Genie")

st.image(image="EmailGenie.png", width = 750)
st.header("EmailGenie")

col1, col2 = st.columns(2)

with col1:
    st.markdown("EmailGenie is an AI-powered tool designed to help individuals improve their email communication skills. With the help of OpenAI\'s language model, this tool can analyze and improve the tone, structure, and content of emails, making them more effective and professional.")
    
with col2:
    st.markdown("This tool is particularly useful for individuals who struggle with email communication, whether due to language barriers, social anxiety, or simply lack of experience. EmailGenie can suggest edits and rephrasings for awkward or unclear language")
   
st.markdown("**Instructions:**")
st.markdown("1. **Generate OpenAI API Key:** In order to use the EmailGenie, you will first need to generate an API key for OpenAI. This key will allow you to authenticate your requests to OpenAI's API and gain access to its language processing capabilities. Here's how you can generate an API key:") 
st.markdown("- Go to the OpenAI website and sign up for an account.")
st.markdown("- Navigate to the API dashboard and select \"Create a new API key\"")
st.markdown("- Copy the generated API key and store it somewhere safe. You will need to enter this key into the Email Writer tool in order to use it.")

st.markdown("2. **Write your email in the text box given:** Once you have your API key, you can start using the Email Writer tool. Simply navigate to the tool's interface and enter your email message into the text box provided. You can write your email in any language that the OPENAI API supports.") 

st.markdown("3. **Select the tone and dialect from the options given:** The Email Writer tool allows you to choose from a variety of tones and dialects to suit your needs. You can select the appropriate tone and dialect from the drop-down menus provided in the tool's interface.") 

st.markdown("4. **Hit Enter:** Once you have written your email and selected your tone and dialect, simply hit ""CTRL/CMD + Enter" "to submit your request to the API. The API will process your text and generate suggestions for improving your email's tone, structure, and content.") 


st.markdown("5. **Review and Edit the suggested changes:** The Email Writer tool will display the suggested changes to your email in a separate text box. You can review these changes and choose to accept or reject them as you see fit. You can also make additional edits to your email in the original text box and re-submit your request to the API.") 

st.markdown("6. **Copy and paste the improved email:** Once you are satisfied with the suggested changes to your email, simply copy and paste the improved text into your email client of choice and send your email as normal. Congratulations, you've just used the Email Writer tool to improve your email communication!") 

st.markdown("## Please write your Email Content")

def get_api_key():
    input_text = st.text_input(label="OpenAI API Key ",  placeholder="Ex: sk-2twmA8tfCb8un4...", key="openai_api_key_input")
    return input_text

openai_api_key = get_api_key()

col3, col4 = st.columns(2)

with col3:
    option_tone = st.selectbox(
        "Which tone would you like your email to have?",
        ('Formal', 'Informal', 'Persuasive', 'Apologetic', 'Assertive', 'Collaborative', 'Humorous')    
    )

with col4:
    option_language = st.selectbox(
        "Which language would you like?",
        ('English', 'Hindi', 'French', 'Dutch', 'Espanyol', 'Chinese (Traditional)')    
    )
    
    
def get_text():
    input_text = st.text_area(label="", placeholder="Your Email Content", key="email_input")
    return input_text
    
email_input = get_text()

st.markdown("**Your Converted Email**")

if len(email_input.split(" ")) > 700:
    st.write("Please enter a shorter email. The maximum length is 700 words.")
    st.stop()

if email_input:
    if not openai_api_key:
        st.warning('Please insert OpenAI API Key. Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)', icon="⚠️")
        st.stop()

    llm = load_LLM(openai_api_key=openai_api_key)

    prompt_with_email = prompt.format(tone=option_tone, language=option_language, email=email_input)

    formatted_email = llm(prompt_with_email)

    st.write(formatted_email)