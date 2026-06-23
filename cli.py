import sys 
import os 
from lz77 import compress, decompress 
 
MAGIC = b"BZP2" 
 
def pack_folder(folder, out_file): 
    files = [] 
    for root, _, names in os.walk(folder): 
        for n in names: 
            path = os.path.join(root, n) 
            rel = os.path.relpath(path, folder) 
            data = open(path,"rb").read() 
            comp = compress(data) 
            files.append((rel, comp)) 
 
    f = open(out_file,"wb") 
    f.write(MAGIC) 
    f.write(len(files).to_bytes(4,"big")) 
 
    for name, data in files: 
        nb = name.encode() 
        f.write(len(nb).to_bytes(2,"big")) 
        f.write(nb) 
 
        raw = bytearray() 
        for t in data: 
            if t[0]=="L": 
                raw += b"L"+bytes([t[1]]) 
            else: 
                raw += b"M"+bytes([t[1],t[2]]) 
 
        f.write(len(raw).to_bytes(4,"big")) 
        f.write(raw) 
 
def unpack_folder(inp,out): 
    data = open(inp,"rb").read() 
    i = 4 
    count = int.from_bytes(data[i:i+4],"big") 
    i += 4 
 
    for _ in range(count): 
        nl = int.from_bytes(data[i:i+2],"big") 
        i += 2 
        name = data[i:i+nl].decode() 
        i += nl 
        size = int.from_bytes(data[i:i+4],"big") 
        i += 4 
        raw = data[i:i+size] 
        i += size 
 
        tokens = [] 
        j = 0 
        while j < len(raw): 
            if raw[j]==76: 
                tokens.append(("L",raw[j+1])) 
                j += 2 
            else: 
                tokens.append(("M",raw[j+1],raw[j+2])) 
                j += 3 
 
        res = decompress(tokens) 
        full = os.path.join(out,name) 
        os.makedirs(os.path.dirname(full),exist_ok=True) 
        open(full,"wb").write(res) 
 
if sys.argv[1]=="a": 
    pack_folder(sys.argv[2],sys.argv[3]) 
elif sys.argv[1]=="x": 
    unpack_folder(sys.argv[2],sys.argv[3]) 
