import streamlit as st

def munculkan_kontak():
    st.title("Kontak")
    st.write("Hubungi saya melalui tautan berikut:")

    # LinkedIn
    st.markdown(
        "[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/irfadillah-afni-nurvita/)"
    )

    # WhatsApp
    st.markdown(
        "[![WhatsApp](https://img.shields.io/badge/WhatsApp-Profile-brightgreen)](https://wa.me/6282123970898)"
    )

    # Email
    st.write("📧 Email: irfadillahafninurvita@gmail.com")


