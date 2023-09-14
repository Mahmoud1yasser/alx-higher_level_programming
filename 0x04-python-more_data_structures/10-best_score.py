#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return (None)
    else:
        n = []
        f = []
        for k, v in a_dictionary.items():
            n.append(k)
            f.append(v)
            po = max(f)
            q = f.index(po)
        return (n[q])
