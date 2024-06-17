import streamlit as st
from parser_validator import SentenceValidator
from token_identifier import TokenIdentifier

def main():
    st.title("Tubes TBA - SPOK")
    st.write("##### Anggota Kelompok: ")
    st.write("##### - Moza Qonita        | 1301220378")
    st.write("##### - Ananta Firdiansyah | 1301220277")
    st.write("")
    st.write("")

    st.write("""
    Masukkan kalimat berbahasa Indonesia untuk memeriksa kevalidan struktur SPOK-nya.
    Struktur yang dikenali adalah:
    - S – P – O – K
    - S – P – K
    - S – P – O
    - S – P
    """)

    # Tampilkan daftar kalimat yang dikenali oleh token identifier
    st.write("### Daftar Kata yang Dikenali:")
    identifier = TokenIdentifier()
    st.write("#### Subyek (S):")
    st.write(", ".join([key for key, value in identifier.valid_tokens.items() if value == "S"]))
    st.write("#### Predikat (P):")
    st.write(", ".join([key for key, value in identifier.valid_tokens.items() if value == "P"]))
    st.write("#### Obyek (O):")
    st.write(", ".join([key for key, value in identifier.valid_tokens.items() if value == "O"]))
    st.write("#### Keterangan (K):")
    st.write(", ".join([key for key, value in identifier.valid_tokens.items() if value == "K"]))

    kalimat = st.text_area("Masukkan kalimat:")

    if st.button("Periksa"):
        validator = SentenceValidator()
        hasil, struktur = validator.validate(kalimat)
        st.write(f"Hasil: {hasil}")
        st.write(f"Struktur Kalimat: {'-'.join(struktur)}")

if __name__ == "__main__":
    main()
