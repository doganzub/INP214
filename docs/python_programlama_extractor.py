#!/usr/bin/env python3
"""
Python Programlama PDF -> Markdown Dönüştürücü (Temiz ve Eksiksiz)

/tmp/pdf_extracted.txt dosyasını temizleyerek
/Users/zuber/INP104/docs/python_programlama.md oluşturur.

Temizlik işlemleri:
- "=== SAYFA X ===" satırları kaldırılır
- "5.01.2024 13:31" header satırları kaldırılır
- "Ders : PYTHON PROGRAMLAMA - eKtap" satırları kaldırılır
- "about:blank X/170" prefix'leri kaldırılır (sonrasındaki içerik korunur)
- Bölüm başlıkları markdown heading'e dönüştürülür
- Ardışık boş satırlar azaltılır

Kullanım:
    python python_programlama_extractor.py
"""

import re
import os


EXTRACTED_TEXT = "/tmp/pdf_extracted.txt"
BASE_DIR = "/Users/zuber/INP104"
OUTPUT_MD = os.path.join(BASE_DIR, "docs", "python_programlama.md")


def clean_extracted_text(raw_lines):
    """Ham PDF metnini temizle ve satır listesi olarak döndür"""
    cleaned = []
    in_toc = False  # İçindekiler sayfasında mıyız

    for line in raw_lines:
        line = line.rstrip("\n")

        # === SAYFA X === satırlarını atla
        if re.match(r"^=== SAYFA \d+ ===$", line.strip()):
            if in_toc:
                in_toc = False  # İçindekiler sayfası bitti
            cleaned.append("")
            continue

        # "5.01.2024 13:31" ile başlayan header satırlarını atla
        if "5.01.2024 13:31" in line:
            continue

        # "Ders : PYTHON PROGRAMLAMA" satırlarını atla
        if "Ders : PYTHON PROGRAMLAMA" in line:
            continue

        # about:blank X/170 prefix'ini kaldır, sonrasındaki içeriği koru
        # NOT: /170 sabit, greedy \d+ "1702" gibi section numarasını yutmasın
        m = re.match(r"^about:blank\s+\d+/170(.*)", line.strip())
        if m:
            remainder = m.group(1).strip()
            if remainder:
                # İçindekiler sayfası başlangıcı
                if remainder == "İÇİNDEKİLER":
                    in_toc = True
                    continue
                # about:blank sonrası gelen bölüm başlıkları: §HEADING§ ile işaretle
                # Sadece 1-8 arası ana bölüm numaraları (tek haneli + büyük harfle başlayan)
                if re.match(r"^[1-8]\.\s+[A-ZÜĞŞÇÖİ]", remainder):
                    cleaned.append(f"§HEADING§{remainder}")
                else:
                    cleaned.append(remainder)
            continue

        # İçindekiler sayfasındaki bölüm listesini atla (başlığa çevirme)
        if in_toc:
            continue

        cleaned.append(line)

    return cleaned


def format_section_headings(lines):
    """Bölüm başlıklarını markdown heading formatına dönüştür"""
    result = []

    # §HEADING§ ile işaretlenmiş ana bölüm başlıklarını dönüştür
    heading_fixes = {
        "PROGRAMLAMA YA GİRİŞ": "PROGRAMLAMAYA GİRİŞ",
        "KOŞUL  İFADELERİ": "KOŞUL İFADELERİ",
        "NUMPY  VE P ANDAS": "NUMPY VE PANDAS",
        "KÜTÜPHANELERİ İLE": "KÜTÜPHANELERİ İLE ÇALIŞMA",
        "DEMET , KÜME,": "DEMET, KÜME, SÖZLÜK",
    }

    skip_next_sozluk = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # "SÖZLÜK" tek satırda gelebilir (3. bölüm başlığının devamı)
        if skip_next_sozluk and stripped == "SÖZLÜK":
            skip_next_sozluk = False
            continue

        # §HEADING§ ile işaretlenmiş ana bölüm başlıkları
        if stripped.startswith("§HEADING§"):
            heading_text = stripped.replace("§HEADING§", "").strip()
            # Bilinen hataları düzelt
            for wrong, correct in heading_fixes.items():
                heading_text = heading_text.replace(wrong, correct)
            result.append("")
            result.append(f"# {heading_text}")
            result.append("")
            if "KÜME," in heading_text and "SÖZLÜK" not in heading_text:
                skip_next_sozluk = True
            continue

        # Alt bölüm başlıkları: X.Y. veya X.Y.Z.
        sub_sub_match = re.match(r"^(\d+\.\d+\.\d+\.)\s+(.*)", stripped)
        if sub_sub_match and len(stripped) < 120:
            num = sub_sub_match.group(1).rstrip(".")
            title = sub_sub_match.group(2).strip()
            if title and len(title) > 2:
                result.append("")
                result.append(f"### {num}. {title}")
                result.append("")
                continue

        sub_match = re.match(r"^(\d+\.\d+\.)\s+(.*)", stripped)
        if sub_match and len(stripped) < 120:
            num = sub_match.group(1).rstrip(".")
            title = sub_match.group(2).strip()
            if title and len(title) > 2:
                result.append("")
                result.append(f"## {num}. {title}")
                result.append("")
                continue

        # Önemli alt başlıklar
        bold_headings = [
            "Kazanımlar", "Brlkte Düşünelm", "Birlikte Düşünelim",
            "Başlamadan Önce", "Bölüm Özet", "Bölüm Özeti",
            "Kaynakça", "Ünte Soruları", "Ünite Soruları",
            "Değşken Tanımlama Kuralları", "Değişken Tanımlama Kuralları",
            "Intern Nesneler", "İntern Nesneler",
            "Bölümle İlgl Özlü Söz", "Bölümle İlgili Özlü Söz",
        ]
        if stripped in bold_headings:
            result.append("")
            result.append(f"**{stripped}**")
            result.append("")
            continue

        result.append(line)

    return result


