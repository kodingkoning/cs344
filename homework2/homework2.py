# CS 344 Homework 2
# Elizabeth Koning

# Problem 1
print("Problem 1")
# TODO

spam_corpus = [["i", "am", "spam", "spam", "i", "am"], ["i", "do", "not", "like", "that", "spamiam"]]
ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]

min_threshold = 1
unseen_prob = 0.4


class SpamFilter:

    def __init__(self, spam, not_spam):
        # number of messages in each corpus
        self.ngood = len(not_spam)
        self.nbad  = len(spam)

        # flatten lists
        spam = sum(spam, [])
        not_spam = sum(not_spam, [])

        # list of words in either corpus
        keys = list( set(spam) | set(not_spam) ) # union of key lists

        # store counts of tokens in each list
        self.spam = {token:spam.count(token) for token in keys}
        self.not_spam = {token:not_spam.count(token) for token in keys}

        # third hash table -- probability that message containing word is spam
        self.probs = {}
        for token in keys:
            g = float(2 * self.not_spam[token])
            b = float(self.spam[token])
            if g + b > min_threshold:
                self.probs[token] = max(0.01, min(0.99, min(1.0, b/self.nbad) / (min(1.0, g/self.ngood) + min(1.0, b/self.nbad))))

        print("Dictionary")
        print(self.probs, '\n')

    def filter(self, text):
        product = 1.0
        comp_product = 1.0

        for token in text:
            if token in self.probs:
                probability = self.probs[token]
            else:
                probability = unseen_prob
            product *= probability
            comp_product *= (1.0 - probability)

        print(text, product / (product + comp_product))

        return product / (product + comp_product)


spam_filter = SpamFilter(spam_corpus, ham_corpus)

# examples
print("Examples")
print(spam_filter.filter(["i"])) # single word
print(spam_filter.filter(["blah"])) # single word not in corpuses
print(spam_filter.filter(["spamiam", "am"]))
print(spam_filter.filter(["i", "blah"]))
print(spam_filter.filter(["i", "am"]))
print(spam_filter.filter(["i", "do"])) # ham list
print(spam_filter.filter(["i", "am", "spam", "spam", "i", "am"])) # spam list
print(spam_filter.filter(["do", "i", "like", "green", "eggs", "and", "ham"])) # ham list
print(spam_filter.filter(["i", "do", "not", "like", "that", "spamiam"]))


# Problem 2a
# TODO: copy into Jupyter notebook

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

grass = BayesNet([
    ('Cloudy', '', 0.5),
    ('Sprinkler', 'Cloudy', {T:0.1, F:0.5}),
    ('Rain', 'Cloudy', {T:0.8, F:0.2}),
    ('WetGrass', 'Sprinkler Rain', {(T, T):0.99, (T,F):0.9, (F,T):0.9, (F,F):0.0}),
    ])

print("\n\nProblem 2")
print("i. " + enumeration_ask('Cloudy', dict(), grass).show_approx())

print("ii. " + enumeration_ask('Sprinkler', dict(Cloudy=T), grass).show_approx())

print("iii. " + enumeration_ask('Cloudy', dict(Sprinkler=T, Rain=F), grass).show_approx())

print("iv. " + enumeration_ask('WetGrass', dict(Cloudy=T, Sprinkler=T, Rain=T), grass).show_approx())

print("v. " + enumeration_ask('Cloudy', dict(WetGrass=F), grass).show_approx())
