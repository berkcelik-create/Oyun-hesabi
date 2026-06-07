# Arama Bölümü
st.subheader("🔍 Hesap Ara")
with st.container(border=True):
    arama_terimi = st.text_input("Oyun veya detay içinde ara:").lower()
    
    if arama_terimi:
        bulundu = False
        # Hem oyuna hem de detaylara bakıyoruz
        for oyun, detay in st.session_state.oyunlar.items():
            if arama_terimi in oyun.lower() or arama_terimi in detay.lower():
                st.success(f"Bulundu: **{oyun.capitalize()}**")
                st.write(f"Detay: {detay}")
                bulundu = True
        
        if not bulundu:
            st.warning("Hiçbir sonuç bulunamadı.")
