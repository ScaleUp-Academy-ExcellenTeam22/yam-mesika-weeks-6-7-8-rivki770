from PIL import Image


def open_image(path: str) -> str:
    '''
    A function that receives a path to an image, according to the number of lines of the black pixels finds the message.
    :param path: string of path of image file.
    :return: The decrypted file.
    '''
    image = Image.open(path)
    width, high = image.size
    letter = [chr(row) for column in range(width) for row in range(high) if image.load()[column, row] == 1]  # 1 = black
    return ''.join(letter)


def main():
    print(open_image("code.png"))


if __name__ == '__main__':
    main()

'''    
The message: Place gunpowder beneath the House of Lords. 11/05/1605
'''