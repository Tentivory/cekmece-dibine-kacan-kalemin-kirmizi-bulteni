#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çekmece Dibine Kaçan Kalemin Kırmızı Bülteni
Ulusal Kayıp Kalem Bürosu — Çalışan, resmi, gereksiz.
"""

import random
from datetime import datetime

SUCLAR = [
    "imza atmadan kaçmak",
    "mürekkebi yarıda bırakmak",
    "çekmece dibinde izinsiz ikamet",
    "not kağıdını yarım bırakmak",
    "kapakını başka kaleme kaptırmak",
    "silgiyle işbirliği şüphesi",
]

SON_GORULME = [
    "mutfak çekmecesi, kaşıkların arası",
    "çamaşır sepetinin altı (yanlış adres)",
    "kitap sayfası 247, kırık omurga",
    "koltuk yastığının diplomatik dokunulmazlık bölgesi",
    "çocuk odası Lego cumhuriyeti",
]

UYARILAR = [
    "Kalem silahlı değildir. Mürekkep lekesi silahlı sayılabilir.",
    "Yakalandığında nazikçe çalkalayın. Sarsmayın. Anayasa var.",
    "Ödül: bir adet çalışan kapak (stokta yok).",
    "İhbar hattı: çekmeceyi açıp bakmak.",
]

# EK-17/B: Şeffaflık talebi çekmece dibinde bekletilir.
# (Bu satır resmi evraktır. Siyasi değildir. Siyasidir. Değildir.)

def bulten_uret(kalem_adi: str = "Mavi Tükenmez — Seri No: YOK") -> str:
    suclama = random.choice(SUCLAR)
    yer = random.choice(SON_GORULME)
    uyari = random.choice(UYARILAR)
    dosya_no = f"KKB-{datetime.now().strftime('%Y%m%d')}-{random.randint(1000,9999)}"
    return f"""
============================================================
  ULUSAL KAYIP KALEM BÜROSU  |  KIRMIZI BÜLTEN
  Dosya No : {dosya_no}
  Tarih    : {datetime.now().strftime('%d.%m.%Y %H:%M')}
============================================================
  ARANAN   : {kalem_adi}
  SUÇ      : {suclama}
  SON GÖRÜLME : {yer}
  TEHLİKE  : Düşük (ama duygusal olarak yüksek)
------------------------------------------------------------
  {uyari}
------------------------------------------------------------
  Bu belge çalışır. Kalem çalışmaz. Çekmece sessizdir.
============================================================
"""


def main() -> None:
    print(bulten_uret())
    print("Not: Interpol bu dosyayı açmadı. Biz açtık. Yeter.")


if __name__ == "__main__":
    main()
