# Skills Test 3rd Quarter
from pyscript import document


lists = {
	"Names A": ["INPUT HERE", "INPUT HERE", "INPUT HERE", "INPUT HERE", "INPUT HERE"],
	"Names B": ["INPUT HERE", "INPUT HERE", "INPUT HERE"],
	"Names C": ["INPUT HERE", "INPUT HERE", "INPUT HERE"],
	"Names D": ["INPUT HERE", "INPUT HERE"],
	"Names E": ["INPUT HERE", "INPUT HERE", "INPUT HERE"],
    "Names F": ["INPUT HERE", "INPUT HERE"],
    "Names G": ["INPUT HERE", "INPUT HERE", "INPUT HERE", "INPUT HERE"],
}

output = document.getElementById("output")
for title, names in lists.items():
    output.innerHTML += f"<h5 class='text-center mb-1'>{title}</h5>"
    for i, name in enumerate(names, 1):
        output.innerHTML += f"{i}. {name}<br>"
    output.innerHTML += "<br>"
