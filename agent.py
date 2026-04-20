import json

# load JSON file
with open("reflection-tree.json") as f:
    data = json.load(f)

nodes = {node["id"]: node for node in data["nodes"]}

current = "START"

while True:
    node = nodes[current]

    print("\n" + node["text"])

    if node["type"] == "end":
        break

    elif node["type"] == "question":
        options = node["options"]
        for i, opt in enumerate(options):
            print(f"{i+1}. {opt}")

        choice = int(input("Choose option: ")) - 1
        answer = options[choice]

        # move to next manually (simple flow)
        if current == "Q1":
            if answer in ["Productive", "Mixed"]:
                current = "Q2A"
            else:
                current = "Q2B"

        elif current == "Q2A" or current == "Q2B":
            current = "Q3"

        elif current == "Q3":
            current = "R1"

        elif current == "Q4":
            current = "Q5"

        elif current == "Q5":
            current = "Q6"

        elif current == "Q6":
            current = "R2"

        elif current == "Q7":
            current = "Q8"

        elif current == "Q8":
            current = "Q9"

        elif current == "Q9":
            current = "Q10"

        elif current == "Q10":
            current = "R3"

    elif node["type"] == "reflection":
        input("Press Enter to continue...")
        if current == "R1":
            current = "BR1"
        elif current == "R2":
            current = "BR2"
        elif current == "R3":
            current = "SUMMARY"

    elif node["type"] == "bridge":
        input("Press Enter to continue...")
        if current == "BR1":
            current = "Q4"
        elif current == "BR2":
            current = "Q7"

    elif node["type"] == "summary":
        input("Press Enter to finish...")
        current = "END"

    elif node["type"] == "start":
        current = "Q1"