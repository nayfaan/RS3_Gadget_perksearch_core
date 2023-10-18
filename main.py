from tqdm import tqdm
import itertools

comps = {
    "normal": {
        "tool": [
            "null",
            "Precious components",
            "Precise components",
            "Pious components",
            "Evasive components",
            "Blade parts",
            "Magic parts",
            "Deflecting parts",
            "Direct components",
            "Refined components",
            "Resilient components",
            "Enhancing components",
            "Simple parts",
            "Oceanic components",
            "Fungal components",
            "Heavy components",
            "Armadyl components",
            "Flexible parts",
            "Third-age components",
            "Cover parts",
            "Spiritual parts",
            "Light components",
            "Base parts",
            "Plated parts",
            "Swift components",
            "Clear parts",
            "Healthy components",
            "Smooth parts",
            "Sharp components",
            "Protective components",
            "Imbued components",
            "Ethereal components",
            "Subtle components",
            "Fortunate components",
            "Living components",
            "Seren components",
            "Ascended components",
            "Crystal parts",
            "Strong components",
            "Shifting components",
            "Organic parts",
            "Dextrous components",
            "Variable components",
            "Stave parts",
            "Zaros components",
            "Silent components",
            "Head parts",
            "Explosive components",
            "Undead components",
            "Stunning components",
            "Clockwork components",
            "Spiked parts",
            "Zamorak components",
            "Brassican components",
            "Padded parts",
            "Dragonfire components",
            "Delicate parts",
            "Tensile parts",
            "Crafted parts",
            "Metallic parts",
        ],
        "weapon": [
            "null",
            "Precious components",
            "Precise components",
            "Pious components",
            "Evasive components",
            "Blade parts",
            "Magic parts",
            "Deflecting parts",
            "Direct components",
            "Shadow components",
            "Refined components",
            "Enhancing components",
            "Ilujankan components",
            "Simple parts",
            "Oceanic components",
            "Heavy components",
            "Armadyl components",
            "Flexible parts",
            "Third-age components",
            "Cover parts",
            "Spiritual parts",
            "Cywir components",
            "Light components",
            "Base parts",
            "Plated parts",
            "Swift components",
            "Saradomin components",
            "Clear parts",
            "Healthy components",
            "Smooth parts",
            "Knightly components",
            "Sharp components",
            "Protective components",
            "Imbued components",
            "Ethereal components",
            "Subtle components",
            "Fortunate components",
            "Bandos components",
            "Living components",
            "Culinary components",
            "Seren components",
            "Ascended components",
            "Crystal parts",
            "Strong components",
            "Powerful components",
            "Avernic components",
            "Shifting components",
            "Organic parts",
            "Dextrous components",
            "Variable components",
            "Stave parts",
            "Zaros components",
            "Head parts",
            "Explosive components",
            "Undead components",
            "Stunning components",
            "Clockwork components",
            "Spiked parts",
            "Zamorak components",
            "Brassican components",
            "Padded parts",
            "Noxious components",
            "Connector parts",
            "Dragonfire components",
            "Delicate parts",
            "Rumbling components",
            "Tensile parts",
            "Crafted parts",
            "Metallic parts",
        ],
        "armour": [
            "null",
            "Precious components",
            "Precise components",
            "Pious components",
            "Evasive components",
            "Blade parts",
            "Magic parts",
            "Deflecting parts",
            "Direct components",
            "Refined components",
            "Resilient components",
            "Enhancing components",
            "Simple parts",
            "Oceanic components",
            "Fungal components",
            "Heavy components",
            "Armadyl components",
            "Flexible parts",
            "Third-age components",
            "Cover parts",
            "Spiritual parts",
            "Light components",
            "Base parts",
            "Plated parts",
            "Swift components",
            "Saradomin components",
            "Clear parts",
            "Healthy components",
            "Smooth parts",
            "Knightly components",
            "Sharp components",
            "Protective components",
            "Imbued components",
            "Ethereal components",
            "Subtle components",
            "Fortunate components",
            "Bandos components",
            "Living components",
            "Culinary components",
            "Seren components",
            "Ascended components",
            "Corporeal components",
            "Crystal parts",
            "Strong components",
            "Powerful components",
            "Shifting components",
            "Organic parts",
            "Dextrous components",
            "Faceted components",
            "Pestiferous components",
            "Variable components",
            "Stave parts",
            "Zaros components",
            "Silent components",
            "Head parts",
            "Explosive components",
            "Undead components",
            "Stunning components",
            "Clockwork components",
            "Spiked parts",
            "Zamorak components",
            "Brassican components",
            "Padded parts",
            "Noxious components",
            "Connector parts",
            "Harnessed components",
            "Dragonfire components",
            "Delicate parts",
            "Tensile parts",
            "Crafted parts",
            "Metallic parts",
        ],
    },
    "ancient": {
        "tool": [
            "Historic components",
            "Vintage components",
            "Timeworn components",
            "Classic components",
        ],
        "weapon": [
            "Historic components",
            "Vintage components",
            "Timeworn components",
            "Classic components",
        ],
        "armour": ["Historic components", "Vintage components", "Classic components"],
    },
}

def write2file(arr, filename):
    with open("./output/" + filename + ".js", "w") as f:
        f.write("var " + filename + " = ")
        arr = str(arr)
        n = len(arr)
        k = max(1000, int(n/100))
        with tqdm(
            total=n, desc="Printing: " + filename, mininterval=1
        ) as pbar:
            for i in range(0, n, k):
                chunk = arr[i : i+k]
                f.write(chunk)
                pbar.update(len(chunk))

    print("Completed: " + filename)


def comps_permutator(gizmo, type):
    iterable = comps["normal"][gizmo]
    slots = None
    if type == "normal":
        slots = 5
    elif type == "ancient":
        slots = 9
        iterable = iterable + comps["ancient"][gizmo]
    # elif type == "test":
    #     slots = 13
    #     iterable = comps["ancient"][gizmo]

    print()
    result = []
    with tqdm(
        total=pow(len(iterable), slots),
        desc="Iterating: " + type + " " + gizmo,
        mininterval=1,
    ) as pbar:
        for p in itertools.product(tqdm(iterable), repeat=slots):
            result.append(p)
            pbar.update()

    return result


def run():
    perm = {"tool": {}, "weapon": {}, "armour": {}}

    # test = comps_permutator("armour", "test")
    # write2file(test, "test")

    perm["tool"]["normal"] = comps_permutator("tool", "normal")
    write2file(perm["tool"]["normal"],"tool_normal")

    perm["tool"]["ancient"] = comps_permutator("tool", "ancient")
    write2file(perm["tool"]["ancient"],"tool_ancient")

    perm["weapon"]["normal"] = comps_permutator("weapon", "normal")
    write2file(perm["weapon"]["normal"],"weapon_normal")

    perm["weapon"]["ancient"] = comps_permutator("weapon", "ancient")
    write2file(perm["weapon"]["ancient"],"weapon_ancient")

    perm["armour"]["normal"] = comps_permutator("armour", "normal")
    write2file(perm["armour"]["normal"],"armour_normal")

    perm["armour"]["ancient"] = comps_permutator("armour", "ancient")
    write2file(perm["armour"]["ancient"],"armour_ancient")

    write2file(perm,"perm")

if __name__ == "__main__":
    run()
    print()

