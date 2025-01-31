class MyDictionary:
    def __init__(self):
        self.entries = {}

    def add_entry(self, key, value):
        self.entries[key] = value

    def remove_entry(self, key):
        if key in self.entries:
            del self.entries[key]
        else:
            print(f"Key '{key}' tidak ditemukan dalam kamus.")

    def get_value(self, key):
        if key in self.entries:
            return self.entries[key]
        else:
            return None

    def display(self):
        print("Kamus buah dan sayuran:")
        for key, value in self.entries.items():
            print(f"{key}: {value}")

# Membuat objek MyDictionary
my_dict = MyDictionary()

# Menambahkan entri ke dictionary
my_dict.add_entry("apel", " buah")
my_dict.add_entry("pisang", "buah")
my_dict.add_entry("melon", "buah")
my_dict.add_entry("timun", "sayuran")
my_dict.add_entry("wortel", "sayuran")

# Menampilkan entri dictionary
my_dict.display()

# Menghapus entri dari dictionary
my_dict.remove_entry("pisang")

# Menampilkan entri dictionary setelah penghapusan
my_dict.display()

# Mendapatkan nilai berdasarkan kunci
print("Value for 'apel':", my_dict.get_value("apel"))
print("Value for 'pisang':", my_dict.get_value("pisang"))