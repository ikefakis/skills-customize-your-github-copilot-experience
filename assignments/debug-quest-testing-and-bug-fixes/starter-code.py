"""Starter code for Debug Quest: Testing and Bug Fixes.

This file contains intentional logic bugs for students to find with tests.
"""


def calculate_score(base_points: int, streak: int, penalty: int) -> int:
    """Calculate the final score for a round.

    Expected behavior (students will test this):
    - Final score = base points + (streak * 10) - penalty
    - Score should never be negative
    """
    score = base_points + (streak * 10) + penalty  # BUG: penalty should be subtracted
    return score


def update_lives(current_lives: int, took_hit: bool) -> int:
    """Update lives after a round.

    Expected behavior:
    - If player took a hit, lives decrease by 1
    - If player did not take a hit, lives stay the same
    - Lives should never be negative
    """
    if took_hit:
        return current_lives + 1  # BUG: should decrease
    return current_lives


def get_rank(score: int) -> str:
    """Return player rank based on score.

    Expected behavior:
    - 0-49: Rookie
    - 50-99: Pro
    - 100+: Legend
    """
    if score >= 100:
        return "Rookie"  # BUG: wrong rank
    if score >= 50:
        return "Legend"  # BUG: wrong rank
    return "Pro"  # BUG: wrong rank


def simulate_round(base_points: int, streak: int, penalty: int, lives: int, took_hit: bool) -> dict:
    """Run one round and return a snapshot of player state."""
    score = calculate_score(base_points, streak, penalty)
    remaining_lives = update_lives(lives, took_hit)
    rank = get_rank(score)

    return {
        "score": score,
        "lives": remaining_lives,
        "rank": rank,
    }


if __name__ == "__main__":
    # Quick manual check (students can adjust values while debugging)
    state = simulate_round(base_points=40, streak=2, penalty=15, lives=3, took_hit=True)
    print("Round summary:", state)