import streamlit as st
import openai

# 1. ॲप सेटिंग आणि डिझाईन
st.set_page_config(page_title="Zlender.ai", page_icon="🧊", layout="centered")

st.title("🧊 Zlender.ai - Blender Python Code Generator")
st.write("Welcome to your 3D course web app! Create Blender scripts instantly using AI.")
st.markdown("---")

# 2. साईडबार - API Key साठी
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input("OpenAI API Key:", type="password", placeholder="sk-...")
    st.markdown("---")
    st.info("साईडबारमध्ये तुमची API Key टाकल्याशिवाय ॲप काम करणार नाही.")

# 3. मुख्य स्क्रीन - युजर इनपुट
user_prompt = st.text_area(
    "तुम्हाला Blender मध्ये काय बनवायचे आहे ते लिहा:",
    placeholder="उदा. Create a low-poly tree or coffee mug..."
)

if st.button("🚀 Generate Blender Script", type="primary"):
    if not api_key:
        st.error("⚠️ कृपया आधी साईडबारमध्ये तुमची OpenAI API Key टाका!")
    elif not user_prompt:
        st.warning("⚠️ कृपया प्रॉम्प्ट बॉक्समध्ये काहीतरी लिहा.")
    else:
        with st.spinner("✨ AI कोड तयार करत आहे... थोडा वेळ थांबा."):
            try:
                # OpenAI API कनेक्ट करणे
                client = openai.OpenAI(api_key=api_key)
                
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are an expert Blender Python (bpy) developer. Write only clean, executable Blender Python code based on the user's request."},
                        {"role": "user", "content": user_prompt}
                    ]
                )
                
                code_result = response.choices[0].message.content
                
                st.success("🎉 कोड यशस्वीपणे तयार झाला आहे!")
                
                # कोड दाखवणे आणि डाऊनलोड बटण
                st.subheader("📜 Generated Blender Python Code:")
                st.code(code_result, language="python")
                
                st.download_button(
                    label="📥 Download Script (.py)",
                    data=code_result,
                    file_name="blender_script.py",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"❌ काहीतरी चूक झाली आहे (API Key तपासा): {e}")

# फुटर
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Zlender.ai - Built with Streamlit</p>", unsafe_allow_html=True)
