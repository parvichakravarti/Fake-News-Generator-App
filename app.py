# fake_news_generator_app.py
# --------------------------
# A fun Streamlit web app that generates random, fake news headlines

import streamlit as st
import random

# --------------------------
# CONFIGURE PAGE
# --------------------------
st.set_page_config(
    page_title="Fake News Headline Generator 📰",
    page_icon="🗞️",
    layout="centered"
)

# --------------------------
# APP TITLE AND INTRO
# --------------------------
st.title("📰 Fake News Headline Generator")
st.markdown(
    """
    Generate hilarious and totally fake headlines in seconds!😄  
    ---
    """
)

# --------------------------
# DATA
# --------------------------
categories = {
    "Celebrities": [
        "Shah Rukh Khan",
        "Virat Kohli",
        "Alia Bhatt",
        "Salman Khan",
        "Kareena Kapoor"
    ],
    "Politics": [
        "Prime Minister Modi",
        "Nirmala Sitharaman",
        "Rahul Gandhi",
        "Arvind Kejriwal",
        "A Delhi MLA"
    ],
    "Animals": [
        "A Mumbai Cat",
        "A Group of Monkeys",
        "A Clever Dog",
        "An Angry Cow",
        "A Dancing Peacock"
    ],
    "Common People": [
        "An Auto Rickshaw Driver from Delhi",
        "A College Student",
        "A Chai Seller",
        "A School Teacher",
        "A Street Vendor"
    ]
}

actions = [
    "launches a rocket",
    "cancels a ticket",
    "dances with a boxer",
    "eats 50 samosas",
    "declares war on Apple",
    "orders a 10-layer cake",
    "celebrates birthday with aliens",
    "starts a podcast",
    "opens a tech company",
    "learns Python overnight"
]

places = [
    "at Red Fort",
    "in a Mumbai Local Train",
    "inside Parliament",
    "during an IPL match",
    "at Ganga Ghat",
    "at India Gate",
    "in a crowded metro",
    "inside a classroom",
    "on top of Mount Everest"
]

# --------------------------
# SIDEBAR SETTINGS
# --------------------------
st.sidebar.header("⚙️ Customize Your Headlines")

selected_category = st.sidebar.selectbox(
    "Choose a category:", list(categories.keys())
)

num_headlines = st.sidebar.slider(
    "Number of headlines to generate", 1, 5, 1
)

st.sidebar.info("Tip: Change category and hit 'Generate' for different results!")

# --------------------------
# GENERATE HEADLINES
# --------------------------
if st.button("🎲 Generate Headlines"):
    st.subheader("🗞️ Breaking News Just In!")

    for _ in range(num_headlines):
        subject = random.choice(categories[selected_category])
        action = random.choice(actions)
        place = random.choice(places)

        headline = f"**Breaking News:** {subject} {action} {place}!"
        st.markdown(f"<p style='font-size:18px; margin-bottom:10px;'>{headline}</p>", unsafe_allow_html=True)

    st.success("✨ Headlines generated successfully!")

else:
    st.info("Click 'Generate Headlines' to get your fake news dose!")

# --------------------------
# FOOTER
# --------------------------
st.markdown("---")
st.caption("🧠 Created for fun using Streamlit | 2025 Fake News")
