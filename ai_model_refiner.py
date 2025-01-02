from core.golden_ratio import phi_scale, phi_inverse_scale

class AIModelRefiner:
    """
    Optimizes model parameters using Golden Ratio-based scaling.
    """
    def __init__(self, model):
        self.model = model

    def refine(self):
        for layer in self.model['layers']:
            layer['weights'] = [phi_scale(w) for w in layer['weights']]
        self.model['learning_rate'] = phi_scale(self.model['learning_rate'])
        self.model['dropout_rate'] = phi_inverse_scale(self.model['dropout_rate'])
        return self.model