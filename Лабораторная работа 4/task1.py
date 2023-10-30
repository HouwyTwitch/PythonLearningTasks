import json


# TODO решите задачу
def task() -> float:
    with open('input.json') as f:
        data = json.load(f)
    return round(sum([x['score']*x['weight'] for x in data]), 3)


print(task())
