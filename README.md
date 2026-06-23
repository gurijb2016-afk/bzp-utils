
# bzp utils

A lightweight Python-based compression and archive tool using a custom LZ77 implementation.

---

## 🚀 Features

- LZ77 compression algorithm
- File + folder support (PRO version)
- Custom `.bzp` archive format
- Simple CLI tool (`bzp a / x`)
- Windows install support (`install.bat`)

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourname/bzp-utils.git
cd bzp-utils
Windows install:
install.bat

Then restart terminal.

📦 Usage
Compress file or folder:
bzp a input_folder output.bzp
Extract archive:
bzp x output.bzp output_folder
🧠 How it works

bzp utils uses a simplified LZ77 algorithm:

Detects repeating patterns in files
Replaces them with distance/length references
Stores data in a custom .bzp binary format
⚠️ Notes
This is a learning / experimental project
Not optimized like ZIP or 7zip
Focused on simplicity and understanding compression
📁 Project structure
bzp-utils/
 ├── cli.py
 ├── lz77.py
 ├── install.bat
 ├── uninstall.bat
 ├── README.md
🔥 Future ideas
Huffman coding integration
Better compression ratio
GUI interface
Cross-platform installer
Multi-threaded compression
