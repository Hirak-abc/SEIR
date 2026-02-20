from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import time


#=================================================================================================================================================
def summon_page(url):
    veil = Options()
    veil.add_argument("--headless")
    veil.add_argument("--disable-gpu")
    veil.add_argument("--no-sandbox")

    summoner = webdriver.Chrome(#to automatically download the correct ChromeDriver version matching the installed Chrome browser
        service=Service(ChromeDriverManager().install()),
        options=veil
    )
 # I initially used a manually downloaded ChromeDriver, but it broke after a Chrome update,
 # so I switched to automatic driver management to always stay compatible.
    summoner.get(url)
    time.sleep(3)
    revealed_script = summoner.page_source
    summoner.quit()
    return revealed_script




def unveil_url(url):#It handles everything after a page is fetched(summoned).
    summoned_script = summon_page(url)
    true_sight = BeautifulSoup(summoned_script, "html.parser")#true_sight converts raw HTML into a form which one can see through and query.

    title = true_sight.title.string.strip() if true_sight.title and true_sight.title.string else ""

    for tag in true_sight(["script", "style"]):
        tag.decompose()

    body = true_sight.get_text(separator=" ", strip=True)

    urls = []
    for a_tag in true_sight.find_all("a", href=True):
        urls.append(urljoin(url, a_tag["href"]))

    return title, body, urls


def count_words(body):
    words = re.findall(r"[A-Za-z0-9]+", body.lower())
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq



#==============================================================================================================================================
def polyhash(word):
    p = 53
    m = 2**64
    h = 0
    power = 1
    for ch in word:
        h = (h + ord(ch) * power) % m
        power = (power * p) % m
    return h


def compute_simhash(freq_map):
    vector = [0] * 64
    for word, weight in freq_map.items():
        h = polyhash(word)
        for i in range(64):
            bit = (h >> i) & 1
            if bit == 1:
                vector[i] += weight
            else:
                vector[i] -= weight
    simhash = 0
    for i in range(64):
        if vector[i] > 0:
            simhash |= (1 << i)

    return simhash


def count_common_bits(h1, h2):
    diff_bits = bin(h1 ^ h2).count("1")#We will use xor 
    return 64 - diff_bits
#===============================================================================================================================================


def main():
    link1 = input("Enter first URL: ").strip()
    link2 = input("Enter second URL: ").strip()

    simhashes = []

    with open("output.txt", "w", encoding="utf-8") as out:
        for index, link in enumerate((link1, link2), start=1):
            title, body, links = unveil_url(link)

            out.write("\n" + "=" * 150 + "\n")
            out.write(f"PAGE {index}\n")
            out.write("=" * 150 + "\n")

            out.write("\nTITLE:\n")
            if title:
                out.write(title + "\n")
            else:
                out.write("[No Title Found]\n")

            out.write("\nBODY:\n")
            if body:
                out.write(body[:1000] + "\n")
            else:
                out.write("[No Text in Body]\n")

            out.write("\nOUTGOING URLS:\n")
            if links:
                for u in links:
                    out.write(u + "\n")
            else:
                out.write("[No Links Found]\n")

            if body:
                freq = count_words(body)
                simhash = compute_simhash(freq)
                simhashes.append(simhash)

            
            #Writing everything to a txt file as terminal stops showing output after a limit.
                out.write("\nWORD FREQUENCIES:\n")
                for w in sorted(freq, key=freq.get, reverse=True)[:]:
                    out.write(f"{w} : {freq[w]}\n")

                out.write("\nSIMHASH:\n")
                out.write(str(simhash) + "\n")
            else:
                out.write("\n[No Words Found-->Its A Void .....]\n")

        # For Final Simhash Comparison
        if len(simhashes) == 2:
            common = count_common_bits(simhashes[0], simhashes[1])
            out.write("\n" + "=" * 100 + "\n")
            out.write("SIMHASH COMPARISON\n")
            out.write("=" * 100 + "\n")
            out.write(f"Common bits between the two pages: {common}\n")


#=======================================================================================================================================================================

if __name__ == "__main__":#To execute main and take input
    main()
