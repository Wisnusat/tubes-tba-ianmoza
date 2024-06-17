from token_identifier import TokenIdentifier

class SentenceValidator:
    def __init__(self):
        self.token_identifier = TokenIdentifier()

    def validate(self, sentence):
        tokens = sentence.split()
        structure = []

        for token in tokens:
            token_type = self.token_identifier.identify(token)
            if not token_type:
                return f"{token} Ditolak", structure

            structure.append(token_type)

        valid_structures = [
            ["S", "P", "O", "K"],
            ["S", "P", "K"],
            ["S", "P", "O"],
            ["S", "P"]
        ]

        if structure in valid_structures:
            return "Diterima", structure
        else:
            return "Ditolak", structure
