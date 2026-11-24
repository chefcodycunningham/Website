"""Site copy and menus shared by every sample design.

Prices come from tools/prices.json, which tools/sync_prices.py copies out of the private
menus repo (current season only). Edit prices there, never here."""
import json, os

PHONE = "970-470-2339"
INSTAGRAM = "https://www.instagram.com/chefcodycunningham/"

OPENING = "Private chef in the Vail Valley."
OFFER = ("Dinner parties, family-style feasts, ski-week stays, cocktail hours and cooking classes, "
         "cooked and served in your home.")

BIO = [
    "I learned to cook on a stool beside my grandmother, and was making béchamel for breakfast at six. "
    "Growing up in Bozeman, Montana meant wild game, foraged mushrooms and mountain berries, and I've cooked that way ever since.",
    "The work has taken me a long way from Montana: a nonprofit café on a permaculture farm in Tamil Nadu, cooking with millets "
    "and native grains; kitchens in Melbourne and Byron Bay, where I fell for lemon myrtle and bush pepper; then back to the "
    "mountains, at Sweet Basil and Mountain Standard, and as executive chef of Larkspur in Vail.",
    "Now I cook in people's homes. My wife is Italian, we live in Avon, and we go back to Italy every year to eat. "
    "Her mother's tiramisù is on my menus.",
]
BIO_SHORT = BIO[0] + " " + BIO[2]
CLOSING = "Tell me about the evening you have in mind."

PLACES = ["Bozeman", "Tamil Nadu", "Melbourne", "Byron Bay", "Vail"]

MENU_INTRO = ("Every menu here is a starting point. Tell me what you love, what you don't, and anything you can't eat, "
              "and I'll write one for your table.")

