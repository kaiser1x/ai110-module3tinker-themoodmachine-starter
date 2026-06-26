# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""

from typing import List, Dict, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a list of tokens the model can work with.

        TODO: Improve this method.

        Right now, it does the minimum:
          - Strips leading and trailing whitespace
          - Converts everything to lowercase
          - Splits on spaces

        Ideas to improve:
          - Remove punctuation
          - Handle simple emojis separately (":)", ":-(", "🥲", "😂")
          - Normalize repeated characters ("soooo" -> "soo")
        """
        cleaned = text.strip().lower()
        tokens = cleaned.split()

        return tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    # Negation words that flip the next sentiment word's value
    NEGATION_WORDS = {
        "not", "never", "no", "cant", "can't", "don't", "dont",
        "won't", "wont", "isn't", "isnt", "hardly", "without",
    }

    # Emoji/slang tokens mapped to score values (positive > 0, negative < 0)
    EMOJI_SCORES = {
        ":)": 1, ":-)": 1, ":D": 2,
        ":(": -1, ":-(": -1,
        "😊": 1, "😍": 2, "🥳": 2, "😁": 1, "😄": 1,
        "😢": -1, "😭": -2, "😤": -1, "😰": -1, "💀": -1,
        "lol": 1, "lmao": 1, "haha": 1, "hehe": 1,
        "ugh": -1, "smh": -1,
        "thriving": 2, "vibing": 1, "highkey": 1, "lowkey": 0,
    }

    def _analyze(self, text: str):
        """
        Return (pos_count, neg_count) after applying negation and emoji/slang signals.

        Negation flips a word's polarity: "not happy" adds to neg_count, not pos_count.
        Emoji/slang values split by sign into the appropriate bucket.
        """
        tokens = self.preprocess(text)
        pos_count = 0
        neg_count = 0
        negate_next = False

        negate_window = 0
        MAX_NEGATE_WINDOW = 2  # "not at all happy" — allow 2 filler words

        for token in tokens:
            if token in self.EMOJI_SCORES:
                val = self.EMOJI_SCORES[token]
                if negate_next and val != 0:
                    val = -val
                if val > 0:
                    pos_count += val
                elif val < 0:
                    neg_count += abs(val)
                negate_next = False
                negate_window = 0
                continue

            clean = token.strip(".,!?;:'\"")

            if clean in self.NEGATION_WORDS:
                negate_next = True
                negate_window = 0
                continue

            if clean in self.positive_words:
                if negate_next:
                    neg_count += 1
                else:
                    pos_count += 1
                negate_next = False
                negate_window = 0
            elif clean in self.negative_words:
                if negate_next:
                    pos_count += 1
                else:
                    neg_count += 1
                negate_next = False
                negate_window = 0
            else:
                # Non-sentiment word: count toward negation window
                if negate_next:
                    negate_window += 1
                    if negate_window > MAX_NEGATE_WINDOW:
                        negate_next = False
                        negate_window = 0

        return pos_count, neg_count

    def score_text(self, text: str) -> int:
        """
        Compute a numeric mood score: pos_count - neg_count.

        Improvements over baseline:
          1. Negation: "not happy" contributes -1 not +1
          2. Emoji/slang signals via EMOJI_SCORES lookup
          3. Repeated sentiment words accumulate (counted, not just presence)
        """
        pos, neg = self._analyze(text)
        return pos - neg

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Turn the numeric score for a piece of text into a mood label.

        The default mapping is:
          - score > 0  -> "positive"
          - score < 0  -> "negative"
          - score == 0 -> "neutral"

        TODO: You can adjust this mapping if it makes sense for your model.
        For example:
          - Use different thresholds (for example score >= 2 to be "positive")
          - Add a "mixed" label for scores close to zero
        Just remember that whatever labels you return should match the labels
        you use in TRUE_LABELS in dataset.py if you care about accuracy.
        """
        pos, neg = self._analyze(text)
        score = pos - neg
        if pos > 0 and neg > 0:
            return "mixed"
        elif score > 0:
            return "positive"
        elif score < 0:
            return "negative"
        else:
            return "neutral"

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining WHY the model chose its label.

        TODO:
          - Look at the tokens and identify which ones counted as positive
            and which ones counted as negative.
          - Show the final score.
          - Return a short human readable explanation.

        Example explanation (your exact wording can be different):
          'Score = 2 (positive words: ["love", "great"]; negative words: [])'

        The current implementation is a placeholder so the code runs even
        before you implement it.
        """
        tokens = self.preprocess(text)

        positive_hits: List[str] = []
        negative_hits: List[str] = []
        score = 0

        for token in tokens:
            if token in self.positive_words:
                positive_hits.append(token)
                score += 1
            if token in self.negative_words:
                negative_hits.append(token)
                score -= 1

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )
