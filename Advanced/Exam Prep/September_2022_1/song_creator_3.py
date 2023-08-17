
def add_songs(*args):
    result = {} # title : [ lirics]
    for i in args:
        song_title = i[0]
        sont_lyrics = i[1]
        if not song_title in result.keys():
            result[song_title] = sont_lyrics
            continue
        result[song_title] += sont_lyrics

    total = ""
    for key,value in result.items():
        total+= f"- {key}\n"
        if not value:
            continue
        total += '\n'.join(value)+"\n"
    return total


print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))

import unittest


class Tests(unittest.TestCase):
    def test(self):
        result = add_songs(
            ("Love of my life",
             ["Love of my life, you've hurt me",
              "You've broken my heart, and now you leave me",
              "Love of my life, can't you see?",
              "Bring it back, bring it back"]),
            ("Beat It", []),
            ("Love of my life",
             ["Don't take it away from me",
              "Because you don't know",
              "What it means to me"]),
            ("Dream On",
             ["Every time that I look in the mirror"]),
        )

        self.assertEqual(result.strip(), """- Love of my life
Love of my life, you've hurt me
You've broken my heart, and now you leave me
Love of my life, can't you see?
Bring it back, bring it back
Don't take it away from me
Because you don't know
What it means to me
- Beat It
- Dream On
Every time that I look in the mirror""")


if __name__ == "__main__":
    unittest.main()