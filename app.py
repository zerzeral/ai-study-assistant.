from flask import Flask, render_template, request, jsonify

app = Flask(name)

@app.get("/")
def home():
return render_template("index.html")

@app.post("/analisis")
def analisis():
data = request.get_json(silent=True) or {}
soal = str(data.get("soal", "")).strip()

if not soal:
    return jsonify({"error": "Soal belum diisi."}), 400

hasil = (
    "MODE DEMO — ini contoh respons, bukan jawaban AI sungguhan.\n\n"
    f"Soal kamu: {soal}\n\n"
    "Cara belajar:\n"
    "1. Baca soal dan tentukan apa yang ditanyakan.\n"
    "2. Catat informasi penting.\n"
    "3. Pilih konsep atau rumus yang sesuai.\n"
    "4. Kerjakan langkah demi langkah dan periksa hasilnya.\n\n"
    "Mode demo belum menjawab soal secara otomatis."
)

return jsonify({"hasil": hasil})

if name == "main":
app.run(host="0.0.0.0", port=5000)
