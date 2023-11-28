import chardet

file_path = "C:/Users/elift/Desktop/test/rag_instruct_benchmark_tester.csv"

# Dosyanın karakter setini belirle
with open(file_path, 'rb') as f:
    result = chardet.detect(f.read())

# Dosyayı belirlenen karakter setiyle aç
with open(file_path, 'r', encoding=result['encoding']) as f:
    file_content = f.read()

# Dosya içeriğini kullanmaya devam edebilirsiniz.
print(file_content)
