#!/usr/bin/env python3
"""
Makine Öğrenmesi PDF -> Markdown Dönüştürücü (Temiz ve Eksiksiz)

Adım 1: makine_ogrenmesi.pdf dosyasından PyPDF2 ile metin çıkarır.
Adım 2: Çıkarılan metni temizler ve markdown formatına dönüştürür.
Adım 3: /Users/zuber/INP214/docs/makine_ogrenmesi.md dosyasını oluşturur.

Temizlik işlemleri:
- "=== SAYFA X ===" satırları kaldırılır
- "6.05.2024 13:55" header satırları kaldırılır
- "Ders : MAKİNE ÖĞRENMESİ - eKtap" satırları kaldırılır
- "about:blank X/277" prefix'leri kaldırılır (sonrasındaki içerik korunur)
- Bölüm başlıkları markdown heading'e dönüştürülür
- Ardışık boş satırlar azaltılır

Kullanım:
    python makine_ogrenmesi_extractor.py
"""

import re
import os

try:
    import PyPDF2
except ImportError:
    print("HATA: PyPDF2 kütüphanesi gerekli. Yüklemek için: pip install PyPDF2")
    exit(1)


BASE_DIR = "/Users/zuber/INP214"
PDF_PATH = os.path.join(BASE_DIR, "docs", "makine_ogrenmesi.pdf")
EXTRACTED_TEXT = "/tmp/makine_ogrenmesi_extracted.txt"
OUTPUT_MD = os.path.join(BASE_DIR, "docs", "makine_ogrenmesi.md")


def extract_pdf_to_text(pdf_path, output_path):
    """PDF dosyasından metin çıkar ve geçici dosyaya yaz"""
    reader = PyPDF2.PdfReader(pdf_path)
    total_pages = len(reader.pages)
    print(f"  -> {total_pages} sayfa bulundu")

    with open(output_path, "w", encoding="utf-8") as f:
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            f.write(f"=== SAYFA {i + 1} ===\n")
            if text:
                # Null byte'ları temizle (PDF extraction artifact)
                text = text.replace("\x00", "")
                f.write(text + "\n")
            f.write("\n")

    size = os.path.getsize(output_path)
    print(f"  -> {size:,} bayt metin çıkarıldı -> {output_path}")
    return total_pages


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

        # "6.05.2024 13:55" ile başlayan/içeren header satırlarını atla
        if "6.05.2024 13:55" in line:
            continue

        # "Ders : MAKİNE ÖĞRENMESİ" satırlarını atla
        if "Ders : MAKİNE ÖĞRENME" in line:
            continue

        # about:blank X/277 satırlarını tamamen atla
        if re.match(r"^about:blank\s+\d+/277", line.strip()):
            continue

        # İçindekiler sayfasını atla
        if line.strip() == "İÇİNDEKİLER":
            in_toc = True
            continue

        if in_toc:
            continue

        # Ana bölüm başlıklarını tespit et (standalone satırlarda)
        # Tam eşleşme: sadece kitabın 10 bölüm başlığı
        chapter_patterns = [
            r"^1\.\s+Yapay Zekâ,?\s*Mak",
            r"^2\.\s+Mak\w*\s+Öğr\s*enmes\s*Sür",
            r"^3\.\s+Python\s+le\s+Ver\s+Görselleşt",
            r"^4\.\s+Python\s+le\s+Ver\s+Ön",
            r"^5\.\s+K-ortalamalar",
            r"^6\.\s+Bast\s+ve\s+Çoklu",
            r"^7\.\s+K-en\s+Yakın",
            r"^8\.\s+Naıve\s+Bayes",
            r"^9\.\s+Karar\s+Ağaçları",
            r"^10\.\s+Yapay\s+S\w*r\s+Ağları",
        ]
        is_chapter = False
        for cp in chapter_patterns:
            if re.match(cp, line.strip()):
                is_chapter = True
                break
        if is_chapter:
            cleaned.append(f"§HEADING§{line.strip()}")
            continue

        cleaned.append(line)

    return cleaned


