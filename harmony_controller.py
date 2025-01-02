class HarmonyController:
    """
    Tracks global Harmony vs Chaos metrics, referencing the “1F+1C=MOK”
    concept for dynamic gameplay or scenario generation.
    """
    def __init__(self):
        self.harmony_level = 50.0  # Starting in a neutral state
        self.chaos_level = 50.0
    
    def update_metrics(self, harmony_delta, chaos_delta):
        self.harmony_level += harmony_delta
        self.chaos_level += chaos_delta
    
    def get_status(self):
        return {
            "Harmony": round(self.harmony_level, 2),
            "Chaos": round(self.chaos_level, 2)}