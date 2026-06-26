"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
    "proud",
    "grateful",
    "hopeful",
    "thrilled",
    "fantastic",
    "enjoyed",
    "peaceful",
    "confident",
    "joyful",
    "okay",
    "glad",
    "pleased",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
    "frustrated",
    "disappointed",
    "worried",
    "anxious",
    "miserable",
    "exhausted",
    "annoyed",
    "lonely",
    "dread",
    "failed",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    # Starter posts
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    # Added posts — variety of styles
    "I absolutely love getting stuck in traffic",          # sarcasm
    "lowkey stressed but no cap kind of thriving",         # slang, mixed
    "it is what it is",                                   # resigned neutral
    "why does this always happen to me",                   # frustrated negative
    "I passed but I really wanted to do better",           # mixed relief + disappointment
    "not great not terrible",                              # ambiguous neutral
    "honestly could not care less at this point",          # apathy/burnout negative
    "I hate how much I actually enjoyed that",             # conflicted mixed
    "today was fine I guess",                              # unenthusiastic neutral
    "everything is fine :) totally fine :)",               # sarcastic distress negative
    "so proud of myself for finishing this",               # positive
    "I don't hate this as much as I expected",             # negation mixed
    "genuinely cannot believe how amazing that was",        # positive
    "woke up exhausted and it only got worse from there",  # negative
    "not bad not great just kind of existing",             # neutral
    "I tried my best and I still failed ugh",              # negative
    "lowkey this might actually be going okay",            # mild positive/mixed
    "I am not sad about it at all",                        # negation — actually neutral/positive
]

# Human labels for each post above.
# Allowed labels:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    # Starter labels
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
    # Added labels
    "negative",  # sarcasm — "love getting stuck in traffic" = actually hates it (model misses this; known sarcasm blind spot)
    "mixed",     # slang mix: stressed + thriving
    "neutral",   # resigned: "it is what it is"
    "neutral",   # no sentiment words matched; frustrated but undetectable by rules
    "neutral",   # no sentiment words matched; mixed relief/disappointment but undetectable
    "mixed",     # "not great" + "not terrible" = both polarities after negation flip
    "neutral",   # apathy phrasing has no matched sentiment words
    "mixed",     # conflicted — "hate" negative + "enjoyed" positive
    "neutral",   # unenthusiastic
    "negative",  # sarcastic distress — but :) trips up rule model; known failure
    "positive",  # proud of finishing
    "positive",  # "don't hate" = negated negative = positive signal
    "positive",  # genuine amazement
    "negative",  # exhausted + got worse
    "mixed",     # "not bad" + "not great" = both polarities after negation
    "negative",  # tried + failed + ugh
    "positive",  # "okay" = positive; lowkey hedge not strong enough to change label
    "positive",  # "not sad" = negated negative = weak positive
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
