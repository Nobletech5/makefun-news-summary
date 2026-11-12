"""make.fun news-summary-01 entry: writes the 11 Nov 2026 world-news summary."""
import os

SUMMARY = "World news, Wednesday 11 November 2026.\n\nMarco Rubio said in Paris that economic pressure was working so well no major combat operations were needed for now, though force remained possible if Iran crossed red lines. Tehran's security chief said Iran was still waiting for a US answer to its seven conditions, and Hormuz would stay shut until they were met. Iran's top negotiator said the strait would never return to its pre-war state. Iranian media said two tankers caught fire after hitting naval mines, and US forces disabled a cargo ship breaching the blockade.\n\nTwo days of Ukraine-Russia-US talks in Abu Dhabi ended with no ceasefire but a large prisoner exchange agreed, called the biggest release of the war by US envoy Jared Kushner. NATO jets scrambled after drones strayed into Baltic airspace during Ukrainian strikes on Russia.\n\nCongo confirmed 11,042 Ebola cases and 5,387 deaths, its deadliest outbreak, now in eight of 26 provinces.\n\nAt COP31 in Antalya, UN chief Antonio Guterres warned the slow climate response had put the world on a path to destruction. Nigeria backed a plan to double homes with rooftop solar by 2030.\n\nIn Washington, the House voted 211-204 to send the impeachment resolution against Defence Secretary Pete Hegseth to committee, effectively killing it; Republicans elected Jim Jordan as House leader. The Justice Department charged three Iran-backed operatives over nearly 20 alleged plots in the US and Europe, including one at RAF Fairford, and Treasury Secretary Scott Bessent moved to a military base after threats.\n\nNvidia rose 2.9% to $173.73, then fell about 8% after hours as its board met on CEO Jensen Huang's future after reports of a second affair. A three-storey building collapsed in Brooklyn, killing at least two and injuring more than a dozen. A US Army officer was arrested in Britain on suspicion of spying for Russia, Israel's new parliament was sworn in with no government yet, and Delhi's air stayed poor at 299 after Diwali."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SUMMARY.rstrip("\n") + "\n")

if __name__ == "__main__":
    main()
