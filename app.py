import streamlit as st

st.set_page_config(layout="wide", page_title="Oyun Hesap Yönetim Paneli")

if 'oyunlar' not in st.session_state:
    st.session_state.oyunlar = {
        "valorant": "Vandal skinli, Asil Karambit",
        "pubg": "M416 Glacier, 500 UC"
    }

st.title("🎮 Oyun Hesap Yönetim Paneli")

col1, col2, col3 = st.columns([1, 1, 1])

# --- 1. ARAMA PANELİ ---
with col1:
    st.subheader("🔍 Akıllı Arama")
    with st.container(border=True):
        arama = st.text_input("Arama terimi:").lower()
        if arama:
            bulundu = False
            for oyun, detay in st.session_state.oyunlar.items():
                if arama in oyun.lower() or arama in detay.lower():
                    st.success(f"**{oyun.upper()}**: {detay}")
                    bulundu = True
            if not bulundu: st.warning("Bulunamadı.")

# --- 2. EKLEME PANELİ ---
with col2:
    st.subheader("➕ Yeni Ekle")
    with st.container(border=True):
        yeni_oyun = st.text_input("Oyun Adı:")
        yeni_detay = st.text_area("Detay:")
        if st.button("Kaydet"):
            st.session_state.oyunlar[yeni_oyun.lower()] = yeni_detay
            st.rerun()

# --- 3. SİLME PANELİ ---
with col3:
    st.subheader("🗑️ Kayıt Sil")
    with st.container(border=True):
        # Silinecek oyunu seçmek için bir dropdown (açılır liste)
        silinecek_oyun = st.selectbox("Silinecek oyunu seçin:", list(st.session_state.oyunlar.keys()))
        if st.button("Seçili Oyunu Sil"):
            if silinecek_oyun in st.session_state.oyunlar:
                del st.session_state.oyunlar[silinecek_oyun]
                st.success(f"'{silinecek_oyun}' silindi!")
                st.rerun()

st.divider()
st.subheader("📋 Mevcut Hesaplar")
st.table(st.session_state.oyunlar)
