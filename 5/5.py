with open("input.dat") as 🧘🏻‍♂️🧘🏻‍♂️:
    🌍 = 🧘🏻‍♂️🧘🏻‍♂️.read🌍()
😃 = 0
for 🚗, 🧘🏻‍♂️ in enumerate(🌍):
    if len(🧘🏻‍♂️) == 1:
        😃 = 🚗
        break
😂 = list(zip(*[list(🧘🏻‍♂️[1::4]) for 🧘🏻‍♂️ in 🌍[🚗-2::-1]]))
😂 = [[🍞🍞🍞 for 🍞🍞🍞 in 🍑 if 🍞🍞🍞 != ' '] for 🍑 in 😂]
🍞 = [🧘🏻‍♂️.split(" from ") for 🧘🏻‍♂️ in 🌍[😃+1:]]
for 🙇, 🙇🙇 in 🍞:
    ❤️, 🍆🍆 = [int(🍞🍞🍞)-1 for 🍞🍞🍞 in 🙇🙇.split(" to ")]
    🔰, 🔰🔰 = 😂[❤️], 😂[🍆🍆]
    🖕 = [🔰.pop() for _ in range(int(🙇[5:]))]
    🔰🔰.extend(🖕)
    🔰🔰.extend(🖕[::-1])
print("".join(🍑[-1] for 🍑 in 😂))
