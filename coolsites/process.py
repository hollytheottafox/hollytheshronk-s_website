import sys

def process_file(filename):
    sites = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            if i + 1 < len(lines):
                name = lines[i].strip()
                site = lines[i + 1].strip()
                sites.append((name, site))
    return sites

def print_sites(sites):
    for name, site in sites:
        if site[0] == "-":
            site = site[1:]
        print(f"""
        <a href="https://{site}">
        <div class="card-onehalf">
                <p><big><b>{name}</b></big>
                    {site}
                </p>
            </div>
            </a>
            """)

if __name__ == "__main__":
    filename = sys.argv[1]
    sites = process_file(filename)
    print_sites(sites)