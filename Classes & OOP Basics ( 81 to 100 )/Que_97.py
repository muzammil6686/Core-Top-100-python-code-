class Hadith_book:
    hadith_list = [
    "Actions are judged by intentions.",
    "A Muslim is one from whose tongue and hands others are safe.",
    "Cleanliness is half of faith.",
    "Make things easy, do not make them difficult.",
    "He who does not show mercy will not be shown mercy.",
    "The best among you are those who are most beneficial to others.",
    "Seeking knowledge is an obligation upon every Muslim.",
    "Whoever gives up lying will enter Paradise.",
    "Charity is obligatory upon every Muslim.",
    "Allah loves gentleness in all matters.",
    "He who does not respect elders is not one of us.",
    "Smiling at your brother is charity.",
    "Prayer is the pillar of religion.",
    "Whoever fasts, Allah forgives his sins.",
    "The best of you is the one who is best to his family.",
    "Do not get angry.",
    "Whoever forgives, Allah elevates him.",
    "Faith is in the heart, not just on the tongue.",
    "Breaking promises is a sign of hypocrisy.",
    "The most beloved deeds to Allah are those done consistently, even if small."
]

    def get_hadith(self, index):
        if 0 <= index < len(self.hadith_list):
            print(self.hadith_list[index])
        
