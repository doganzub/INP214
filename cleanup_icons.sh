#!/bin/bash
# INP214 - Icon ve gereksiz dosya temizleme scripti
# .DS_Store, icon dosyalari ve diger gereksiz dosyalari siler

echo "Temizlik basliyor..."

# .DS_Store dosyalarini sil
find . -name ".DS_Store" -type f -delete -print
echo "-> .DS_Store dosyalari silindi"

# Icon dosyalarini sil (varsa)
find . -name "*.ico" -type f -delete -print
find . -name "Icon?" -type f -delete -print
find . -name "icon*" -type f -not -name "*.py" -not -name "*.sh" -delete -print
echo "-> Icon dosyalari silindi"

# Thumbs.db (Windows) dosyalarini sil (varsa)
find . -name "Thumbs.db" -type f -delete -print
find . -name "desktop.ini" -type f -delete -print
echo "-> Windows sistem dosyalari silindi"

echo "Temizlik tamamlandi!"
