import os
import subprocess
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_ollama(prompt):
    system_instruction = (
        "Kamu adalah Stark, asisten AI yang membantu pengguna dengan berbagai pertanyaan dan tugas. "
        "Jawabanmu harus jelas, ringkas, dan informatif. Jika pertanyaannya tidak jelas, minta klarifikasi. "
        "Jangan membuat asumsi atau memberikan informasi yang tidak akurat. "
        "Berikan jawaban yang relevan dan bermanfaat berdasarkan pertanyaan pengguna. "
        "Gunakan bahasa yang sopan dan profesional."
    )
    
    payload = {
        "model": "qwen2.5:1.5b",
        "prompt": f"System: {system_instruction}\nUser: {prompt}\nStark:",
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json()['response']
    except Exception as e:
        return f"Gagal terhubung ke Ollama: {e}"

def execute_system_command(text):
    text_lower = text.lower()
    
    if "buka browser" in text_lower:
        subprocess.Popen(["firefox"])
        return "Browser telah dibuka."
    elif "buka terminal" in text_lower:
        subprocess.Popen(["kitty"])
        return "Terminal telah dibuka."
    elif "cek sistem" in text_lower or "monitor" in text_lower:
        subprocess.Popen(["kitty", "-e", "btop"])
        return "Membuka monitor sistem."
    
    return ask_ollama(text)

if __name__ == "__main__":
    print("STARK Online. Ketik 'exit' atau 'quit' untuk keluar.\n")
    while True:
        user_input = input("Tanya STARK: ")
        
        if user_input.lower().strip() in ["exit", "quit", "keluar"]:
            print("STARK: Sampai jumpa!")
            break
            
        if not user_input.strip():
            continue
            
        jawaban = execute_system_command(user_input)
        print(f"STARK: {jawaban}\n")
        
        
        # sudo systemctl start ollama
        # ollama run qwen2.5:1.5bollama run qwen2.5:1.5b
        # /bye