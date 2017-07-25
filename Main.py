from MakeCrop import *
from Utils import *
from CropClassifier import CropClassifier
import glob
import os
import re

def main():

    classifier = CropClassifier()
    preDataPaths = glob.glob('PreData/*/')

    goodCounterId = 0
    badCounterId = 0

    for locationPath in preDataPaths:

        tempLocationPath = locationPath + "*/"

        print(locationPath)
        print(tempLocationPath)

        allTreePath = glob.glob(tempLocationPath)

        for treePath in allTreePath:

            tempTreePath = treePath + "*.jpg"
            allFilePath = glob.glob(tempTreePath)

            treeKind = re.match(".*([A-Z]{3})[0-9].*", treePath).group(1)

            print("Kind Of Tree : " + treeKind)

            directory = "./data/good/" + treeKind

            if not os.path.exists(directory):
                os.makedirs(directory)

            print(treePath)
            print(tempTreePath)

            for file in allFilePath:

                print(file)

                img = load_image(file)
                allCrops = getCrops(img)

                for crop in allCrops:

                    cropZero = removeMean(crop)
                    prediction = classifier.getCropClass(cropZero)
                    if (prediction):
                        save_image(directory + "/crop" + treeKind + str(goodCounterId) + ".jpg", crop)

                        goodCounterId += 1

                    else:
                        save_image("./data/bad/crop"  + str(badCounterId) + ".jpg", crop)

                        badCounterId += 1

    print(str(goodCounterId) + " good crop!")
    print(str(badCounterId) + " bad crop!")



main()