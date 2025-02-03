# ai18n - AI-Powered i18n Translation Tool 🌍  
**Effortless file translations using OpenAI's API**  

`ai18n.py` is a command-line tool designed for **translating text and JSON files** into multiple languages using OpenAI's AI models. It supports **automatic language detection**, **large file handling**, and **configuration via `.env` or `config.yaml`**.

---

## ✨ Features  
✅ **Supports multiple languages** (English, French, Spanish, Catalan, Euskera)  
✅ **Automatic source language detection** (if not specified)  
✅ **Handles large JSON files** with **chunking** to prevent API limits  
✅ **Secure API key management** using `.env` or `config.yaml`  
✅ **Simple command-line interface (CLI)** for easy translations  
✅ **Maintains JSON structure while translating text**  

---

## 📥 Installation  

### 1️⃣ Clone the Repository  
```sh
git clone git@github.com:thdelmas/ai18n.git
cd ai18n
```

### 2️⃣ Install Dependencies  
```sh
pip install -r requirements.txt
```

### 3️⃣ Set Up API Key  
To authenticate with OpenAI, you need an API key. You can store it securely in either **`.env`** or **`config.yaml`**.

#### **Option 1: Using a `.env` File (Recommended)**
Create a `.env` file in the `ai18n` directory:
```sh
OPENAI_API_KEY=your_api_key_here
```
#### **Option 2: Using `config.yaml`**
Create a `config.yaml` file in the `ai18n` directory:
```yaml
OPENAI_API_KEY: your_api_key_here
```

---

## 🎯 Usage  

### **1️⃣ Translate a Text File**
```sh
python3 ai18n.py input.txt output.txt --target_language fr
```
This translates `input.txt` into **French** and saves it as `output.txt`.

### **2️⃣ Translate a JSON File (Handles Large JSON Automatically)**
```sh
python3 ai18n.py data.json translated.json --target_language es --chunk_size 500
```
This translates `data.json` into **Spanish**, processing **500 items at a time** to avoid API limits.

### **3️⃣ Auto-Detect Source Language**
If you **omit `--source_language`**, the script will attempt to **automatically detect** the language.

Example:
```sh
python3 ai18n.py input.txt output.txt --target_language fr
```
If `input.txt` is in **English**, the tool will detect and translate it to **French**.

### **4️⃣ Use a Custom Configuration File**
If using a different config file, specify it with:
```sh
python3 ai18n.py input.txt output.txt --target_language fr --config my_config.yaml
```

---

## ⚙️ Configuration  

### **📌 `.env` File (Preferred)**
The script will **automatically load** environment variables from `.env`.
```sh
OPENAI_API_KEY=your_api_key_here
```

### **📌 `config.yaml` File (Alternative)**
If `.env` is not used, the script will check for `config.yaml`:
```yaml
OPENAI_API_KEY: your_api_key_here
```
If using a **custom config file**, pass it with `--config my_config.yaml`.

---

## 🚀 Advanced Usage  

### **🌟 Supported Languages**
The following language codes are supported:  
| Code | Language  |
|------|----------|
| `en` | English  |
| `fr` | French   |
| `es` | Spanish  |
| `ca` | Catalan  |
| `eu` | Euskera  |
| `pt` | Portuguese |

Example:
```sh
python3 ai18n.py input.txt output.txt --target_language es
```
(Translates to **Spanish**)

### **⚡ Processing Large Files**
For **large JSON files**, adjust the chunk size:
```sh
python3 ai18n.py large.json output.json --target_language fr --chunk_size 500
```
This processes **500 items at a time**, preventing **API timeouts**.

---

## 🛠 Development & Contributions  
We welcome contributions! If you'd like to improve `ai18n`:

1. **Fork the repository**
2. **Create a new branch**
3. **Submit a pull request (PR)** with your changes.

### **💡 Planned Features**
✅ **Parallel processing for faster translations**  
✅ **Streaming large file translations**  
🟡 **Support for more structured file formats (YAML, XML, CSV, etc.)**  
🟡 **Add caching to avoid redundant API calls**  

---

## 📄 License  
This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute! 🚀  

---
🚀 **Happy Translating!** 🚀  
