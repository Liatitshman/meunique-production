import streamlit as st

def add_chat_widget():
    """מוסיף צ'אט חכם לכל עמוד"""
    with st.sidebar:
        st.markdown("---")
        st.markdown("### 💬 צ'אט עזרה")
        
        # צ'אט מוטמע
        user_input = st.text_input("שאל אותי כל דבר:", key="chat_input")
        
        if user_input:
            with st.spinner("חושב..."):
                # כאן יהיה החיבור ל-AI
                response = f"אני כאן לעזור עם: {user_input}"
                st.info(response)
        
        # כפתורי עזרה מהירה
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🚀 איך להשתמש"):
                st.info("לחץ על הטאבים למעלה")
        with col2:
            if st.button("🔧 בעיה טכנית"):
                st.info("נסה לרענן את הדף")

# הוסף לכל עמוד:
# add_chat_widget() 