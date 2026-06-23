📄 README.md (bzipmini)
# bzipmini

A simple Python-based LZ77 + folder archiver.

This project is a lightweight experimental compression tool similar to ZIP, but custom-built for learning purposes.

---

## 🚀 Features

- LZ77 compression algorithm
- File + folder support (PRO version)
- Custom `.bzp` archive format
- Simple CLI usage (`bzp a / x`)
- Windows install support (install.bat)

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourname/bzipmini.git
cd bzipmini

Run installer (Windows):

install.bat

After installation, restart terminal.

📦 Usage
Compress file or folder:
bzp a input_folder output.bzp
Extract archive:
bzp x output.bzp output_folder
🧠 How it works

bzipmini uses a simplified LZ77 algorithm:

Searches repeated patterns in data
Replaces them with (distance, length) references
Stores raw + compressed tokens in .bzp format
⚠️ Notes
This is a learning project, not production-grade compression
Compression ratio is lower than ZIP / 7zip
Best used for education and experimentation
📁 Project Structure
bzipmini/
 ├── cli.py
 ├── lz77.py
 ├── install.bat
 ├── uninstall.bat
 └── README.md
🔥 Future ideas
Huffman encoding support
Better compression ratio
GUI version
Cross-platform installer
Faster LZ77 implementation
