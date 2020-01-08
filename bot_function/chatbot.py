import nltk
import json
import numpy
import tensorflow
import tflearn
import random
import pickle
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()


def chat(var):
    with open("bot_function/intents.json") as file:
        data = json.load(file)

    with open("bot_data/data.pickle", "rb") as f:
            words, labels, training, output = pickle.load(f)

    tensorflow.reset_default_graph()

    net = tflearn.input_data(shape=[None, len(training[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
    net = tflearn.regression(net)

    model = tflearn.DNN(net)
    model.load("bot_data/model.tflearn")

    def bag_of_words(s, words):
        bag = [0 for _ in range(len(words))]
        s_words = nltk.word_tokenize(s)
        s_words = [stemmer.stem(word.lower()) for word in s_words]

        for se in s_words:
            for i, w in enumerate(words):
                if w == se:
                    bag[i] = (1)

        return numpy.array(bag)

    result = model.predict([bag_of_words(var, words)])[0]
    result_index = numpy.argmax(result)
    tag = labels[result_index]

    if result[result_index] > 0.7:
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
        return random.choice(responses)
    else:
        return "I didn't get that.. Try again!"

