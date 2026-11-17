import cv2
def pencil_sketch(image):
    gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    inverted_gray_image=cv2.bitwise_not(gray_image)
    blurred_image=cv2.GaussianBlur(inverted_gray_image,(21,21),0)
    inverted_blurred_image=cv2.bitwise_not(blurred_image)
    pencil_sketch_image=cv2.divide(gray_image,inverted_blurred_image,scale=256.0)
    return pencil_sketch_image
image=cv2.imread('image.jpg')
if image is None:
    raise FileNotFoundError("Image ot loaded.Kindly check the image name/Path")
pencil_sketch_image=pencil_sketch(image)
cv2.imwrite('pencil_sketch.jpg',pencil_sketch_image)
cv2.imshow('original Image',image)
cv2.imshow('Pencil sketch',pencil_sketch_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
