from tlib.datautil.random import MultiClassRandDataGen


def gen_cat() -> str:
    return "cat"

def gen_dog() -> str:
    return "dog"


def gen_bird() -> str:
    return "bird"


def gen_frog() -> str:
    return "frog"

def main():
    m = MultiClassRandDataGen()
    m.add(50, gen_cat)
    print(m.get_current_percentage())
    m.add(30, gen_dog)
    print(m.get_current_percentage())
    m.add(15, gen_bird)
    print(m.get_current_percentage())
    m.add(5, gen_frog)
    print(m.get_current_percentage())
    r = []
    for _ in range(10000):
        r.append(m.gen())
    print(r)


if __name__ == "__main__":
    main()
