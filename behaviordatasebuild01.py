import pandas as pd
import random
import datetime

# Alternate psychological states (same labels, but varied context)
psych_labels = ["anxious", "guilt", "dependency", "exhaustion", "reward"]

# Alternative and unrelated keyword sets for diversity
alt_keywords = {
    "anxious": [
        "stock crash", "job loss", "climate news", "dystopia", "anxiety tips", "bad news", 
        "market panic", "war update", "interview fail", "disaster", "recession", "health scare"
    ],
    "guilt": [
        "missed deadline", "regret", "cheat story", "failed test", "overspending", "wasted time",
        "ignored calls", "late work", "bad habit", "procrastination", "poor grades", "missed goal"
    ],
    "dependency": [
        "daily routine", "coffee addiction", "always online", "check notifications", "fear of missing out", 
        "compulsive scrolling", "digital cling", "sleep with phone", "can't stop", "constant refresh"
    ],
    "exhaustion": [
        "long work hours", "burnout symptoms", "overwork", "no sleep", "crash nap", "work stress",
        "fatigue", "stretch break", "mental drain", "power nap", "digital fatigue", "overstimulated"
    ],
    "reward": [
        "win prize", "bonus drop", "good news", "celebration", "funny fail", "surprise box",
        "birthday cake", "positive feedback", "unexpected win", "congrats", "happy ending", "meme gold"
    ]
}

# Self-goals for variation (can include overlaps)
alt_goals = {
    "anxious": ["I want to feel safe again", "I need to relax my mind"],
    "guilt": ["I wish I had used time better", "I want to be more productive"],
    "dependency": ["I want to take control of my habits", "I want to be more independent"],
    "exhaustion": ["I need rest", "I want better balance"],
    "reward": ["I deserve this joy", "I want to enjoy the moment"]
}

# Row generator with alternative data
def generate_alt_row(user_id):
    label = random.choice(psych_labels)
    session_start = datetime.datetime(2025, 6, 12, random.randint(0, 23), random.randint(0, 59))

    hour = session_start.hour
    if hour < 6:
        period = "late_night"
    elif hour < 12:
        period = "morning"
    elif hour < 18:
        period = "afternoon"
    else:
        period = "night"

    session_duration = round(random.uniform(8, 85), 1)
    avg_video_duration = round(random.uniform(5, 70), 1)
    switch_freq = round(random.uniform(0.3, 3.5), 1)
    emotion_score = round(random.uniform(-1.0, 1.0), 2)
    keywords = random.sample(alt_keywords[label], k=3)
    repeated_ratio = round(random.uniform(0.0, 0.4), 2)
    skip_ratio = round(random.uniform(0.1, 0.9), 2)
    saved = random.choice([True, False])
    total_watch = round(random.uniform(180.0, 700.0), 1)
    short_ratio = round(random.uniform(0.55, 0.98), 2)
    goal = random.choice(alt_goals[label])

    return [
        f"U_ALT{user_id:03d}",
        session_start.strftime("%Y-%m-%d %H:%M:%S"),
        session_duration,
        period,
        avg_video_duration,
        switch_freq,
        emotion_score,
        keywords,
        repeated_ratio,
        skip_ratio,
        saved,
        total_watch,
        short_ratio,
        goal,
        label
    ]

# Column headers (same as before)
columns = [
    "user_id", "session_start_time", "session_duration_min", "active_period_label",
    "avg_video_duration_sec", "switch_frequency", "content_emotion_score",
    "content_type_keywords", "repeated_viewing_ratio", "skipped_intro_ratio",
    "saved_to_favorites", "3_day_total_watch_time", "short_video_ratio",
    "self_reported_goal", "psych_state_label"
]

# Generate 1000 more diverse rows
alt_data = [generate_alt_row(i) for i in range(1000)]
alt_df = pd.DataFrame(alt_data, columns=columns)

# Save to CSV
alt_csv_path = "./Try01/data/alt_diverse_video_behavior_dataset01.csv"
alt_df.to_csv(alt_csv_path, index=False)

