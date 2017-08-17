import numpy as np
import tensorflow as tf

class CropClassifier:

    def __init__(self):

        modelPath = "./model-It88250-Acc98"

        self.sess = tf.Session()

        saver = tf.train.import_meta_graph(modelPath + "/model.ckpt.meta")
        saver.restore(self.sess, modelPath + "/model.ckpt")
        #saver.restore(self.sess, tf.train.latest_checkpoint('./model-It4587-Acc90'))

        graph = tf.get_default_graph()
        self.y_conv = graph.get_tensor_by_name("softmax/y_conv:0")
        self.softmax = tf.nn.softmax(self.y_conv)
        print("Model Loaded")

    def getCropClass(self, data):

        val = np.array([data], dtype=float)

        feed_dict = {"x:0": val}
        result = self.sess.run(self.softmax, feed_dict)

        prediction = result[0,0]

        answer = True
        if (prediction < 0.51):
            answer = False

        #good = 0
        #bad = 1
        return answer
