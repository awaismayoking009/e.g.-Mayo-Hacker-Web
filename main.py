def send_data(self, instance):
    token = "8275595420:AAEbGQoAXyUQ_yVLSsli7zsd0Cy4DTS9ajA"
    chat_id = "6523586283"
    message = "ہیلو! یہ میسج اینڈرائیڈ ایپ سے بھیجا گیا ہے 📱"
    
    # ٹیلی گرام API کا یو آر ایل
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    # ڈیٹا جو بھیجنا ہے
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    
    # میسج بھیجنے کی کوشش
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            self.btn.text = "میسج کامیابی سے بھیج دیا گیا! ✅"
        else:
            self.btn.text = "کچھ غلط ہو گیا ❌"
    except:
        self.btn.text = "انٹرنیٹ کا مسئلہ ہے 🌐"
