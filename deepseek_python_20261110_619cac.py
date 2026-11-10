import streamlit as st

st.set_page_config(page_title="GuideMatch Test", page_icon="🧭")

st.title("🧭 GuideMatch — Test Sayfası")
st.caption("Bu sadece deneme. Rehberlere tıklayınca detay açılır.")

# --- 2 sahte rehber ---
rehber1 = {
    "ad": "Rehber 1 — Ayşe Yılmaz",
    "sehir": "İstanbul",
    "diller": "TR, EN, DE",
    "uzmanlik": "Tarihi Yarımada",
    "fiyat": 800,
    "puan": 4.9,
    "telefon": "555-0001",
    "dogrulanmis": True,
    "hakkinda": "10 yıllık deneyim. Ayasofya, Topkapı, Sultanahmet turları.",
}

rehber2 = {
    "ad": "Rehber 2 — Mehmet Demir",
    "sehir": "Kapadokya",
    "diller": "TR, EN, RU",
    "uzmanlik": "Balon turları",
    "fiyat": 1200,
    "puan": 4.7,
    "telefon": "555-0002",
    "dogrulanmis": True,
    "hakkinda": "Kapadokya'da 8 yıl. Balon, vadi yürüyüşleri, ATV turları.",
}

rehberler = [rehber1, rehber2]

# --- Liste ---
st.header("Rehberler")

for i, r in enumerate(rehberler):
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])

        with col1:
            rozet = "✅ Doğrulanmış" if r["dogrulanmis"] else "⏳ Bekliyor"
            st.markdown(f"### {r['ad']} ⭐ {r['puan']} · {rozet}")
            st.write(f"📍 {r['sehir']} · 🗣️ {r['diller']} · 🎯 {r['uzmanlik']}")
            st.write(f"💰 **{r['fiyat']} ₺/gün**")

        with col2:
            if st.button("Detay Gör", key=f"detay_{i}"):
                st.session_state["secili"] = i

# --- Detay paneli ---
if "secili" in st.session_state:
    r = rehberler[st.session_state["secili"]]
    st.divider()
    st.header(f"📋 {r['ad']}")
    st.write(f"**Şehir:** {r['sehir']}")
    st.write(f"**Diller:** {r['diller']}")
    st.write(f"**Uzmanlık:** {r['uzmanlik']}")
    st.write(f"**Fiyat:** {r['fiyat']} ₺/gün")
    st.write(f"**Puan:** ⭐ {r['puan']}")
    st.write(f"**Telefon:** {r['telefon']}")
    st.write(f"**Hakkında:** {r['hakkinda']}")

    if st.button("Kapat"):
        del st.session_state["secili"]
        st.rerun()