import cv2
import easyocr
import numpy as np
import requests


class Crawler:

    def __init__(self):
        self.reader = easyocr.Reader(["fr"])

    def process(self, url, mode):
        response = requests.get(url)
        img_original = response.content
        img_as_np = np.frombuffer(img_original, dtype=np.uint8)
        raw_img = cv2.imdecode(img_as_np, flags=1)

        # get image dimension
        dim = raw_img.shape

        # crop ROI
        y0, y1, x0, x1 = int(dim[0] * 0.175), int(dim[0]
                                                  * 0.85), int(dim[1] * 0.196), int(dim[1] * 0.365)
        cropped_img = raw_img[y0:y1, x0:x1]

        # run text recognition
        result = self.reader.readtext(cropped_img, paragraph=False)

        # process results
        results = [(res[1], res[0][0][1]) for res in result]

        results = sorted(results, key=lambda res: res[1])

        _results = results
        for i in range(len(results) - 2):
            if abs(results[i][1] - results[i + 1][1]) <= 5:
                _results[i] = (_results[i][0] + "-" + _results[i+1][0], 0)
                _results.remove(results[i+1])

        results = [res[0] for res in _results]

        # filter perco or prisme
        participants = filter(lambda res: "'" not in res and "Do" not in res and "Prisme " not in res, results)
        perco = [res for res in results if res not in participants][0]
        participants = np.array(list(results))

        winners = list(participants[int(np.where(participants == "Gagnants")[
                                       0]) + 1:int(np.where(participants == "Perdants")[0])])
        losers = list(participants[int(np.where(participants == "Perdants")[
                                      0]) + 1:len(participants)])

        if mode == "Attaque":
            if perco not in losers:
                return [], []
            losers.remove(perco)
        else:
            if perco not in winners:
                return [], []
            winners.remove(perco)

        return winners, losers, perco
