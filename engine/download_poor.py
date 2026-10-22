# -*- coding: utf-8 -*-
import urllib.request
from PIL import Image

url = "https://aka.doubaocdn.com/s/oUxWeTThHM"
tmp = r"E:\doubao\摄影\PhotoJudge\engine\poor-source.jpg"
out = r"E:\doubao\摄影\PhotoJudge\engine\poor-scaled.jpg"

urllib.request.urlretrieve(url, tmp)
im = Image.open(tmp)
print("source size:", im.size)
im.thumbnail((2000, 2000))
im.save(out, "JPEG", quality=90)
print("saved:", out, im.size)
