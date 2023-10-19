from tqdm import tqdm
import itertools
import numpy as np
import math

import multiprocessing
import threading

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

def comps_permutator(gizmo, type, queue=None):
    iterable = comps["normal"][gizmo]
    slots = None
    if type == "normal":
        slots = 5
    elif type == "ancient":
        slots = 9
        iterable = np.concatenate([iterable, comps["ancient"][gizmo]])
    elif type == "test":
        slots = 5
        # iterable = np.concatenate([iterable, comps["ancient"][gizmo]])

    pos = 0
    if queue:
        current = multiprocessing.current_process()
        pos = current._identity[0]-1

    print()
    result = []
    with tqdm(
        total=combLen(len(iterable), slots),
        desc="Iterating: " + type + " " + gizmo,
        mininterval=1,
        bar_format="{l_bar}{bar:20}{r_bar}{bar:-20b}",
        dynamic_ncols=True,
        position=pos
    ) as pbar:
        for p in itertools.combinations_with_replacement(tqdm(iterable), slots):
            result.append(p)
            pbar.update()

    if queue:
        queue.put(result)
    else:
        return result

def run():
    # pool = multiprocessing.Pool(os.cpu_count() - 1)
    
    perm = {"tool": {}, "weapon": {}, "armour": {}}

    # test = comps_permutator("tool", "test")
    # write2file(test, "test")
    # test = pool.starmap(comps_permutator, [("tool", "test")])
    # pool.starmap(write2file, [(test, "test")])
    # test_q1 = multiprocessing.Queue()
    # test_q2 = multiprocessing.Queue()
    # test_q3 = multiprocessing.Queue()
    # test_p1 = multiprocessing.Process(target=comps_permutator, args=("tool", "test", test_q1))
    # test_p2 = multiprocessing.Process(target=comps_permutator, args=("weapon", "test", test_q2))
    # test_p3 = multiprocessing.Process(target=comps_permutator, args=("armour", "test", test_q3))
    # test_p1.start()
    # test_p2.start()
    # test_p3.start()
    # t1 = test_q1.get()
    # t2 = test_q2.get()
    # t3 = test_q3.get()
    # test_p1.join()
    # test_p2.join()
    # test_p3.join()
    # write2file(t1, "t1")
    # write2file(t2, "t2")
    # write2file(t3, "t3")
    
    # # Normal gizmos (compiled)
    # perm["tool"]["normal"] = comps_permutator("tool", "normal")
    # write2file(perm["tool"]["normal"], "tool_normal")

    # perm["weapon"]["normal"] = comps_permutator("weapon", "normal")
    # write2file(perm["weapon"]["normal"], "weapon_normal")

    # perm["armour"]["normal"] = comps_permutator("armour", "normal")
    # write2file(perm["armour"]["normal"], "armour_normal")

    # Ancient gizmos
    queue1 = multiprocessing.Queue()
    queue2 = multiprocessing.Queue()
    queue3 = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=comps_permutator, args=("tool", "ancient", queue1))
    p2 = multiprocessing.Process(target=comps_permutator, args=("weapon", "ancient", queue2))
    p3 = multiprocessing.Process(target=comps_permutator, args=("armour", "ancient", queue3))

    p1.start()
    p2.start()
    p3.start()
    
    perm["tool"]["ancient"] = queue1.get()
    perm["weapon"]["ancient"] = queue2.get()
    perm["armour"]["ancient"] = queue3.get()

    p1.join()
    p2.join()
    p3.join()

    t1 = threading.Thread(target=write2file, args=(perm["tool"]["ancient"], "tool_ancient"))
    t2 = threading.Thread(target=write2file, args=(perm["weapon"]["ancient"], "weapon_ancient"))
    t3 = threading.Thread(target=write2file, args=(perm["armour"]["ancient"], "armour_ancient"))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    # write2file(perm, "perm")

if __name__ == "__main__":
    run()
    print()
