def scentence_maker(phrase):
    interrogatives = ("How", "What", "Why", "When", "Where",
                      "how", "what", "why", "when", "where")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


results = []
while True:
    ip = input("Say something: ")
    if ip == "\end":
        break
    else:
        results.append(scentence_maker(ip))

print(" ".join(results))
