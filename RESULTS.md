# API lab results

## Part 0

- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token:
- Step 0.4, the name of your pizza:
- Step 0.12, results of the three runs without a session (optional):
- Step 0.16, blocks of "how many of the three tools are excluded":

## Defect report

Title:
Request:
Expected result:
Actual result:
Severity:

## Part A

Step A4, status codes when the other user reads, changes and deletes:

## Part B

1.
2.
3.
4.
5.
6.
7.
8.

````[cite: 43]

---

### Step 0.1: A first request with curl

1. พิมพ์คำสั่งใน Terminal[cite: 30]:
   ```powershell
   curl.exe https://quickpizza.grafana.com/api/names
   ```[cite: 30]
2. นับจำนวนชื่อพิซซ่าที่ได้ใน JSON (มีทั้งหมด 10 ชื่อ)[cite: 30] นำตัวเลขไปเติมใน `RESULTS.md` บรรทัด Step 0.1: `10`[cite: 30, 43]
3. รันคำสั่ง Commit & Push[cite: 29]:
   ```powershell
   git add .
   git commit -m "Step 0.1"
   git push
   ```[cite: 29]

---

### Step 0.3: A request that needs a token

1. พิมพ์คำสั่งยิงแบบไม่มี Token ใน Terminal[cite: 31]:
   ```powershell
   curl.exe -i https://quickpizza.grafana.com/api/tools
   ```[cite: 31]
2. ดู Status Code ในคำตอบ (`401`)[cite: 31] นำไปเติมใน `RESULTS.md` บรรทัด Step 0.3: `401`[cite: 31, 43]
3. รันคำสั่ง Commit & Push[cite: 29]:
   ```powershell
   git add .
   git commit -m "Step 0.3"
   git push
   ```[cite: 29]

---

### Step 0.4: Sending data with POST

1. พิมพ์คำสั่งยิง POST ขอดูพิซซ่ามังสวิรัติ[cite: 31]:
   ```powershell
   curl.exe -H "@auth.txt" -d "@veg.json" https://quickpizza.grafana.com/api/pizza
   ```[cite: 31]
2. ดูชื่อพิซซ่าที่สุ่มได้ใน JSON (เช่น `Americana`)[cite: 31] นำไปเติมใน `RESULTS.md` บรรทัด Step 0.4[cite: 31, 43]
3. รันคำสั่ง Commit & Push[cite: 29]:
   ```powershell
   git add .
   git commit -m "Step 0.4"
   git push
   ```[cite: 29]

---

### Step 0.6: Your first test

1. สร้างไฟล์ **`test_names.py`** แล้วใส่โค้ดนี้[cite: 33]:
   ```python
   import requests
   SITE = "https://quickpizza.grafana.com"

   # The list of pizza names answers 200 and holds Margherita.
   def test_names_are_listed():
       res = requests.get(SITE + "/api/names")
       assert res.status_code == 200
       assert "Margherita" in res.json()["names"]
   ```[cite: 33]
2. พิมพ์รันใน Terminal เพื่อเช็กว่าผ่าน (`1 passed`)[cite: 33]:
   ```powershell
   pytest -v
   ```[cite: 33]
3. รันคำสั่ง Commit & Push[cite: 29]:
   ```powershell
   git add .
   git commit -m "Step 0.6"
   git push
   ```[cite: 29]

---

### Step 0.7: A test with a token

1. สร้างไฟล์ **`test_tools.py`** แล้วใส่โค้ดนี้[cite: 33]:
   ```python
   import requests
   SITE = "https://quickpizza.grafana.com"
   AUTH = {"Authorization": "token abcdef0123456789"}

   # The list of tools answers 200 and names the three tools.
   def test_tools_are_listed():
       res = requests.get(SITE + "/api/tools", headers=AUTH)
       assert res.status_code == 200
       assert res.json() == {"tools": ["Knife", "Pizza cutter", "Scissors"]}
   ```[cite: 33]
2. พิมพ์รันเช็กผล (`2 passed`)[cite: 33]:
   ```powershell
   pytest -v
   ```[cite: 33]
3. รันคำสั่ง Commit & Push[cite: 29]:
   ```powershell
   git add .
   git commit -m "Step 0.7"
   git push
   ```[cite: 29]

---

ทำ 5 ขั้นตอนนี้เรียบร้อยแล้ว พิมพ์บอกได้เลยครับ เดี๋ยวพาทำ Step 0.8 ถึง 0.16 ต่อทันที!
````
