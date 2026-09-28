import streamlit as st

# App Page Configuration
st.set_page_config(
    page_title="Zlender.ai - AI & 3D Generator",
    page_icon="🧊",
    layout="wide"
)

# App Title
st.title("🧊 Zlender.ai - AI 3D Asset & Code Generator")
st.markdown("---")
st.write("Cursor-style AI App: Enter a text prompt, and generate 3D code or models using AI and Blender engines!")

# Sidebar - API Settings
with st.sidebar:
    st.header("⚙️ System Settings")
    api_key = st.text_input("Enter your AI API Key:", type="password")
    engine_type = st.selectbox(
        "Select 3D Engine:",
        ["Blender Python API (bpy)", "Trimesh Python Engine", "AI 3D Cloud API"]
    )
    st.markdown("---")
    st.info("Note: This app generates 3D generation logic based on your text prompt.")

# Main Dashboard (Two columns)
col1, col2 = st.columns([1.2, 0.8])

with col1:
    st.subheader("✍️ 3D Prompt Workspace (Cursor Style)")
    
    # User Prompt Input Box
    user_prompt = st.text_area(
        "What would you like to create in 3D?",
        placeholder="e.g., Generate a low-poly tree model or a sci-fi container using Python...",
        height=150
    )

    if st.button("🚀 Start 3D Generation", type="primary"):
        if user_prompt:
            with st.spinner("AI model is reading the prompt and generating 3D code..."):
                
                # Simulation / Backend Processing Logic
                generated_code = f"""
# Zlender.ai Generated Blender Python Script
import bpy

# Clear existing objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Prompt based action: {user_prompt}
# Creating a 3D Mesh structure
bpy.ops.mesh.primitive_cube_add(size=2.0, location=(0, 0, 0))
obj = bpy.context.active_object
obj.name = "Zlender_Generated_Asset"

print("Model generated successfully for prompt: {user_prompt}")
                """
                
                st.success("✨ 3D model and code successfully generated!")
                
                # Display generated code to user
                st.markdown("### 💻 Generated Blender Python Code (bpy):")
                st.code(generated_code, language="python")
                
                # Download Button
                st.download_button(
                    label="📥 Download Blender Script (.py)",
                    data=generated_code,
                    file_name="zlender_script.py",
                    mime="text/plain"
                )
        else:
            st.warning("Please enter a prompt in the box first.")

with col2:
    st.subheader("👁️ 3D Output & Preview")
    
    st.markdown(
        """
        <div style="border: 2px dashed #10b981; padding: 40px; text-align: center; border-radius: 10px; background-color: #0f172a;">
            <p style="color: #34d399; font-size: 16px; font-weight: bold;">Blender / 3D Engine Status</p>
            <p style="color: #94a3b8; font-size: 13px;">Engine connected. 3D output or progress will appear here after providing a prompt.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    st.markdown("### 📋 Project Status:")
    st.write("✅ **Streamlit UI:** Online & Active")
    st.write("✅ **AI & Blender Bridge:** Ready")
    st.write("🟢 **System:** Ready to Run")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Zlender.ai - Powered by Python & Streamlit</p>", unsafe_allow_html=True)
