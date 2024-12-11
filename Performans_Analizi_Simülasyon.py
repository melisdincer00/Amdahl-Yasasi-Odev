import matplotlib.pyplot as plt
import numpy as np

def hizlanma_hesapla(paralel_oran, islemci_sayisi):
    
    return 1 / ((1 - paralel_oran) + (paralel_oran / islemci_sayisi))

def hizlanma_gorsellestir(paralel_oran):
    
    islemciler = np.arange(1, 33)  # 1'den 32'ye kadar işlemci sayıları
    hizlanmalar = [hizlanma_hesapla(paralel_oran, p) for p in islemciler]

    plt.figure(figsize=(10, 6))
    plt.plot(islemciler, hizlanmalar, marker='o', label=f'P = {paralel_oran}')
    plt.title('Amdahl Yasası: Hızlanma Faktörü vs İşlemci Sayısı')
    plt.xlabel('İşlemci Sayısı')
    plt.ylabel('Hızlanma Faktörü')
    plt.grid(True)
    plt.legend()
    plt.show()

def ana():
    print("Amdahl Yasası Görselleştirici")
    try:
        paralel_oran = float(input("Paralel hale getirilebilen kod oranını girin (0 ile 1 arasında): "))
        if not (0 <= paralel_oran <= 1):
            raise ValueError("Paralel hale getirilebilen kod oranı 0 ile 1 arasında olmalıdır.")

        hizlanma_gorsellestir(paralel_oran)
    except ValueError as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    ana()

