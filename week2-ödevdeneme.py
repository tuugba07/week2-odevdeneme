class Node():
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, text: str, value: int):
        self.root = Node(text, value)

    def add_node(self, text: str, value: int):
        new_node = Node(text, value)
        current_node = self.root
        
        while True:
            if value > current_node.value:
                if current_node.right is None:
                    current_node.right = new_node
                    break # Ekleme yapınca döngüyü bitir
                current_node = current_node.right
            elif value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node # Burada sağ yazmıştın, sola çevirdik
                    break
                current_node = current_node.left
            else:
                print(f"Hata: {value} değeri zaten mevcut.")
                break

    def search_node(self, value):
        current_node = self.root
        while current_node:
            if value == current_node.value:
                return current_node.key
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return "Hata: Bulunamadı"

    def size(self):
        return self._size(self.root)

    def _size(self, current_node):
        if current_node is None:
            return 0
        return 1 + self._size(current_node.left) + self._size(current_node.right)

    def height(self):
        return self._height(self.root)

    def _height(self, current_node):
        if current_node is None:
            return -1 # Genelde boş ağacın boyu -1 veya 0 kabul edilir
        return 1 + max(self._height(current_node.left), self._height(current_node.right))

# Test Kısmı
my_tree = BinaryTree("Mehmet", 32)
my_tree.add_node("Sabriye", 9)
my_tree.add_node("Emirhan", 31)
my_tree.add_node("Ata", 41)
my_tree.add_node("Burdur", 15)

print(f"Aranan Değer (41): {my_tree.search_node(41)}")
print(f"Ağaç Eleman Sayısı: {my_tree.size()}")
print(f"Ağaç Yüksekliği: {my_tree.height()}")
#deneme
