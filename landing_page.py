import streamlit as st

st.set_page_config(
    page_title="moodmix",
    page_icon="🎶"
)

# CSS styles
css = """
<style>
body {
  margin: 0;
  padding: 0;
  text-align: left;
  min-height: 100vh;
  background-image: linear-gradient(80deg, rgb(5, 124, 172), rgb(199, 10, 114));
  overflow: hidden;
}

#up {
    position: absolute; 
    height: 800px;
    width: 800px;
    border-radius: 50%;
    background-image: linear-gradient(80deg, rgb(5, 124, 172), rgb(43, 247, 202, 0.5));
    filter: blur(80px);
    animation: down 40s infinite;
}
#down {
    position: absolute; 
    right: 0;
    height: 500px;
    width: 500px;
    border-radius: 50%;
    background-image: linear-gradient(80deg, rgba(245, 207, 82, 0.8), rgba(199, 10, 114))
    filter: blur(80px);
    animation: up 30s infinite;
}

#left {
    position: absolute;
    height: 500px;
    width: 500px;
    border-radius: 50%;
    background-image: linear-gradient(80deg, rgb(199, 10, 160), rgba(183, 253, 52, 0.8));
    filter: blur(80px);
    animation: left 40s 1s infinite;
}

#right {
    position: absolute;
    height: 500px;
    width: 500px;
    border-radius: 50%;
    background-image: linear-gradient(80deg, rgba(26, 248, 18, 0.6), rgba(199, 10, 52, 0.8));
    filter: blur(80px);
    animation: right 30s .5s infinite;
}

@keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
}
@keyframes floating {
    0% { transform: translateY(0px); }
    50% { transform: translateY(5px); }
    100% { transform: translateY(0px); }
}

@keyframes down {
    0%, 100%{
        top: -100px;
    }
    70%{
        top: 700px;
    }
}

@keyframes up {
    0%, 100%{
        bottom: -100px;
    }
    70%{
        bottom: 700px;
    }
}
@keyframes left {
    0%, 100%{
        left: -100px;
    }
    70%{
        left: 1000px;
    }
}

@keyframes right {
    0%, 100%{
        right: -100px;
    }
    70%{
        right: 1000px;
    }
}

a:hover {
    color: black;
}
a:hover button {
    background-color: white !important;
    color: black !important;
}
</style>
"""

# HTML content
html = """
<section id="up"></section>
<section id="down"></section>
<section id="left"></section>
<section id="right"></section>
"""

st.markdown(css, unsafe_allow_html=True)
st.markdown(html, unsafe_allow_html=True)

st.markdown("<h1 style='color: white; opacity: 0; animation: fadeIn 8s ease forwards, floating 2s ease infinite;'>"
            "<span style='font-weight:normal; font-family: sans serif; font-size: 50px;'>welcome to </span>"
            "<span style='font-weight:bold; font-family: serif; font-size: 70px; font-weight:bold;'>moodmix.</span>"
            "</h1>", unsafe_allow_html=True)

st.markdown("<p style='opacity: 0; animation: fadeIn 10s ease forwards; font-size: 20px;'><strong>we are always trying to discover new music.</strong><br>" "what if we don't know what songs we want to listen to? "
            "what if we only know a <strong>vibe</strong> or <strong>mood</strong> we want to listen to?<br>"
            "<i><strong>moodmix aims to solve that</strong></i>. <br>" "based on inputted adjectives or nouns fitting the desired atmosphere, "
            "a playlist is generated for you.</p>", unsafe_allow_html=True)

# url = 'https://moodmix-main.streamlit.app'

st.markdown(f'''
<a href='https://moodmix-main.streamlit.app/?embedded=true/' target="_blank"><button style="font-weight:bold; opacity: 0; animation: fadeIn 5s ease forwards; background-color:black; border-radius: 20px; padding: 10px 20px; border: none; color: white;">get started</button></a>
''', unsafe_allow_html=True)

st.markdown("<small>if 'get started' page does not load, click <a href='https://moodmix-main.streamlit.app' target='_blank'>here</a></small>", unsafe_allow_html=True)



# st.link_button("get started", "https://moodmix-main.streamlit.app")

# st.markdown('<a href="https://moodmix-main.streamlit.app" target="_self">get started</a>',unsafe_allow_html=True)
