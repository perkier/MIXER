# src/tracks/track.py
class TrackBase:
    def __init__(self, name, audio_data):
        self.name = name
        self.audio_data = audio_data
        self.effects = []
        self.eq = None
        self.filters = []

    def add_effect(self, effect):
        self.effects.append(effect)

    def set_eq(self, eq):
        self.eq = eq

    def add_filter(self, filter):
        self.filters.append(filter)

    def apply_effects(self):
        processed_data = self.audio_data
        for effect in self.effects:
            processed_data = effect.apply(processed_data)
        if self.eq:
            processed_data = self.eq.apply(processed_data)
        for filter in self.filters:
            processed_data = filter.apply(processed_data)
        return processed_data
