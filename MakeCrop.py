
def getCrops(img):

    return getMultipleCrop(img, (224, 224), 250)


def getCropOfMatrix(img, left, top, shape):

    right = left + shape[0]
    bottom = top + shape[1]
    return img[left:right, top:bottom]

def getMultipleCrop(img, cropShape, step):

    allCrops = []
    if (img.shape[0] > cropShape[0] and img.shape[1] > cropShape[1]):

        x = img.shape[0] - cropShape[0]
        y = img.shape[1] - cropShape[1]

        for i in range(0, x, step):
            for j in range(0, y, step):
                allCrops += [getCropOfMatrix(img, i, j, cropShape)]

    else:
        print("Img too small")


    return allCrops
