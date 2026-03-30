"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    # user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    user_profiles = [
    {"genre": "pop", "mood": "happy", "energy": 0.9},       # High-Energy Pop
    {"genre": "lofi", "mood": "chill", "energy": 0.3},      # Chill Lofi
    {"genre": "rock", "mood": "intense", "energy": 0.8},    # Deep Intense Rock
    ]
    
    # recommendations = recommend_songs(user_prefs, songs, k=5)

    for idx, profile in enumerate(user_profiles, start=1):
        print(f"\n=== Recommendations for Profile {idx} ===")
        print(f"Profile: Genre={profile['genre']}, Mood={profile['mood']}, Energy={profile['energy']}\n")
        
        recommendations = recommend_songs(profile, songs, k=5)

    # print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} by {song['artist']}")
        print(f"Score: {score:.2f}")
        print(f"Why: {explanation}")
        print("-" * 40)


if __name__ == "__main__":
    main()
