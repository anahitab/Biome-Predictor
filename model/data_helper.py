import os
import tensorflow as tf



class data_iterator():
    def __init__(self,images,labels,org_images=None):
        
        #c = list(zip(images, labels))
        #for i in range(15):
          #  random.shuffle(c)
        #a, b = zip(*c)
        self.labels = labels
        self.final_images = images
        self.org_images = org_images
        self.cursor = 0

    def next_batch(self, n):
        #print(type(self.final_images))
        
        image_batch = self.final_images[self.cursor:self.cursor+n]
        
        #print(type(image_batch))
        laels = self.labels[self.cursor:self.cursor+n]
        if self.org_images:
            org_imes = self.org_images[self.cursor:self.cursor+n]
	        self.cursor += n
            return image_batch , laels ,org_imes
        #print type(laels)
        self.cursor += n
        return image_batch , laels