def reduce_blank_lines(lines):
    """Ardışık boş satırları en fazla 2'ye düşür"""
    result = []
    blank_count = 0
    for line in lines:
        if line.strip() == "":
            blank_count += 1
            if blank_count <= 2:
                result.append("")
        else:
            blank_count = 0
            result.append(line)
    return result


def build_markdown(lines):
    """Son markdown metnini oluştur"""
    header = """# PYTHON PROGRAMLAMA - eKitap

**Züber Doğan**
Yeditepe Üniversitesi - Meslek Yüksekokulu

---

## İÇİNDEKİLER

1. Python ile Programlamaya Giriş
2. Değişkenler ve Veri Tipleri
3. Veri Yapıları: Liste, Demet, Küme, Sözlük
4. Koşul İfadeleri
5. Döngüler
6. Fonksiyonlar
7. Nesneye Yönelik Programlama
8. NumPy ve Pandas Kütüphaneleri ile Çalışma

---

"""
    body = "\n".join(lines)
    return header + body


def main():
    print("=" * 60)
    print("PYTHON PROGRAMLAMA PDF -> MD (Temiz ve Eksiksiz)")
    print("=" * 60)

    if not os.path.exists(EXTRACTED_TEXT):
        print(f"HATA: {EXTRACTED_TEXT} bulunamadı!")
        return

    # 1. Ham metni oku
    print(f"\n[1/5] Okunuyor: {EXTRACTED_TEXT}")
    with open(EXTRACTED_TEXT, "r", encoding="utf-8") as f:
        raw_lines = f.readlines()
    print(f"  -> {len(raw_lines)} satır okundu")

    # 2. Temizle
    print("[2/5] Sayfa başlıkları ve gereksiz satırlar temizleniyor...")
    cleaned = clean_extracted_text(raw_lines)
    print(f"  -> {len(cleaned)} satır kaldı")

    # 3. Bölüm başlıklarını formatla
    print("[3/5] Bölüm başlıkları markdown formatına dönüştürülüyor...")
    formatted = format_section_headings(cleaned)

    # 4. Boş satırları azalt
    print("[4/5] Ardışık boş satırlar azaltılıyor...")
    reduced = reduce_blank_lines(formatted)
    print(f"  -> {len(reduced)} satır (son)")

    # 5. Markdown oluştur ve yaz
    print(f"[5/5] Yazılıyor: {OUTPUT_MD}")
    md_text = build_markdown(reduced)

    os.makedirs(os.path.dirname(OUTPUT_MD), exist_ok=True)
    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write(md_text)

    file_size = os.path.getsize(OUTPUT_MD)
    line_count = md_text.count("\n") + 1

    print(f"\n{'=' * 60}")
    print("TAMAMLANDI!")
    print(f"  Dosya: {OUTPUT_MD}")
    print(f"  Boyut: {file_size:,} bayt")
    print(f"  Satır: {line_count:,}")
    print(f"{'=' * 60}")

    # Doğrulama: Bölüm başlıklarını kontrol et
    print("\nBölüm başlıkları kontrolü:")
    for line in reduced:
        if line.startswith("# ") and not line.startswith("# PYTHON"):
            print(f"  {line}")


if __name__ == "__main__":
    main()
