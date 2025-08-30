import imageio as iio

filenames = [
    'C:/Users/KIIT/OneDrive/Documents/VS code - AH/python/1.png',
    'C:/Users/KIIT/OneDrive/Documents/VS code - AH/python/2.png'
]

images = [iio.imread(filename) for filename in filenames]

iio.mimsave('image.gif', images, duration=0.5, loop=0)
