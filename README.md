# The Mood Machine

The Mood Machine is a simple text classifier that begins with a rule based approach and can optionally be extended with a small machine learning model. It tries to guess whether a short piece of text sounds **positive**, **negative**, **neutral**, or even **mixed** based on patterns in your data.

This lab gives you hands on experience with how basic systems work, where they break, and how different modeling choices affect fairness and accuracy. You will edit code, add data, run experiments, and write a short model card reflection.

---

## Repo Structure

```plaintext
├── dataset.py         # Starter word lists and example posts (you will expand these)
├── mood_analyzer.py   # Rule based classifier with TODOs to improve
├── main.py            # Runs the rule based model and interactive demo
├── ml_experiments.py  # (New) A tiny ML classifier using scikit-learn
├── model_card.md      # Template to fill out after experimenting
└── requirements.txt   # Dependencies for optional ML exploration
```

---

## Getting Started

1. Open this folder in VS Code.
2. Make sure your Python environment is active.
3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the rule-based starter:

    ```bash
    python main.py
    ```

If pieces of the analyzer are not implemented yet, you will see helpful errors that guide you to the TODOs.

To try the ML model later, run:

```bash
python ml_experiments.py
```

---

## What You Will Do

During this lab you will:

- Implement the missing parts of the rule based `MoodAnalyzer`.
- Add new positive and negative words.
- Expand the dataset with more posts, including slang, emojis, sarcasm, or mixed emotions.
- Observe unusual or incorrect predictions and think about why they happen.
- Train a tiny machine learning model and compare its behavior to your rule based system.
- Complete the model card with your findings about data, behavior, limitations, and improvements.
- The goal is to help you reason about how models behave, how data shapes them, and why even small design choices matter.

---

## Tips

- Start with preprocessing before updating scoring rules.
- When debugging, print tokens, scores, or intermediate choices.
- Ask an AI assistant to help create edge case posts or unusual wording.
- Try examples that mislead or confuse your model. Failure cases teach you the most.

---

## Instructor Summary

The core concept students need to understand is that rule-based classifiers are only as good as the rules and data behind them — the model does not "understand" language, it just pattern-matches against word lists, so its behavior is fully determined by those design choices. Students most commonly struggle with negation logic ("not happy" should score negative, not positive) and with sarcasm, where the literal words contradict the intended meaning and no rule-based system handles it cleanly. AI assistants are genuinely helpful for generating diverse test posts, suggesting slang or emoji examples, and explaining why a score came out a certain way — but they can mislead students into copying word lists or threshold values without understanding why, which undercuts the lab's goal of building that intuition from scratch. AI also tends to overexplain negation handling in ways that skip the student's own discovery moment. To guide a stuck student without giving the answer, ask: "Print out the tokens your model sees for that sentence — do any of them appear in your positive or negative word lists?" That one question usually surfaces whether the issue is preprocessing, missing vocabulary, or a negation window problem, and lets the student diagnose it themselves.
