from collections import defaultdict

# ----------------------------
# Sosyal Ağ Sınıfı
# ----------------------------
# Kullanıcıları ve arkadaşlık ilişkilerini tutan sınıf
class SocialNetwork:
    def __init__(self):
        self.graph = defaultdict(list)  # arkadaşlık ilişkilerini tutan grafik (adjacency list)
        self.users = set()  # tüm kullanıcıları tutan küme

    def add_user(self, user_id):
        self.users.add(user_id)  # kullanıcı ekle

    def add_friendship(self, u1, u2):
        # iki yönlü arkadaşlık ilişkisi ekle
        self.graph[u1].append(u2)
        self.graph[u2].append(u1)

# ----------------------------
# Dosyadan veri okuma fonksiyonu
# ----------------------------
def load_data(filename):
    sn = SocialNetwork()
    with open(filename) as f:
        for line in f:
            parts = line.strip().split()
            if parts[0] == "USER":
                sn.add_user(parts[1])  # kullanıcı satırıysa kullanıcı ekle
            elif parts[0] == "FRIEND":
                sn.add_friendship(parts[1], parts[2])  # arkadaşlık satırıysa ilişki kur
    return sn

# ----------------------------
# DFS ile k mesafedeki arkadaşları bulma
# ----------------------------
def dfs_friends_at_distance_k(graph, start, k):
    result = []  # sonuç listesi
    visited = set()  # ziyaret edilen düğümler

    # iç içe DFS fonksiyonu
    def dfs(node, depth):
        if depth > k:
            return
        visited.add(node)
        if depth == k:
            result.append(node)  # istenen mesafedeyse ekle
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, depth + 1)

    dfs(start, 0)  # DFS başlat
    return result

# ----------------------------
# Ortak arkadaşları bulma
# ----------------------------
def common_friends(graph, user1, user2):
    # iki kullanıcının arkadaş kümesinin kesişimini al
    return list(set(graph[user1]) & set(graph[user2]))

# ----------------------------
# Toplulukları (bağlı bileşenleri) bulma
# ----------------------------
def find_communities(graph, users):
    visited = set()
    communities = []

    def dfs(node, community):
        visited.add(node)
        community.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, community)

    for user in users:
        if user not in visited:
            community = []
            dfs(user, community)  # her bileşeni ayrı ayrı bul
            communities.append(community)

    return communities

# ----------------------------
# Bir kullanıcının etki alanını hesaplama
# ----------------------------
def influence_domain(graph, user):
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(user)  # DFS başlat
    return len(visited) - 1  # kendisi hariç bağlı olan kişi sayısı

# ----------------------------
# Kırmızı-Siyah Ağaç (Red-Black Tree) Simülasyonu
# ----------------------------
class RBTreeNode:
    def __init__(self, key, color='red'):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

# Simülasyon amaçlı kırmızı-siyah ağaç sınıfı
class RedBlackTree:
    def __init__(self):
        self.nil = RBTreeNode(None, color='black')  # sentinel node
        self.root = self.nil

    def insert(self, key):
        # Gerçek RBTree algoritması uygulanmadı, sadece simülasyon
        print(f"[Simülasyon] {key} kullanıcısı RBTree'ye eklendi.")

    def search(self, key):
        # Gerçek arama yapılmadan çıktıyı simüle eder
        print(f"[Simülasyon] {key} kullanıcısı RBTree içinde aranıyor.")
        return True

# ----------------------------
# Ana test fonksiyonu (örnek senaryo)
# ----------------------------
if __name__ == '__main__':
    sn = load_data("veriseti.txt")  # dosyayı yükle

    print("Kullanıcılar:", sn.users)
    print("Arkadaşlıklar:", dict(sn.graph))

    print("\n2 mesafedeki arkadaşlar (101):", dfs_friends_at_distance_k(sn.graph, '101', 2))
    print("Ortak arkadaşlar (101, 102):", common_friends(sn.graph, '101', '102'))
    print("Topluluklar:", find_communities(sn.graph, sn.users))
    print("Etki alanı (104):", influence_domain(sn.graph, '104'))

    # Red-Black Tree Kullanımı
    rbtree = RedBlackTree()
    for user in sn.users:
        rbtree.insert(user)
    rbtree.search('104')
