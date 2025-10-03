import sys
print("Python version:", sys.version)

# Test import trực tiếp từ thư mục PSSE
import os
os.chdir(r"C:\Program Files\PTI\PSSE36\36.1\PSSPY311")

try:
    import psspy
    print("SUCCESS: psspy imported!")
except Exception as e:
    print("ERROR:", e)
    print("Try different Python version (3.8 instead of 3.7)")