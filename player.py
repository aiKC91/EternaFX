class Player:
    """
    Basic representation of a player or user, referencing historic 
    or AI-based ‘characters’ from the notes (e.g., Turing, Newton).
    """
    def __init__(self, name: str, knowledge_level: float = 1.0):
        self.name = name
        self.knowledge_level = knowledge_level
    
    def gain_knowledge(self, amount: float):
        self.knowledge_level += amount