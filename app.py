import streamlit as st
import math

st.title("Simulasi EOQ - Economic Order Quantity")

st.write("Masukkan data berikut:")
D = st.number_input("Permintaan Tahunan (D)", value=2000)
S = st.number_input("Biaya Pemesanan per Order (S)", value=150000)
H = st.number_input("Biaya Penyimpanan per Unit per Tahun (H)", value=3000)

if D > 0 and S > 0 and H > 0:
    EOQ = math.sqrt((2 * D * S) / H)
    freq = D / EOQ
    st.subheader("Hasil Perhitungan:")
    st.write(f"EOQ (Jumlah Pemesanan Optimal): {EOQ:.2f} unit")
    st.write(f"Frekuensi Pemesanan per Tahun: {freq:.2f} kali")
    total_cost = (D / EOQ) * S + (EOQ / 2) * H
    st.write(f"Total Biaya Persediaan: Rp {total_cost:,.2f}")
else:
    st.warning("Masukkan semua nilai dengan benar.")
