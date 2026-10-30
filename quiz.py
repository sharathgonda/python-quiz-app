import json
import os
import random

LEADERBOARD_FILE = "leaderboard.json"

QUESTIONS = [
    {"question": "Which gate is known as the universal gate?",
     "options": ["AND", "NAND", "XOR", "OR"], "answer": 2},
    {"question": "Which keyword defines a function in Python?",
     "options": ["def", "func", "function", "define"], "answer": 1},
    {"question": "What is decimal 5 in binary?",
     "options": ["101", "110", "111", "100"], "answer": 1},
    {"question": "Which is the unit of frequency?",
     "options": ["Ohm", "Hertz", "Farad", "Henry"], "answer": 2},
    {"question": "Which symbol starts a comment in Python?",
     "options": ["//", "/*", "#", "--"], "answer": 3},
]


def ask_question(q, number):
    print(f"\nQ{number}. {q['question']}")
    for i, option in enumerate(q["options"], start=1):
        print(f"  {i}. {option}")
    while True:
        choice = input("Your answer (1-4): ").strip()
        if choice in ("1", "2", "3", "4"):
            return int(choice) == q["answer"]
        print("Please enter a number between 1 and 4.")


def run_quiz():
    questions = QUESTIONS.copy()
    random.shuffle(questions)
    score = 0
    for number, q in enumerate(questions, start=1):
        if ask_question(q, number):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. Correct answer: {q['options'][q['answer'] - 1]}")
    print(f"\nYou scored {score}/{len(questions)}")
    return score, len(questions)


def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    with open(LEADERBOARD_FILE, "r") as f:
        return json.load(f)


def save_score(name, score, total):
    board = load_leaderboard()
    board.append({"name": name, "score": score, "total": total})
    board.sort(key=lambda e: e["score"], reverse=True)
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(board, f, indent=2)


def show_leaderboard():
    board = load_leaderboard()
    if not board:
        print("\nNo scores yet.")
        return
    print("\n--- LEADERBOARD (Top 10) ---")
    for rank, e in enumerate(board[:10], start=1):
        print(f"{rank}. {e['name']} - {e['score']}/{e['total']}")


def main():
    while True:
        print("\n=== QUIZ APP ===")
        print("1. Start quiz")
        print("2. View leaderboard")
        print("3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            name = input("Enter your name: ").strip() or "Player"
            score, total = run_quiz()
            save_score(name, score, total)
        elif choice == "2":
            show_leaderboard()
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()