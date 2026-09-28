import streamlit as st
import openai

# App Page Configuration
st.set_page_config(
    page_title="Zlender.ai - AI 3D Generator",
    page_icon="🧊",
    layout="wide"
)

# App Title & Header
st.title("🧊 Zlender.ai - AI 3D Asset & Code Generator")
st.markdown("---")
st.write("Welcome to your user-friendly AI assistant! Enter a prompt or click a quick sample below to generate Blender Python code.")

# Sidebar - API Settings
with st.sidebar:
    st.header("⚙️ Settings")
    user_api_key = st.text_input("Enter your OpenAI API Key:", type="password", help="Paste your secret OpenAI API key here.")
    st.markdown("---")
    st.info("💡 Tip: Keep your API key safe and secure.")

# Main Layout (Two columns for user-friendliness)
col1, col2 = st.columns([1.2, 0.8])

with col1:
    st.subheader("✍️ 3D Prompt Workspace")
    
    # Quick Sample Prompt Buttons (User-friendly feature)
    st.markdown("Quick samples:")
    sample_col1, sample_col2 = st.columns(2)
    
    selected_prompt = ""
    if sample_col1.button("🌲 Low-Poly Tree"):
        selected_prompt = "Generate a low-poly 3D tree model using Blender Python bpy."
    if sample_col2.button("☕ Coffee Mug"):
        selected_prompt = "Generate a simple 3D coffee mug model using Blender Python bpy."

    # User Prompt Input Box (Pre-fills if a sample button is clicked)
    user_prompt = st.text_area(
        "What would you like to create in 3D?",
        value=selected_prompt,
        placeholder="e.g., Create a modern table or a sci-fi container...",
        height=130
    )

    if st.button("🚀 Start AI Generation", type="primary"):
        if not user_api_key:
            st.error("⚠️ कृपया आधी साईडबारमध्ये तुमची OpenAI API Key टाका!")
        elif not user_prompt:
            st.warning("⚠️ कृपया प्रॉम्प्ट बॉक्समध्ये काहीतरी लिहा किंवा वरील सॅम्पल बटण दाबा.")
        else:
            with st.spinner("✨ AI is thinking and writing your Blender Python script..."):
                try:
                    # Connecting to OpenAI API
                    client = openai.OpenAI(api_key=user_api_key)
                    
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are an expert Blender Python (bpy) developer. Write only clean, executable Blender Python code based on the user's request."},
                            {"role": "user", "content": user_prompt}
                        ]
                    )
                    
                    ai_generated_code = response.choices[0].message.content
                    
                    st.success("🎉 Code generated successfully!")
                    
                    # Display Code
                    st.markdown("### 💻 Generated Blender Code:")
                    st.code(ai_generated_code, language="python")
                    
                    # Download Button
                    st.download_button(
                        label="📥 Download Script (.py)",
                        data=ai_generated_code,
                        file_name="zlender_script.py",
                        mime="text/plain"
                    )
                    
                except Exception as e:
                    st.error(f"❌ काहीतरी चूक झाली आहे: {e}")

with col2:
    st.subheader("👁️ Live Preview & Status")
    st.markdown(
        """
        <div style="border: 2px dashed #10b981; padding: 35px; text-align: center; border-radius: 10px; background-color: #0f172a;">
            <p style="color: #34d399; font-size: 16px; font-weight: bold;">System Ready</p>
            <p style="color: #94a3b8; font-size: 13px;">Your generated script will appear here ready for download and use in Blender.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    st.markdown("### 📋 App Status:")
    st.write("✅ **UI Design:** Clean & User-Friendly")
    st.write("✅ **Quick Prompts:** Active")
    st.write("🟢 **AI Engine:** Ready for API Key")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Zlender.ai - Built with Python & Streamlit</p>", unsafe_allow_html=True)
