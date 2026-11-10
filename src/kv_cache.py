"""Streaming KV-cache compressor."""


class StreamingCompressor:
    def __init__(self, block_size=64, budget=2048):
        self.block_size = block_size
        self.budget = budget

    def compress(self, keys, values):
        return keys[:, -self.budget:], values[:, -self.budget:]
