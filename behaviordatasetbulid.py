import pandas as pd
import random
import datetime

# Define psychological state labels and keyword pools for each
psych_labels = ["anxious", "guilt", "dependency", "exhaustion", "reward"]
content_keywords = [
    [  # anxious
        "comedy", "funny", "prank", "fail", "meme", "reaction",
        "rant", "chaos", "drama", "surprise", "fast edit", "parody",
        "gossip", "jump scare", "conflict", "trending", "crazy moment"
    ],
    [  # guilt
        "tutorial", "study", "ai", "education", "how to", "lecture",
        "documentary", "explanation", "productivity", "coding",
        "school hacks", "science", "brain tips", "focus", "note taking",
        "academic", "study vlog", "homework", "exam tips", "online course"
    ],
    [  # dependency
        "romantic", "relationship", "crush", "jealousy", "breakup",
        "texting drama", "true story", "emotional", "affection",
        "therapy", "confession", "cute couple", "toxic love",
        "talking stage", "flirting", "longing", "vulnerability",
        "social circle", "intimacy"
    ],
    [  # exhaustion
        "slow vlog", "minimalism", "lifestyle", "quiet", "healing",
        "deep talk", "well-being", "journaling", "sunset",
        "cooking calmly", "study with me", "life tips", "loneliness",
        "sleep aid", "calm voice", "soft music", "self reflection",
        "mental health", "no drama", "low energy"
    ],
    [  # reward
        "gameplay", "asmr", "sports", "satisfying", "unboxing",
        "pet video", "food review", "travel vlog", "cute animal",
        "music clip", "dancing", "win moment", "hack", "jokes",
        "nice edit", "pop song", "fun fact", "art process",
        "cool trick", "short meme"
    ],
]

# Self-reported user goals
self_goals = [
    "I want to focus on studying",
    "I want to stop wasting time",
    "I just want to relax a bit",
    "I feel tired but want to learn something",
    "I want to stay emotionally balanced"
]

# Generate a single row of simulated user session data
def generate_row(user_id):
    label = random.choice(psych_labels)
    label_index = psych_labels.index(label)

    # Simulate session start time
    session_start = datetime.datetime(2025, 6, 11, random.randint(0, 23), random.randint(0, 59))

    # Determine active period based on hour
    hour = session_start.hour
    if hour < 6:
        period = "late_night"
    elif hour < 12:
        period = "morning"
    elif hour < 18:
        period = "afternoon"
    else:
        period = "night"

    # Generate session and behavior attributes
    session_duration = round(random.uniform(10, 90), 1)
    avg_video_duration = round(random.uniform(10, 60), 1)
    switch_freq = round(random.uniform(0.5, 3.0), 1)
    emotion_score = round(random.uniform(-1.0, 1.0), 2)
    keywords = random.sample(content_keywords[label_index], k=3)  # Randomly select 3 keywords from the label's pool
    repeated_ratio = round(random.uniform(0.0, 0.3), 2)
    skip_ratio = round(random.uniform(0.2, 0.8), 2)
    saved = random.choice([True, False])
    total_watch = round(random.uniform(200.0, 600.0), 1)
    short_ratio = round(random.uniform(0.6, 0.95), 2)
    goal = random.choice(self_goals)

    # Return a complete data row
    return [
        f"U{user_id:03d}",
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

# Define dataset column names
columns = [
    "user_id", "session_start_time", "session_duration_min", "active_period_label",
    "avg_video_duration_sec", "switch_frequency", "content_emotion_score",
    "content_type_keywords", "repeated_viewing_ratio", "skipped_intro_ratio",
    "saved_to_favorites", "3_day_total_watch_time", "short_video_ratio",
    "self_reported_goal", "psych_state_label"
]

# Generate 1000 rows of data
data = [generate_row(i) for i in range(1000)]
df = pd.DataFrame(data, columns=columns)

# Save to CSV file
csv_path = "./Try01/data/short_video_behavior_dataset.csv"
df.to_csv(csv_path, index=False)

