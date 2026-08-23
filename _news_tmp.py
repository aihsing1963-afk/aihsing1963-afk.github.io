import sys, os, re
sys.path.insert(0, os.path.expanduser("~/.hermes/scripts/finance"))
import finance_common as fc

now = fc.taipei_now()
print("整理時間（台灣）：", now.strftime("%Y-%m-%d %H:%M"))
print()
print("===== 台股 / 台灣財經 =====")
for i, t in enumerate(fc.news("台股 OR 台積電 OR 加權指數 OR 電子股 OR 外資", n=8), 1):
    t2 = re.sub(r"\s*-\s*[^-]+$", "", t)
    print(f"{i}. {t2}")
print()
print("===== 國際財經 =====")
for i, t in enumerate(fc.news("國際財經 OR 全球股市 OR 聯準會 OR 油價 OR 金價", n=8), 1):
    t2 = re.sub(r"\s*-\s*[^-]+$", "", t)
    print(f"{i}. {t2}")
