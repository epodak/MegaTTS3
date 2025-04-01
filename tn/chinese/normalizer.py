class Normalizer:
    def __init__(self, overwrite_cache=False, remove_erhua=False, remove_interjections=False):
        self.overwrite_cache = overwrite_cache
        self.remove_erhua = remove_erhua
        self.remove_interjections = remove_interjections
    
    def normalize(self, text):
        # 简单实现，实际上应该包含更复杂的文本规范化逻辑
        return text 