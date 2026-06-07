import streamlit as st

# Veri kaynağın (Bunu daha sonra JSON veya veritabanından da çekebilirsin)
oyun_verileri = {
    "valorant": "Valorant hesabında: Vandal Skinleri, Asil Karambit ve 200 VP mevcut.",
    "pubg": "PUBG hesabında: M416 Glacier, 500 UC ve seviye 3 kask kaplaması var.",
    "league of legends": "LoL hesabında: Elementalist Lux, 150 şampiyon ve Altın küme çerçevesi var.",
    "ready or not": "Ready or Not hesabında: Tüm özel harekat üniteleri açık."
}

st.title("🎮 Oyun Hesap Arama Motoru")
st.write("Aramak istediğin oyunun adını yaz, hesabındaki özellikleri görelim.")

# Arama kutusu
arama = st.text_input("Oyun ismini girin:").lower()

if arama:
    # Eşleşen oyunları bulma
    bulundu = False
    for oyun, detay in oyun_verileri.items():
        if arama in oyun:
            st.success(f"Sonuç: **{oyun.capitalize()}**")
            st.info(detay)
            bulundu = True
    
    if not bulundu:
        st.warning("Maalesef bu oyuna ait bir hesap bilgisi bulunamadı.")
