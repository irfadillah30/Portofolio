import streamlit as st

st.set_page_config(layout='wide')
st.title('Portfolio Saya')
st.header('Data Scientist')

st.sidebar.title('Irfadillah Afni Nurvita')
page = st.sidebar.radio('', ['Tentang saya', 
                                          'Dashboard', 'Proyek', 
                                          'Kontak'])
if page == 'Tentang saya': 
    import about
    about.about_me()
elif page == 'kontak':
    import kontak
    kontak.munculkan_kontak()
elif page == 'Dashboard':
    import Dashboard
    Dashboard.tampilakan_dashboard()