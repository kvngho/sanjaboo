from keras.models import Model
from keras import layers
from keras import Input

text_vocabulary_size = 10000
question_vocabulary_size = 10000
answer_vocabulary_size = 500

text_input = Input(shape=(None, ), dtype='int32', name='text')
embedded_text = layers.Embedding(text_vocabulary_size, 64)(text_input)
encoded_text = layers.LSTM(32)(embedded_text)


question_input = Input(shape=(None, ), dtype='int32', name='question')
embedded_question = layers.Embedding(question_vocabulary_size, 64)(question_input)
encoded_question = layers.LSTM(32)(embedded_question)
encoded_question = layers.LSTM(32)(embedded_question)

concatenated = layers.concatenate([encoded_text, encoded_question])


answer = layers.Dense(answer_vocabulary_size, activation='softmax')(concatenated)


model = Model([text_input, question_input], answer)
model.complie(optimizer='rmsprop',loss='categorical_crossentropy',metricss=['acc'])

class IntergratedModel:
    def __init__(self):
        pass