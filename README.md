# 📦 FTP SENDER — Python CLI FTP Client

A clean and modular FTP client built in Python.  
This tool allows you to browse, upload, download, delete, and rename files on a remote FTP server through an interactive command‑line interface.

---

##  Features

### ✔ Connect to FTP servers
- IPv4 validation using regex  
- Custom port support  
- Anonymous or credential login  

### ✔ Browse remote directories
- Navigate folders  
- List files and directories  
- Interactive file selection  

### ✔ Upload files
- Local folder scanning  
- File selection menu  
- Upload progress bar (chunk‑based)  
- Supports large files (128 KB chunks)

### ✔ Download files
- Interactive file selection  
- Download progress bar  
- Automatic `downloads/` folder creation  

### ✔ Delete files
- Confirmation prompt  
- Safe and clear error handling  

### ✔ Rename files
- Keeps original extension  
- Shows old and new paths  
- Confirmation before renaming  

### ✔ Utility functions
- Show current remote path  
- Get file size  
- Parse FTP LIST output into structured items  

---

##  Project Structure

```
FTP-SENDER/
│
├── CORE/
│   ├── clients.py        # FTPClient class (upload, download, delete, rename…)
│   ├── browsing.py       # Directory browsing + file selection menus
│   ├── helper.py         # Folder scanner + loading bar animation
│
├── main.py               # Main CLI program
├── README.md             # Project documentation
```

---

##  Usage

### 1. Run the program

```bash
python main.py
```

### 2. Enter connection details
- FTP host (validated IPv4)
- Port
- Username (optional)
- Password (optional)

### 3. Use the interactive menu

```
=== FTP MAIN MENU ===
1. Browse server
2. Download file
3. Upload file
4. Delete file
5. Rename file
6. Show current path
0. Exit
```

---

## 📡 Progress Bars

Uploads and downloads use Python’s `storbinary` and `retrbinary` with a custom callback that:

- counts bytes  
- updates progress  
- draws a loading bar  
- shows percentage  

This makes the CLI feel like a real FTP client.

---

##  Requirements

- Python 3.8+
- Standard library only (`ftplib`, `os`, `re`)

No external dependencies.

---

##  Why This Project Matters

This project demonstrates real backend engineering skills:

- protocol handling  
- chunked file transfer  
- callback‑based progress tracking  
- modular architecture  
- clean CLI UX  
- safe destructive operations  
- directory parsing  

A strong portfolio piece showing system‑level backend development.

---

##  Future Improvements

- Upload/download speed (MB/s)  
- ETA (time remaining)  
- Directory upload/download  
- Config file for saved servers  
- Colorized terminal output  
- Logging system  

