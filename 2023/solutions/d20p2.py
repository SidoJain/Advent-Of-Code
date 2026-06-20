import collections
import math
from typing import Any

def parseInput(filename: str) -> dict[str, dict[str, Any]]:
    with open(filename) as file:
        lines = [line.strip() for line in file if line.strip()]

    modules = {}
    for line in lines:
        name_str, dests_str = line.split(" -> ")
        dests = dests_str.split(", ")

        if name_str == "broadcaster":
            type_ = "b"
            name = "broadcaster"
        else:
            type_ = name_str[0]
            name = name_str[1:]

        modules[name] = {
            "type": type_,
            "destinations": dests,
            "memory": {},
            "state": False
        }
    return modules

def calcFewestPressesForRx(modules: dict[str, dict[str, Any]]) -> int:
    for name, mod in modules.items():
        for dest in mod["destinations"]:
            if dest in modules and modules[dest]["type"] == "&":
                modules[dest]["memory"][name] = False 

    feed_module = None
    for name, mod in modules.items():
        if 'rx' in mod["destinations"]:
            feed_module = name
            break

    cycle_lengths = {}
    for name, mod in modules.items():
        if feed_module in mod["destinations"]:
            cycle_lengths[name] = 0

    presses = 0
    while True:
        presses += 1
        queue = collections.deque([("button", "broadcaster", False)])
        while queue:
            src, target, pulse = queue.popleft()
            if target not in modules:
                continue

            if target == feed_module and pulse == True:
                if cycle_lengths[src] == 0:
                    cycle_lengths[src] = presses
                if all(cycle_lengths.values()):
                    return math.lcm(*cycle_lengths.values())

            mod = modules[target]
            if mod["type"] == "b":
                out_pulse = pulse
                for dest in mod["destinations"]:
                    queue.append((target, dest, out_pulse))
            elif mod["type"] == "%":
                if not pulse:
                    mod["state"] = not mod["state"]
                    out_pulse = mod["state"]
                    for dest in mod["destinations"]:
                        queue.append((target, dest, out_pulse))
            elif mod["type"] == "&":
                mod["memory"][src] = pulse
                out_pulse = not all(mod["memory"].values())
                for dest in mod["destinations"]:
                    queue.append((target, dest, out_pulse))

modules = parseInput('../inputs/input20.txt')
print(calcFewestPressesForRx(modules))