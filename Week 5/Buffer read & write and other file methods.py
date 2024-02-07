# for large files
import io

with open ("test1.txt",'wb') as f:
    file = io.BufferedWriter(f)
    file.write(b"Data science is the study of data to extract meaningful insights for business. It is a multidisciplinary approach that combines principles and practices from the fields mathematics, statistics, artificial intelligence, and computer engineering to analyze large amounts of data.")
    file.write(b"My name is Shally")
    file.flush()


with open ("test1.txt",'rb') as f:
    file = io.BufferedReader(f)
    data = file.read(10000)
    print(data)
