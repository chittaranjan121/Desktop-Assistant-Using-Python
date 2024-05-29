import streamlit as st
from helper import voice_input,text_to_speech,llm_model_object

def main():
    st.title("Desktop Assistant Multilangual")

    if st.button("Ask me Anything"):
        with st.spinner("Listining.."):
            text=voice_input()
            response=llm_model_object(text)
            text_to_speech(response)

            audio_file=open("speech.mp3",'rb')
            audio_bytes=audio_file.read()

            st.text_area(label="Response:",value=response,height=360)
            st.audio(audio_bytes,format='audio/mp3')
            st.download_button(label="Download Speech",
                                data=audio_bytes,
                                file_name="speech.mp3",
                                mime="audio/mp3")

if __name__=="__main__":
    main()            


