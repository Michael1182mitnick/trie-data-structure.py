# Create a Trie data structure to store a list of strings. Implement functions to insert a word, search for a word, and check for prefix matches.

class TrieNode:
    """A node in the Trie."""

    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False  # True if the node represents the end of a word


class Trie:
    def __init__(self):
        """Initialize the Trie with an empty root node."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word into the Trie."""
        current = self.root
        for char in word:
            # If the character is not present, add a new node
            if char not in current.children:
                current.children[char] = TrieNode()
            # Move to the next node
            current = current.children[char]
        # Mark the end of the word
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Search for a word in the Trie. Returns True if the word exists, False otherwise."""
        current = self.root
        for char in word:
            # If the character is not present, return False
            if char not in current.children:
                return False
            # Move to the next node
            current = current.children[char]
        # Return True if it's the end of a word
        return current.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """Check if there is any word in the Trie that starts with the given prefix."""
        current = self.root
        for char in prefix:
            # If the character is not present, return False
            if char not in current.children:
                return False
            # Move to the next node
            current = current.children[char]
        return True


# Example usage
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # Returns True
print(trie.search("app"))    # Returns False
print(trie.starts_with("app"))  # Returns True
trie.insert("app")
print(trie.search("app"))    # Returns True