# (section, note, [(menu name, line, [items])])
MENUS = [
    ("Plated", "Courses served at the table", [
        ("The Classic", "Three courses", [
            "King crab linguine, prosciutto di Parma, tarragon beurre fondue",
            "Wagyu NY strip, potato dauphinoise, local mushrooms, shallot, bordelaise",
            "Raspberry, chocolate sponge, raspberry confit, milk chocolate mousse"]),
        ("The Coastal", "Three courses", [
            "Ahi tuna crudo, cucumber aguachile, Fresno oil, chayote, avocado",
            "Ora King salmon, Romanesco, confit tomatoes, spinach, beurre fondue",
            "Key lime tartlet, key lime crémeux and mousse"]),
        ("The Bistro", "Three courses", [
            "Endive, blood orange, chervil, chèvre",
            "Rohan duck breast, peas and carrots, pear demi-glace",
            "Pistachio strawberry tart"]),
        ("A Birthday in Vail", "Four courses, from a recent dinner", [
            "Snow crab, drawn butter, lemon",
            "Ahi tuna crudo, cucumber aguachile, Fresno oil, chayote, avocado",
            "Wagyu NY strip, potato dauphinoise, local mushrooms, shallot, bordelaise",
            "Raspberry, dark chocolate"]),
    ]),
    ("Family Style", "Platters down the middle of the table", [
        ("Steak Night", "", [
            "Wagyu NY strip, bordelaise",
            "Sourdough boule, grass-fed herb butter",
            "Mixed greens, sprouts, radish, sunflower seeds, bacon lardons, avocado mousse",
            "Broccolini, garlic confit, lemon",
            "Roasted fingerlings, pecorino, thyme",
            "Blood orange chocolate tartlet, whipped milk chocolate ganache"]),
        ("Italian Night", "", [
            "Polpette all'arrabbiata, meatballs in angry red sauce",
            "Buffalo mozzarella, heirloom tomatoes, arugula, basil",
            "Shrimp scampi, fresh linguine, garlic, chili, vino bianco",
            "16-hour Bolognese, fresh spaghetti, 24-month Parmigiano Reggiano",
            "Roasted eggplant · Asparagus, preserved lemon",
            "My mother-in-law's tiramisù"]),
        ("Surf and Turf", "", [
            "Wagyu NY strip, tarragon salsa verde",
            "Ora King salmon",
            "Caesar, brioche croutons, Parmigiano Reggiano",
            "Roasted winter roots · Potato dauphinoise",
            "Apple, cinnamon, caramel"]),
        ("Sushi Night", "", [
            "Snow crab California · Spicy ahi, crispy onion · Ora King Philly",
            "Sashimi: ahi with aguachile, Ora King with ponzu, hiramasa with yuzu",
            "Nigiri: ahi tuna, Ora King salmon, sea urchin",
            "Seaweed salad · Cucumber, sesame, rice wine vinegar",
            "Mango, passion fruit, vanilla sponge, white chocolate"]),
        ("Korean Barbecue", "A lettuce-cup taco bar", [
            "Three-layer pork belly · Gochujang pork ribs · NY strip · Seared tuna",
            "Hot and mild kimchi · Sprout and cucumber salad",
            "Matsutake shoyu-glazed mushrooms · Bok choy · Baby peppers",
            "Scallions, cilantro and ten different sauces",
            "Snickers éclair: caramel, peanuts, chocolate"]),
        ("Indian Feast", "", [
            "Palak paneer · Dahl and chana",
            "Goan seafood curry, shrimp, coconut",
            "Murgh makhani, butter chicken",
            "Jasmine rice · Garlic naan · Mint chutney · Raita · Chili crisp",
            "Cloud: vanilla sponge, blackcurrant, white chocolate mousse"]),
        ("Mediterranean", "", [
            "Rack of lamb, mint yogurt",
            "Snapper, fennel, tomatoes",
            "Hummus, tzatziki, baba ganoush, warm pita",
            "Saganaki halloumi · Couscous",
            "Honey cake"]),
    ]),
    ("To Begin", "Before dinner, or instead of it", [
        ("Hors d'Oeuvres", "", [
            "Smoked salmon rillettes, Ora King roe, butter pastry",
            "Bluefin tuna, capsicum, yuzu, scallion",
            "A5 wagyu, bacon and egg yolk jam, brioche",
            "Local mushroom duxelles, black garlic, pickled shimeji",
            "Confit duck, pickled mustard seed, Peruvian pepper",
            "Prawn salad, tarragon rémoulade, endive"]),
        ("Fruits de Mer", "", [
            "East and West Coast oysters, dueling mignonettes",
            "Alaskan king crab, drawn butter · Jonah crab claws, Dijon aioli",
            "Shrimp cocktail, lemon myrtle tomato chutney",
            "White sturgeon caviar, blinis, chive crème fraîche",
            "Lobster salad, tarragon · Salmon gravlax"]),
        ("Fromage & Salumi", "", [
            "Fromage d'Affinois · 36-month Beemster gouda · Stilton",
            "Soppressata · Prosciutto di Parma · Coppa",
            "24-month Parmesan, artichokes, Italian olives",
            "Seasonal jams and fruit · Lavash · Grissini · Ciabatta"]),
    ]),
    ("Stays & Experiences", "From past events", [
        ("A Week in Residence", "Christmas in the mountains", [
            "Lentil soup, fresh linguine with basil pesto, beef milanese, salmoriglio",
            "Paella valenciana, chicken and beef empanadas, papas bravas",
            "Trio of tenderloins, roasted chicken, lobster tail, bordelaise, chimichurri",
            "Fondue night, one traditional and one aged cheese",
            "Gingerbread houses, cookie decorating and a chocolatier for the kids"]),
        ("A Family Reunion", "Four days, twenty-five guests", [
            "Italian night: spaghettini and veal meatballs, chicken parm, tricolore",
            "Crab extravaganza: corn on the cob, slaw, roasted vegetables",
            "Steak night: NY strips, ribeyes, bordelaise, tarragon salsa verde",
            "Pizza party and dueling salads",
            "Mediterranean night: kebabs, hummus, baba ghanoush, couscous"]),
        ("Sushi Workshop", "I teach, your group rolls", [
            "Snow crab · Yellowtail · Ora King salmon · Hiramasa · Uni",
            "Avocado · Cucumber · Jalapeño · Crispy onion · Tobiko · Wakame",
            "Spicy mayo · Eel sauce · Ponzu · Shoyu · Wasabi",
            "Mochi"]),
    ]),
]

_PRICE_DATA = json.load(open(os.path.join(os.path.dirname(__file__), "prices.json"), encoding="utf-8"))
SEASON = _PRICE_DATA["season"]
_PRICES = _PRICE_DATA["prices"]

