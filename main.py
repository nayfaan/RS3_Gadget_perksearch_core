from tqdm import tqdm
import itertools
import numpy as np
import math

import os
from multiprocessing import Pool

from services.comps import comps
from services.comp_list import comp_list


def reverseDict(_dict, _val):
    return list(_dict.keys())[list(_dict.values()).index(_val)]


def combLen(n, r):
    return math.factorial(n + r - 1) / (math.factorial(r) * math.factorial(n - 1))


def write2file(arr, filename):
    _arr = np.empty(len(arr), dtype=object)
    _arr[:] = arr

    n = len(_arr)
    k = min(max(100, int(n / 100)), n)

    with open("./output/" + filename + ".js", "w") as f:
        f.write("var " + filename + " = [")

        with tqdm(
            total=n,
            desc="Printing: " + filename,
            mininterval=1,
            bar_format="{l_bar}{bar:20}{r_bar}{bar:-20b}",
            dynamic_ncols=True,
        ) as pbar:
            for i in range(0, n, k):
                chunk = _arr[i : i + k]
                chunk.tofile(f, sep=", ")
                pbar.update(len(chunk))

        f.write("]")

    print("Completed: " + filename)


def comps_permutator(gizmo, type):
    iterable = comps["normal"][gizmo]
    slots = None
    if type == "normal":
        slots = 5
    elif type == "ancient":
        slots = 9
        iterable = np.concatenate([iterable, comps["ancient"][gizmo]])
    elif type == "test":
        slots = 5
        iterable = np.concatenate([iterable, comps["ancient"][gizmo]])

    print()
    result = []
    with tqdm(
        total=combLen(len(iterable), slots),
        desc="Iterating: " + type + " " + gizmo,
        mininterval=1,
        bar_format="{l_bar}{bar:20}{r_bar}{bar:-20b}",
        dynamic_ncols=True,
    ) as pbar:
        for p in itertools.combinations_with_replacement(tqdm(iterable), slots):
            result.append(p)
            pbar.update()

    return result

def run():
    pool = Pool(os.cpu_count() - 1)
    
    perm = {"tool": {}, "weapon": {}, "armour": {}}

    # test = pool.starmap(comps_permutator, [("tool", "test")])
    # pool.starmap(write2file, [(test, "test")])
    # test = comps_permutator("tool", "test")
    # write2file(test, "test")
    
    # # Normal gizmos (compiled)
    # perm["tool"]["normal"] = comps_permutator("tool", "normal")
    # write2file(perm["tool"]["normal"], "tool_normal")

    # perm["weapon"]["normal"] = comps_permutator("weapon", "normal")
    # write2file(perm["weapon"]["normal"], "weapon_normal")

    # perm["armour"]["normal"] = comps_permutator("armour", "normal")
    # write2file(perm["armour"]["normal"], "armour_normal")

    # Ancient gizmos
    perm["tool"]["ancient"] = pool.starmap(comps_permutator, [("tool", "ancient")])
    pool.starmap(write2file, [(perm["tool"]["ancient"], "tool_ancient")])

    perm["weapon"]["ancient"] = pool.starmap(comps_permutator, [("weapon", "ancient")])
    pool.starmap(write2file, [(perm["weapon"]["ancient"], "weapon_ancient")])

    perm["armour"]["ancient"] = pool.starmap(comps_permutator, [("armour", "ancient")])
    pool.starmap(write2file, [(perm["armour"]["ancient"], "armour_ancient")])

    pool.starmap(write2file, [(perm, "perm")])

    pool.close()
    pool.join()


if __name__ == "__main__":
    run()
    print()
