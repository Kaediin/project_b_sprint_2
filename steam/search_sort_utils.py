from itertools import islice

# Merge recursive algorithm
def merge_recursive(arr, key):
    if len(arr) > 1:
        # Divide
        q = len(arr) // 2

        p = arr[:q]

        r = arr[q:]

        merge_recursive(p, key)

        merge_recursive(r, key)

        i, j, k = 0, 0, 0

        # Combine
        while i < len(p) and j < len(r):
            if p[i][key] < r[j][key]:
                arr[k] = p[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(p):
            arr[k] = p[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1
    return arr

# Insertion sort algorithm
def insertionsort(data, key):
    result = [data[0]]
    del data[0]

    for entry in data:
        inserted = False
        for c in range(0, len(result)):
            if entry[key] < result[c][key]:
                result.insert(c, entry)
                inserted = True
                break
        if not inserted:
            result.append(entry)

    return result

# CENTRUMMATEN

def mean(lst):
    return sum(lst) / len(lst)


def median(lst):
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2] + lst[(len(lst) // 2) - 1]) / 2
    return float(lst[len(lst) // 2])


def freq(lst):
    frqs = dict()
    for n in lst:
        if f"{n}" in frqs:
            frqs[f"{n}"] += 1
        else:
            frqs[f"{n}"] = 1
    return frqs


def modes(lst):
    frqs = freq(lst)
    modi = [k for k, v in frqs.items() if v == frqs[max(frqs, key=frqs.get)]]
    return sorted(modi)


# SPREIDINGSMATEN

def var(lst):
    return sum(map(lambda e: (e - mean(lst)) ** 2, lst)) / len(lst)


def std(lst):
    return var(lst) ** 0.5


def q1(lst):
    return median(sorted(lst)[:len(lst) // 2])


def q3(lst):
    return median(sorted(lst)[len(lst) // 2 + (1 * (len(lst) % 2)):])


def rnge(lst):
    return max(lst) - min(lst)


# TOTAAL

def stats(dicts, key, force_int=False):     # beste als 'dicts' al gesorteerd is
    if force_int:
        values = [int(e[key]) for e in dicts]
    else:
        values = [e[key] for e in dicts]
    return {
        "mean": mean(values),
        "median": median(values),
        "modus": modes(values),
        "variance": var(values),
        "standard": std(values),
        "q1": q1(values),
        "q3": q3(values),
        "range": rnge(values)
    }


# FIX THIS!
# def binary_recursive(arr, appid):
#     q = len(arr) // 2
#     selected = arr[q]['appid']
#     print(arr[q]['appid'])
#     if len(arr) == 1:
#         return True if int(selected) == int(appid) else False
#     elif int(selected) == int(appid):
#         return True
#     else:
#         if int(selected) < int(appid):
#             return binary_recursive((arr[q:]), appid)
#         else:
#             return binary_recursive((arr[:q]), appid)
