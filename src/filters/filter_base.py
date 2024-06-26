class FilterBase:
    def __init__(self, name):
        self.name = name

    def apply(self, audio_data):
        # This method should be overridden by all subclasses
        raise NotImplementedError("FilterBase subclasses must implement the apply method")
