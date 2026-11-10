import streamlit as st
from translations import CEVIRI, DIL_ISIMLERI, RTL_DILLER

st.set_page_config(page_title="GuideMatch", page_icon="🧭")

# --- Dil seçimi ---
if "dil" not in st.session_state:
    st.session_state.dil = "tr"

dil = st.sidebar.selectbox(
    "🌐 " + CEVIRI[st.session_state.dil]["secilen_dil"],
    list(DIL_ISIMLERI.keys()),
    format_func=lambda x: DIL_ISIMLERI[x],
    index=list(DIL_ISIMLERI.keys()).index(st.session_state.dil),
)
st.session_state.dil = dil
t = CEVIRI[dil]

# RTL desteği (Arapça)
if dil in RTL_DILLER:
    st.markdown("<style>.stApp {direction: rtl; text-align: right;}</style>", unsafe_allow_html=True)

st.title(t["baslik"])
st.caption(t["altbaslik"])

# --- Demo rehberler (şimdilik) ---
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

st.header(t["rehberler"])

for i, r in enumerate(rehberler):
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            rozet = t["dogrulanmis"] if r["dogrulanmis"] else t["bekliyor"]
            st.markdown(f"### {r['ad']} ⭐ {r['puan']} · {rozet}")
            st.write(f"📍 {r['sehir']} · 🗣️ {r['diller']} · 🎯 {r['uzmanlik']}")
            st.write(f"💰 **{r['fiyat']} {t['gunluk']}**")
        with col2:
            if st.button(t["detay_gor"], key=f"detay_{i}"):
                st.session_state["secili"] = i

# --- Detay paneli ---
if "secili" in st.session_state:
    r = rehberler[st.session_state["secili"]]
    st.divider()
    st.header(f"📋 {r['ad']}")
    st.write(f"**{t['sehir']}:** {r['sehir']}")
    st.write(f"**{t['diller']}:** {r['diller']}")
    st.write(f"**{t['uzmanlik']}:** {r['uzmanlik']}")
    st.write(f"**{t['fiyat']}:** {r['fiyat']} {t['gunluk']}")
    st.write(f"**{t['puan']}:** ⭐ {r['puan']}")
    st.write(f"**{t['telefon']}:** {r['telefon']}")
    st.write(f"**{t['hakkinda']}:** {r['hakkinda']}")
    if st.button(t["kapat"]):
        del st.session_state["secili"]
        st.rerun()
