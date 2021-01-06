import requests

URL = "https://eval.repl.it/languages"

def format_icon(link: str):
    base = "https://repl.it"

    if "http" not in link:
        return base + link
    else:
        return link


def all_languages(sortBy="abc"):
    r = requests.get(URL)
    r.raise_for_status()
    r = r.json()

    if sortBy == "abc":
        result = []
        names = sorted([l["name"] for l in r])

        for n in names:
            for l in r:
                if l["name"] == n and l not in result:
                    result.append(l)
                else:
                    pass

        return result
    elif sortBy == "cat":
        result = {}

        cats = sorted(list(set([l["category"] for l in r])))
        cats.remove("Pratical")
        for cat in cats: result[cat] = []

        for l in r:
            if l["category"] == "Pratical":
                result["Practical"].append(l)
            else:
                result[l["category"]].append(l)

        return (cats, result)
