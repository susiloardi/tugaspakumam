import streamlit as st

# Judul Aplikasi
st.title("Aplikasi Multi-Fitur")
st.write("Kalkulator, Konversi Suhu, dan Deret Fibonacci")

# Membuat menu navigasi
menu = st.sidebar.selectbox(
    "Pilih Fitur",
    ["Kalkulator", "Konversi Suhu", "Deret Fibonacci"]
)

# ------------------ 1. Kalkulator ------------------
if menu == "Kalkulator":
    st.header("Kalkulator Sederhana")

    # Input angka
    num1 = st.number_input("Masukkan angka pertama", value=0.0)
    num2 = st.number_input("Masukkan angka kedua", value=0.0)

    # Pilih operator
    operator = st.selectbox("Pilih operator", ["+", "-", "*", "/"])

    # Hitung hasil
    if st.button("Hitung"):
        if operator == "+":
            hasil = num1 + num2
        elif operator == "-":
            hasil = num1 - num2
        elif operator == "*":
            hasil = num1 * num2
        elif operator == "/":
            if num2 != 0:
                hasil = num1 / num2
            else:
                hasil = "Error: Tidak bisa dibagi 0"
        st.success(f"Hasil: {hasil}")

# ------------------ 2. Konversi Suhu ------------------
elif menu == "Konversi Suhu":
    st.header("Konversi Suhu")

    # Pilih input satuan
    satuan_asal = st.selectbox("Pilih satuan asal", ["Celcius", "Reamur", "Fahrenheit"])
    nilai = st.number_input("Masukkan nilai suhu", value=0.0)

    # Konversi ke satuan lain
    if st.button("Konversi"):
        if satuan_asal == "Celcius":
            reamur = (4/5) * nilai
            fahrenheit = (9/5) * nilai + 32
            st.write(f"{nilai}°C = {reamur}°Re = {fahrenheit}°F")

        elif satuan_asal == "Reamur":
            celcius = (5/4) * nilai
            fahrenheit = (9/4) * nilai + 32
            st.write(f"{nilai}°Re = {celcius}°C = {fahrenheit}°F")

        elif satuan_asal == "Fahrenheit":
            celcius = (5/9) * (nilai - 32)
            reamur = (4/9) * (nilai - 32)
            st.write(f"{nilai}°F = {celcius}°C = {reamur}°Re")

# ------------------ 3. Deret Fibonacci ------------------
elif menu == "Deret Fibonacci":
    st.header("Deret Fibonacci")

    n = st.number_input("Masukkan jumlah n (banyaknya deret)", min_value=1, step=1)

    if st.button("Generate"):
        fibo = [0, 1]
        for i in range(2, int(n)):
            fibo.append(fibo[i-1] + fibo[i-2])
        fibo = fibo[:int(n)]  # ambil n pertama
        st.success(f"Deret Fibonacci {n} angka pertama:")
        st.write(fibo)
