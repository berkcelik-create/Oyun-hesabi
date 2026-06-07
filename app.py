import streamlit as st

# Session state ile veriyi hafızada tutalım (sayfa yenilenince gitmemesi için)
if 'oyunlar' not in st.session_state:
    st.session_state.oyunlar = {
        "valorant": "Valorant hesabı: Vandal skinleri mevcut.",
        "pubg": "PUBG hesabı: M416 Glacier var."
    }

st.title("🎮 Oyun Hesap Arayüzü")

# 1. Arama Bölümü
st.subheader("🔍 Hesap Ara")
arama = st.text_input("Oyun ismini girin:").lower()
if arama:
    sonuc = st.session_state.oyunlar.get(arama, "Bu oyun kayıtlı değil.")
    st.write(f"**Sonuç:** {sonuc}")

# 2. Veri Ekleme Bölümü (Görsel Arayüzden)
st.divider()
st.subheader("➕ Yeni Oyun Ekle")
yeni_oyun = st.text_input("Oyun Adı:").lower()
yeni_detay = st.text_area("Hesap Detayları:")

if st.button("Kaydet"):
    if yeni_oyun and yeni_detay:
        st.session_state.oyunlar[yeni_oyun] = yeni_detay
        st.success(f"{yeni_oyun} başarıyla eklendi!")
    else:
        st.error("Lütfen tüm alanları doldurun.")