# Sample-site menu name -> name in the season's menu.md, where they differ.
_ALIASES = {
    "Italian Night": "Italian Favorites",
    "Korean Barbecue": "Korean BBQ: An Asian Lettuce-Cup Taco Bar",
    "Mediterranean": "Mediterranean Surf and Turf",
    "Hors d'Oeuvres": "Hors d’Oeuvres",
    "Fromage & Salumi": "Fromage, Antipasti & Salumi",
    "Sushi Workshop": "Sushi Making Workshop",
}
# Menus with no published price (custom events and stays).
_CUSTOM = "Priced to your event"


def price_for(name):
    """Price line for a sample menu, e.g. '$850 chef fee · $120 per person'."""
    return _PRICES.get(_ALIASES.get(name, name), _CUSTOM)


PRICE_NOTE = (f"{SEASON} pricing: a chef fee plus a per-person fee. Menus and prices can change "
              "with availability, season and guest count.")

EXTRAS = (f"A sommelier, mixologist or server can join any dinner: {price_for('Mixologist, Sommelier, Server')}. "
          "A server is required for plated dinners of 8 or more guests.")

# Photo library, path relative to assets/img
P = {k: f"{k}.jpg" for k in [
    "tuna-tataki", "scallops-coho-roe", "beet-salad", "steak-wine", "duck-green", "sea-bass", "foie-torchon",
    "wagyu-ny-strip", "king-crab-caviar", "melon-gazpacho", "charcuterie", "crudite", "caviar", "wagyu-tartare",
    "salmon-crudo", "cacio-e-pepe-truffle", "stuffed-calamari", "uni-gem-lettuce", "watermelon-rice", "lobster",
    "peach-salad", "albacore-carrot", "wagyu-onion-mousse", "fish-daikon-beet", "cured-salmon", "salmon-quinoa",
    "swordfish", "scallops-carrot", "avocado-toast", "portrait", "duck-breast"]}

ALT = {
    "tuna-tataki": "Tuna tataki, cucumber aguachile, radish, pomegranate",
    "scallops-coho-roe": "Herb pressed scallops with coho roe on a black plate",
    "beet-salad": "Roasted beets, chèvre and sprouts in a white bowl",
    "steak-wine": "Sliced wagyu with chanterelles and a glass of red wine",
    "duck-green": "Duck breast with peas and carrots on a green purée",
    "sea-bass": "Sea bass, asparagus, shallot and turnip",
    "foie-torchon": "Foie torchon, rabbit terrine, cherry",
    "wagyu-ny-strip": "Wagyu NY strip, local mushrooms, potato dauphinoise",
    "king-crab-caviar": "King crab and caviar over fresh pasta",
    "melon-gazpacho": "Melon gazpacho with caviar and crab",
    "charcuterie": "Cheese and charcuterie board",
    "crudite": "Crudités standing in a lit glass trough",
    "caviar": "Caviar service with garnishes",
    "wagyu-tartare": "A5 wagyu tartare, chanterelles, cured yolk",
    "salmon-crudo": "Salmon crudo plated for a dinner party",
    "cacio-e-pepe-truffle": "Cacio e pepe under shaved white truffle",
    "stuffed-calamari": "Stuffed calamari, beet rémoulade, cilantro pesto",
    "uni-gem-lettuce": "Uni, gem lettuce, salmon roe",
    "watermelon-rice": "Watermelon, rice, avocado and balsamic bites",
    "lobster": "Lobster, pearl onion and chili on spoons",
    "peach-salad": "Peach salad with herbs and flowers",
    "albacore-carrot": "Albacore, coconut cream, carrot variations",
    "wagyu-onion-mousse": "Wagyu, caramelized onion mousse, tomato",
    "fish-daikon-beet": "Fish, daikon, citrus and beet",
    "cured-salmon": "Cured salmon, capers, potato chip",
    "salmon-quinoa": "Salmon, quinoa, nasturtium",
    "swordfish": "Swordfish, daikon, citrus",
    "scallops-carrot": "Scallops, coconut cream, carrot, herbs",
    "avocado-toast": "Avocado toast, pickled red onion, seeds",
    "portrait": "Chef Cody Cunningham in chef's whites",
    "duck-breast": "Duck breast, peppers, pear, peas",
}
