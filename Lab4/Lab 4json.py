import json
with open('sample-data.json') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 79)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("-" * 79)

for item in data["imdata"]:
    attr = item["l1PhysIf"]["attributes"]
    dn = attr.get("dn", "")
    descr = attr.get("descr", "")
    speed = attr.get("speed", "")
    mtu = attr.get("mtu", "")
    
    print(f"{dn:<50} {descr:<20} {speed:<7} {mtu:<6}")
