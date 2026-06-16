from collections import Counter

def parseInput(filename: str) -> list[str]:
    with open(filename) as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def getHandStrength(hand: str) -> int:
    counts = Counter(hand)
    joker_count = counts.pop('J', 0)
    if joker_count == 5:
        return 7

    most_common_card = counts.most_common(1)[0][0]
    counts[most_common_card] += joker_count

    frequencies = sorted(counts.values(), reverse=True)
    if frequencies == [5]: return 7
    if frequencies == [4, 1]: return 6
    if frequencies == [3, 2]: return 5
    if frequencies == [3, 1, 1]: return 4
    if frequencies == [2, 2, 1]: return 3
    if frequencies == [2, 1, 1, 1]: return 2
    return 1

def getCardValues(hand: str) -> list[int]:
    card_map = {
        'A': 13, 'K': 12, 'Q': 11, 'T': 10,
        '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 
        'J': 1
    }
    return list(card_map[card] for card in hand)

def getRank(lines: list[str]) -> int:
    processed_hands = []
    for line in lines:
        hand, bid_str = line.split()
        bid = int(bid_str)
        sort_key = (getHandStrength(hand), *getCardValues(hand))
        processed_hands.append((sort_key, bid))

    processed_hands.sort(key=lambda x: x[0])
    total_winnings = 0
    for rank, (sort_key, bid) in enumerate(processed_hands, start=1):
        total_winnings += rank * bid
    return total_winnings

lines = parseInput('../inputs/input7.txt')
print(f"New total winnings: {getRank(lines)}")