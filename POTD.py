import sys, os
print("PYTHONPATH:", os.environ.get("PYTHONPATH"))
print("sys.path:", sys.path)
sys.modules.pop("requests", None)
sys.path = ['/volume1/@appstore/Python3.9/usr/lib/python3.9/site-packages']

print("Python version:", sys.version)
print("Python executable:", sys.executable)

sys.path = [p for p in sys.path if "Pc/other stuff" not in p]
import requests
print("Using requests from:", getattr(requests, '__file__', 'None'))

print("Using requests from:", getattr(requests, '__file__', 'None'))
print("requests contents:", dir(requests))

print("Using requests from:", requests.__file__)
print("Type of requests:", type(requests))
print("Contents of requests:", dir(requests))

print("Using requests from:", requests.__file__)

import random

def get_random_pokemon_id():
    # PokéAPI currently supports up to Gen IX (1010 Pokémon as of Oct 2025)
    return random.randint(1, 1010)

def fetch_pokemon_data(pokemon_id):
    base_url = "https://pokeapi.co/api/v2"
    pokemon_url = f"{base_url}/pokemon/{pokemon_id}"
    species_url = f"{base_url}/pokemon-species/{pokemon_id}"

    pokemon_data = requests.get(pokemon_url).json()
    species_data = requests.get(species_url).json()

    # Evolution chain
    evo_chain_url = species_data["evolution_chain"]["url"]
    evo_chain_data = requests.get(evo_chain_url).json()

    return {
        "name": pokemon_data["name"].title(),
        "id": pokemon_data["id"],
        "types": [t["type"]["name"].title() for t in pokemon_data["types"]],
        "abilities": [a["ability"]["name"].title() for a in pokemon_data["abilities"]],
        "stats": {s["stat"]["name"]: s["base_stat"] for s in pokemon_data["stats"]},
        "sprite": pokemon_data["sprites"]["front_default"],
        "flavor_text": next(
            (entry["flavor_text"] for entry in species_data["flavor_text_entries"]
             if entry["language"]["name"] == "en"), "No flavor text available."
        ),
        "evolution_chain": extract_evolution_chain(evo_chain_data["chain"])
    }

def extract_evolution_chain(chain):
    evo_chain = []
    current = chain
    while current:
        evo_chain.append(current["species"]["name"].title())
        if current["evolves_to"]:
            current = current["evolves_to"][0]
        else:
            break
    return evo_chain

def display_pokemon(pokemon):
    print(f"\n🌟 Pokémon of the Day: {pokemon['name']} (#{pokemon['id']})")
    print(f"Types: {', '.join(pokemon['types'])}")
    print(f"Abilities: {', '.join(pokemon['abilities'])}")
    print("Stats:")
    for stat, value in pokemon["stats"].items():
        print(f"  {stat.title()}: {value}")
    print(f"Evolution Chain: {' → '.join(pokemon['evolution_chain'])}")
    print(f"Flavor Text: {pokemon['flavor_text']}")
    print(f"Sprite URL: {pokemon['sprite']}")

def send_to_discord(pokemon, webhook_url):
    content = (
        f"🌟 **Pokémon of the Day** 🌟\n"
        f"**Name:** {pokemon['name']} (#{pokemon['id']})\n"
        f"**Types:** {', '.join(pokemon['types'])}\n"
        f"**Abilities:** {', '.join(pokemon['abilities'])}\n"
        f"**Stats:**\n" +
        "\n".join([f"• {stat.title()}: {val}" for stat, val in pokemon["stats"].items()]) + "\n" +
        f"**Evolution Chain:** {' → '.join(pokemon['evolution_chain'])}\n"
        f"**Flavor Text:** {pokemon['flavor_text']}\n"
        f"[Sprite Image]({pokemon['sprite']})"
    )

    payload = {"content": content}
    requests.post(webhook_url, json=payload)


if __name__ == "__main__":
    webhook_url = "https://discord.com/api/webhooks/1428475018857152663/LET-lcuKHH7HscwKKa37jjHyWXYLHqyN03CimnqMdlgj7p4JyP9wJjoLQUZ_IGyJjLI0"
    
    random_id = get_random_pokemon_id()
    pokemon = fetch_pokemon_data(random_id)
    
    display_pokemon(pokemon)
    send_to_discord(pokemon, webhook_url)
