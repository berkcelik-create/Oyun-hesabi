import streamlit as st

# Sayfa ayarları
st.set_page_config(layout="wide", page_title="Oyun Panelim")

if 'oyunlar' not in st.session_state:
    st.session_state.oyunlar = {"valorant": "Vandal skinli hesap"}

st.title("🎮 Oyun Hesap Yönetim Paneli")

# 1. Sütunlara bölme (Panel yapısı için)
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🔍 Hesap Arama")
    with st.container(border=True): # Çerçeveli kutu içinde
        arama = st.text_input("Oyun ismini yazın:").lower()
        if arama:
            sonuc = st.session_state.oyunlar.get(arama, "Kayıt bulunamadı.")
            st.success(f"Sonuç: {sonuc}")

with col2:
    st.subheader("➕ Yeni Kayıt Ekle")
    with st.container(border=True): # Çerçeveli kutu içinde
        yeni_oyun = st.text_input("Oyun Adı:")
        yeni_detay = st.text_area("Hesap Detayları:")
        if st.button("Sisteme Kaydet"):
            if yeni_oyun and yeni_detay:
                st.session_state.oyunlar[yeni_oyun.lower()] = yeni_detay
                st.success("Başarıyla eklendi!")
            else:
                st.warning("Boş alan bırakma.")

# 2. Alt kısma bir liste paneli ekleyelim
st.divider()
st.subheader("📋 Mevcut Hesaplar")
with st.expander("Kayıtlı oyun listesini gör"):
    st.table(st.session_state.oyunlar)
