import streamlit as st

# Sayfa ayarları
st.set_page_config(layout="wide", page_title="Oyun Hesap Yönetim Paneli")

# Veri kalıcılığı için session_state (Sayfa yenilense de veriler gitmez)
if 'oyunlar' not in st.session_state:
    st.session_state.oyunlar = {
        "valorant": "Vandal skinli, Asil Karambit, 200 VP",
        "pubg": "M416 Glacier, 500 UC, seviye 3 kask",
        "csgo": "Kelebek bıçak, özel eldivenler, prime hesap"
    }

st.title("🎮 Oyun Hesap Yönetim Paneli")

# Sayfayı iki ana panele bölme
col1, col2 = st.columns([1, 1])

# --- SOL PANEL: ARAMA ---
with col1:
    st.subheader("🔍 Akıllı Hesap Arama")
    with st.container(border=True):
        st.write("Oyun ismi veya içerik detayına göre arama yapın:")
        arama = st.text_input("Arama terimi girin:").lower()
        
        if arama:
            bulundu = False
            for oyun, detay in st.session_state.oyunlar.items():
                # Hem isme hem detaya bakıyor
                if arama in oyun.lower() or arama in detay.lower():
                    st.success(f"Oyun: **{oyun.upper()}**")
                    st.write(f"Detaylar: {detay}")
                    st.write("---")
                    bulundu = True
            
            if not bulundu:
                st.warning("Hiçbir sonuç bulunamadı.")

# --- SAĞ PANEL: EKLEME ---
with col2:
    st.subheader("➕ Yeni Hesap Ekle")
    with st.container(border=True):
        yeni_oyun = st.text_input("Oyun Adı:")
        yeni_detay = st.text_area("Hesap Detayları:")
        
        if st.button("Sisteme Kaydet"):
            if yeni_oyun and yeni_detay:
                st.session_state.oyunlar[yeni_oyun.lower()] = yeni_detay
                st.success(f"'{yeni_oyun}' başarıyla kaydedildi!")
                st.rerun() # Sayfayı yenileyerek listeyi günceller
            else:
                st.error("Lütfen tüm alanları doldurun.")

# --- ALT PANEL: LİSTE ---
st.divider()
st.subheader("📋 Mevcut Hesaplar Listesi")
with st.expander("Tüm kayıtları görüntüle"):
    st.table(st.session_state.oyunlar)
