__DEV__ = True

DevLog = __DEV__ and print or (lambda *a, **k: None)
