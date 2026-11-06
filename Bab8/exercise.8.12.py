def make_sandwich(*items):
    """Print a summary of the sandwich that is being ordered."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")


make_sandwich('tuna')
make_sandwich('chicken', 'lettuce', 'tomato')
make_sandwich('beef', 'cheese', 'onion', 'mayonnaise')