"""Module implementing Bob's response logic."""
def response(hey_bob):
    """Determine what Bob will reply to someone when they say something to him or ask him a question"""
    text = hey_bob
    if text.strip() == "":
        return "Fine. Be that way!"
    if text.strip().endswith("?") and text.isupper():
        return "Calm down, I know what I'm doing!"
    if text.isupper():
        return "Whoa, chill out!"
    if text.strip().endswith("?"):
        return "Sure."
    return "Whatever."
    