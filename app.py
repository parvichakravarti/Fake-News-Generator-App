import streamlit as st
import random
from datetime import datetime

# --------------------------------------------------
# CONFIGURE PAGE
# --------------------------------------------------
st.set_page_config(
    page_title="Fake News Headline Generator 📰",
    page_icon="🗞️",
    layout="centered"
)

# --------------------------------------------------
# INTRO SECTION
# --------------------------------------------------
st.title("📰 Fake News Headline Generator")
st.markdown("""
your one-stop place to create the funniest and creative fake headlines!😄  
---
""")

# --------------------------------------------------
# DATA
# --------------------------------------------------
categories = {
    "Celebrities": [
        "Shah Rukh Khan", "Virat Kohli", "Alia Bhatt",
        "Salman Khan", "Deepika Padukone", "Kareena Kapoor"
    ],
    "Politics": [
        "Prime Minister Modi", "Nirmala Sitharaman", "Rahul Gandhi",
        "Arvind Kejriwal", "A Delhi MLA", "A Secret Minister"
    ],
    "Animals": [
        "A Mumbai Cat", "A Group of Monkeys", "A Clever Dog",
        "An Angry Cow", "A Dancing Peacock", "A Sleepy Panda"
    ],
    "Common People": [
        "An Auto Rickshaw Driver from Delhi", "A College Student",
        "A Chai Seller", "A School Teacher", "A Street Vendor", "A YouTuber"
    ],
    "Tech & AI": [
        "ChatGPT", "Elon Musk", "A Robot from Bengaluru", "Google Bard",
        "A Tech Intern", "AI-powered Rickshaw"
    ]
}

actions = [
    "launches a rocket",
    "cancels a flight mid-air",
    "dances with a boxer",
    "eats 50 samosas in one sitting",
    "declares war on Apple",
    "starts a YouTube channel",
    "celebrates birthday with aliens",
    "opens a tech startup",
    "learns Python overnight",
    "joins Indian Idol"
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
    "on top of Mount Everest",
    "in the middle of a Zoom meeting"
]

# --------------------------------------------------
# SIDEBAR CONFIGURATION
# --------------------------------------------------
st.sidebar.header("🎛️ Customize Your Experience")

selected_category = st.sidebar.selectbox(
    "Choose a category:", list(categories.keys())
)

num_headlines = st.sidebar.slider(
    "Number of headlines to generate", 1, 5, 1
)

mode = st.sidebar.radio(
    "Headline Style:",
    ["Funny", "Serious", "Crazy Mode 🤯"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 Tip: Try ‘Crazy Mode’ for totally random combinations!")

# --------------------------------------------------
# GENERATE FUNCTION
# --------------------------------------------------
def generate_headline(category, mode):
    subject = random.choice(categories[category])
    action = random.choice(actions)
    place = random.choice(places)

    headline = f"**Breaking News:** {subject} {action} {place}!"
    
    if mode == "Funny":
        headline += " 😂"
    elif mode == "Serious":
        headline = headline.replace("Breaking News", "Exclusive Report").replace("!", ".")
    elif mode == "Crazy Mode 🤯":
        headline = f"🚨 {subject.upper()} {action.upper()} {place.upper()}!!! 🌀🔥"

    return headline

# --------------------------------------------------
# MAIN SECTION
# --------------------------------------------------
if "history" not in st.session_state:
    st.session_state.history = []

st.subheader("🗞️ Generate Your Fake Headlines")

if st.button("🎲 Generate Now"):
    st.markdown("### 🧠 Headlines Generated:")
    for _ in range(num_headlines):
        new_headline = generate_headline(selected_category, mode)
        st.markdown(f"<p style='font-size:20px; margin-bottom:10px;'>{new_headline}</p>", unsafe_allow_html=True)
        st.session_state.history.append((datetime.now().strftime("%H:%M:%S"), new_headline))
    st.success("✅ Done! Scroll below for your headline history.")
else:
    st.info("Click the **Generate Now** button above to see your headlines!")

# --------------------------------------------------
# CUSTOM HEADLINE BUILDER
# --------------------------------------------------
st.markdown("---")
st.subheader("🖋️ Create Your Own Custom Headline")

user_subject = st.text_input("Who or what is your subject? (e.g., My Cat)")
user_action = st.text_input("What action did they do? (e.g., Became a DJ)")
user_place = st.text_input("Where did it happen? (e.g., In my kitchen)")

if st.button("✨ Create My Custom Headline"):
    if user_subject and user_action and user_place:
        custom_headline = f"**Breaking News:** {user_subject} {user_action} {user_place}!"
        st.success(custom_headline)
        st.session_state.history.append((datetime.now().strftime("%H:%M:%S"), custom_headline))
    else:
        st.warning("Please fill in all three fields before creating a headline!")

# --------------------------------------------------
# HEADLINE HISTORY
# --------------------------------------------------
if st.session_state.history:
    st.markdown("---")
    st.subheader("📜 Headline History")
    for time, headline in reversed(st.session_state.history[-10:]):
        st.markdown(f"<p style='font-size:16px;'><b>{time}</b> — {headline}</p>", unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")
st.caption("🧠 Built with ❤️ using Streamlit | Have fun responsibly 😄")
