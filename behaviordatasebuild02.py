import pandas as pd
import random
import datetime

# Alternate psychological states (same labels, but varied context)
psych_labels = ["anxious", "guilt", "dependency", "exhaustion", "reward"]

third_keywords = {
    "anxious": [
        "dark theory", "scary fact", "paranoia news", "emergency warning", "danger trend", 
        "fear trigger", "stressful scene", "horror edit", "breaking alert", "crisis footage"
    ],
    "guilt": [
        "missed opportunity", "could’ve done better", "regret stories", "bad ending", 
        "shame reel", "embarrassing fail", "loss highlight", "responsibility talk", 
        "disappointing moment", "guilt meme"
    ],
    "dependency": [
        "loop habit", "endless scroll", "daily addiction", "check phone", "wifi need", 
        "can't stop watching", "autoplay trap", "routine doom", "FOMO wave", "habitual checking"
    ],
    "exhaustion": [
        "napping cat", "work burnout", "eye strain", "fatigue diary", "heavy brain", 
        "overstim edit", "crash reel", "sleep vlog", "zoning out", "overload speech"
    ],
    "reward": [
        "motivation win", "proud moment", "finally success", "feel good story", 
        "happy scream", "goal achieved", "celebration edit", "fun time", 
        "reward day", "thankful post"
    ]
}

third_goals = {
    "anxious": ["I want to slow down my mind", "I feel overwhelmed by bad content"],
    "guilt": ["I want to turn regret into action", "I hope to make better choices"],
    "dependency": ["I want to gain control of my scrolling", "I want to reduce my reliance on content"],
    "exhaustion": ["I need more mental rest", "I feel drained and need space"],
    "reward": ["I want to reward myself with positivity", "I deserve to celebrate"]
}

# Generator for third variation
def generate_third_row(user_id):
    label = random.choice(psych_labels)
    session_start = datetime.datetime(2025, 6, 13, random.randint(0, 23), random.randint(0, 59))

    hour = session_start.hour
    if hour < 6:
        period = "late_night"
    elif hour < 12:
        period = "morning"
    elif hour < 18:
        period = "afternoon"
    else:
        period = "night"

    session_duration = round(random.uniform(8, 100), 1)
    avg_video_duration = round(random.uniform(5, 75), 1)
    switch_freq = round(random.uniform(0.4, 3.8), 1)
    emotion_score = round(random.uniform(-1.0, 1.0), 2)
    keywords = random.sample(third_keywords[label], k=3)
    repeated_ratio = round(random.uniform(0.0, 0.4), 2)
    skip_ratio = round(random.uniform(0.15, 0.9), 2)
    saved = random.choice([True, False])
    total_watch = round(random.uniform(150.0, 750.0), 1)
    short_ratio = round(random.uniform(0.5, 0.98), 2)
    goal = random.choice(third_goals[label])

    return [
        f"U_THIRD{user_id:03d}",
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

# Generate third dataset
third_data = [generate_third_row(i) for i in range(1000)]
third_df = pd.DataFrame(third_data, columns=columns)

# Save to CSV
third_csv_path = "./Try01/data/third_diverse_video_behavior_dataset02.csv"
third_df.to_csv(third_csv_path, index=False)

third_csv_path
