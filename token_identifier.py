class TokenIdentifier:
    def __init__(self):
        # Mendefinisikan state penerimaan untuk setiap kelompok kata
        self.valid_tokens = {
            "aku": "S", "anda": "S", "mereka": "S", "kami": "S", "engkau": "S",
            "membaca": "P", "menulis": "P", "menggambar": "P", "menari": "P", "berbicara": "P",
            "buku": "O", "pena": "O", "komputer": "O", "meja": "O", "kursi": "O",
            "di-taman": "K", "di-kantor": "K", "di-perpustakaan": "K", "pada-malam-hari": "K", "dengan-cepat": "K"
        }

    def identify(self, token):
        # Mengembalikan kelompok kata (S, P, O, K) atau None jika tidak valid
        return self.valid_tokens.get(token.lower())
