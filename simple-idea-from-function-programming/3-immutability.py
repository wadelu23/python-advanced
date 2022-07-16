from datetime import datetime
from functools import partial
from typing import Callable
import random


# Use immutability to your advantage

def main() -> None:
    test_list = [120, 68, -20, 0, 5, 67, 14, 99]

    # built in immutable sort
    sorted_list = sorted(test_list) # Tuple is also workable because it is Iterable.
    print(f"Original list: {test_list}")
    print(f"Sorted list: {sorted_list}")

    # built in mutable sort
    test_list.sort() # Tuple is not workable here
    print(f"Original list: {test_list}")

    # other example of mutable vs immutable operations
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    shuffled_cards = random.sample(cards, k=len(cards)) # Require Sequence, so Tuple is also workable.
    print(f"Shuffled cards: {shuffled_cards}")
    print(f"Original cards: {cards}")

    random.shuffle(cards)  # shuffles the cards (mutable)
    # Require MutableSequence, so Tuple is not workable here.
    print(f"Cards: {cards}")


if __name__ == "__main__":
    main()
