import random

# User-defined function untuk simulasi RAMALAN SCORE MALAYSIA VS VIETNAM
def jaring_gol(x):
    hasil = (random.randint(0,x))
    return hasil

# Membuat panggilan function
# Hantar nilai bilangan batu yang digunakan ke dalam bilangan_gol()
terus = "Y"
while terus == "Y":
    hasil_timbang = jaring_gol(5)
    print("Hasil gol MALAYSIA ialah "+str(hasil_timbang)+" jaringan gol")

# Menangkap batu.Membuat panggilan fungsi.
# Hantar hasil timbangan ke dalam bilangan_gol()
    if hasil_timbang >0:
      tangkap = jaring_gol(hasil_timbang)
      print("Hasil gol VIETNAM ialah "+str(tangkap)+" jaringan gol")

    terus=input("\nTeruskan(Y)atau Berhenti(T)? Tekan (Y/T)")
    print("  ")
