# 🧠 تصميم أولي للعبة السجينين عبر الإنترنت (Streamlit + SQLite)

import streamlit as st
import sqlite3
import time

# --- إعداد القاعدة ---
conn = sqlite3.connect("game.db", check_same_thread=False)
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        move TEXT,
        round INTEGER,
        score INTEGER DEFAULT 0,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()

# --- إدخال اسم اللاعب ---
st.set_page_config(page_title="لعبة السجينين عبر الإنترنت", layout="centered")
st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)

st.title("🎮 لعبة السجينين - عبر الإنترنت")

player_name = st.text_input("👤 أدخل اسمك:")
if player_name:
    st.success(f"مرحبًا {player_name}! انتظر خصمًا آخر للانضمام...")
    c.execute("SELECT COUNT(*) FROM players WHERE round = 1")
    players_count = c.fetchone()[0]

    # إدخال اللاعب الحالي
    c.execute("SELECT * FROM players WHERE name=?", (player_name,))
    if not c.fetchone():
        c.execute("INSERT INTO players (name, move, round) VALUES (?, ?, 1)", (player_name, "",))
        conn.commit()

    # انتظار اللاعب الثاني
    while players_count < 2:
        c.execute("SELECT COUNT(*) FROM players WHERE round = 1")
        players_count = c.fetchone()[0]
        time.sleep(2)
        st.info("🕒 في انتظار خصم آخر...")
        st.experimental_rerun()

    # عرض خيارات اللعب
    move = st.radio("اختر حركتك:", ["🤝 التعاون", "❌ الخيانة"])
    if st.button("🚀 أرسل الحركة"):
        c.execute("UPDATE players SET move=? WHERE name=?", (move, player_name))
        conn.commit()
        st.success("✅ تم إرسال حركتك!")

    # انتظار اللاعب الآخر لإرسال الحركة
    while True:
        c.execute("SELECT COUNT(*) FROM players WHERE move != '' AND round = 1")
        moves_done = c.fetchone()[0]
        if moves_done == 2:
            break
        time.sleep(2)
        st.info("⏳ انتظار الخصم...")
        st.experimental_rerun()

    # عرض النتائج
    c.execute("SELECT name, move FROM players WHERE round = 1")
    data = c.fetchall()
    player1, move1 = data[0]
    player2, move2 = data[1]

    payoff_matrix = {
        ("🤝 التعاون", "🤝 التعاون"): (3, 3),
        ("🤝 التعاون", "❌ الخيانة"): (0, 5),
        ("❌ الخيانة", "🤝 التعاون"): (5, 0),
        ("❌ الخيانة", "❌ الخيانة"): (1, 1)
    }
    score1, score2 = payoff_matrix[(move1, move2)]

    st.markdown("## ✅ النتيجة")
    st.write(f"{player1}: {move1} ({score1} نقطة)")
    st.write(f"{player2}: {move2} ({score2} نقطة)")

    # عرض من الفائز
    if player_name == player1:
        st.success("🎉 أنت الفائز!" if score1 > score2 else ("🔁 تعادل!" if score1 == score2 else "❌ لقد خسرت."))
    else:
        st.success("🎉 أنت الفائز!" if score2 > score1 else ("🔁 تعادل!" if score1 == score2 else "❌ لقد خسرت."))

    # تنظيف البيانات للجولة القادمة (اختياري - تطوير لاحقًا)

st.markdown("</div>", unsafe_allow_html=True)