def format_section_headings(lines):
    """Bölüm başlıklarını markdown heading formatına dönüştür"""
    result = []

    # Makine Öğrenmesi kitabına özgü başlık düzeltmeleri
    heading_fixes = {
        "Makne Öğr enmes": "Makine Öğrenmesi",
        "İlşkl Temel Kavramla": "İlişkili Temel Kavramlar",
        "Makne Öğr enmes Sür ec": "Makine Öğrenmesi Süreci",
        "Python le Ver Görselleştrme": "Python ile Veri Görselleştirme",
        "Python le Ver Ön-şleme": "Python ile Veri Ön-İşleme",
        "K-ortalamalar  Algortması": "K-Ortalamalar Algoritması",
        "Bast ve Çoklu Doğrusal Regr esyon Analz": "Basit ve Çoklu Doğrusal Regresyon Analizi",
        "K-en Yakın Komşu Algortması": "K-En Yakın Komşu Algoritması",
        "Naıve Bayes Algortması": "Naive Bayes Algoritması",
        "Karar  Ağaçları": "Karar Ağaçları",
        "Yapay Snr  Ağları": "Yapay Sinir Ağları",
    }

    for i, line in enumerate(lines):
        stripped = line.strip()

        # §HEADING§ ile işaretlenmiş ana bölüm başlıkları
        if stripped.startswith("§HEADING§"):
            heading_text = stripped.replace("§HEADING§", "").strip()
            # Bilinen hataları düzelt
            for wrong, correct in heading_fixes.items():
                heading_text = heading_text.replace(wrong, correct)
            result.append("")
            result.append(f"# {heading_text}")
            result.append("")
            continue

        # Alt bölüm başlıkları: X.Y.Z.
        sub_sub_match = re.match(r"^(\d+\.\d+\.\d+\.)\s+(.*)", stripped)
        if sub_sub_match and len(stripped) < 120:
            num = sub_sub_match.group(1).rstrip(".")
            title = sub_sub_match.group(2).strip()
            if title and len(title) > 2:
                result.append("")
                result.append(f"### {num}. {title}")
                result.append("")
                continue

        # Alt bölüm başlıkları: X.Y.
        sub_match = re.match(r"^(\d+\.\d+\.)\s+(.*)", stripped)
        if sub_match and len(stripped) < 120:
            num = sub_match.group(1).rstrip(".")
            title = sub_match.group(2).strip()
            if title and len(title) > 2:
                result.append("")
                result.append(f"## {num}. {title}")
                result.append("")
                continue

        # Önemli alt başlıklar (bold yapılacak)
        bold_headings = [
            "Kazanımlar", "Brlkte Düşünelm", "Birlikte Düşünelim",
            "Başlamadan Önce", "Bölüm Özet", "Bölüm Özeti",
            "Kaynakça", "Ünte Soruları", "Ünite Soruları",
            "Özlü Söz",
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
    header = """# MAKİNE ÖĞRENMESİ - eKitap

**Doç. Dr. Elif Kartal, Prof. Dr. Mehmet Erdal Balaban**
İstanbul Üniversitesi - Açık ve Uzaktan Eğitim Fakültesi

---

## İÇİNDEKİLER

1. Yapay Zekâ, Makine Öğrenmesi ve İlişkili Temel Kavramlar
2. Makine Öğrenmesi Süreci
3. Python ile Veri Görselleştirme
4. Python ile Veri Ön-İşleme
5. K-Ortalamalar Algoritması
6. Basit ve Çoklu Doğrusal Regresyon Analizi
7. K-En Yakın Komşu Algoritması
8. Naive Bayes Algoritması
9. Karar Ağaçları
10. Yapay Sinir Ağları

---

"""
    body = "\n".join(lines)
    return header + body


def main():
    print("=" * 60)
    print("MAKİNE ÖĞRENMESİ PDF -> MD (Temiz ve Eksiksiz)")
    print("=" * 60)

    # 1. PDF'den metin çıkar
    if not os.path.exists(PDF_PATH):
        print(f"HATA: {PDF_PATH} bulunamadı!")
        return

    print(f"\n[1/5] PDF'den metin çıkarılıyor: {PDF_PATH}")
    extract_pdf_to_text(PDF_PATH, EXTRACTED_TEXT)

    # 2. Ham metni oku
    print(f"[2/5] Okunuyor: {EXTRACTED_TEXT}")
    with open(EXTRACTED_TEXT, "r", encoding="utf-8") as f:
        raw_lines = f.readlines()
    print(f"  -> {len(raw_lines)} satır okundu")

    # 3. Temizle
    print("[3/5] Sayfa başlıkları ve gereksiz satırlar temizleniyor...")
    cleaned = clean_extracted_text(raw_lines)
    print(f"  -> {len(cleaned)} satır kaldı")

    # 4. Bölüm başlıklarını formatla
    print("[4/5] Bölüm başlıkları markdown formatına dönüştürülüyor...")
    formatted = format_section_headings(cleaned)

    # 5. Boş satırları azalt
    reduced = reduce_blank_lines(formatted)
    print(f"  -> {len(reduced)} satır (son)")

    # 6. Markdown oluştur ve yaz
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
        if line.startswith("# ") and not line.startswith("# MAKİNE"):
            print(f"  {line}")


if __name__ == "__main__":
    main()
