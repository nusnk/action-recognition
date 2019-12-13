from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution3D, MaxPooling3D
from keras.optimizers import SGD, RMSprop
from keras.utils import np_utils, generic_utils
import theano
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import cv2
from sklearn.cross_validation import train_test_split
from sklearn import cross_validation
from sklearn import preprocessing



img_rows,img_cols,img_depth=16,16,15



#TODO: implement
X_tr=[]  #To store dataset


# listing = os.listdir('kth dataset/boxing')

# for vid in listing:
#     vid = 'kth dataset/boxing/'+vid
#     frames = []
#     cap = cv2.VideoCapture(vid)
#     fps = cap.get(5)
#     print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
 

#     for k in xrange(15):
#         ret, frame = cap.read()
#         frame=cv2.resize(frame,(img_rows,img_cols),interpolation=cv2.INTER_AREA)
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         frames.append(gray)

#         #plt.imshow(gray, cmap = plt.get_cmap('gray'))
#         #plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#         #plt.show()
#         #cv2.imshow('frame',gray)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     cap.release()
#     cv2.destroyAllWindows()

#     input=np.array(frames)

#     print(input.shape)
#     ipt=np.rollaxis(np.rollaxis(input,2,0),2,0)
#     print(ipt.shape)

#     X_tr.append(ipt)



listing2 = os.listdir('./dataset/handclapping')

for vid2 in listing2:
    vid2 = './dataset/handclapping/'+vid2
    frames = []
    cap = cv2.VideoCapture(vid2)
    fps = cap.get(5)
    print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))

    for k in range(15):
        ret, frame = cap.read()
        frame=cv2.resize(frame,(img_rows,img_cols),interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frames.append(gray)

        #plt.imshow(gray, cmap = plt.get_cmap('gray'))
        #plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
        #plt.show()
        #cv2.imshow('frame',gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    input=np.array(frames)

    print(input.shape)
    ipt=np.rollaxis(np.rollaxis(input,2,0),2,0)
    print(ipt.shape)

    X_tr.append(ipt)


listing3 = os.listdir('./dataset/handwaving')

for vid3 in listing3:
    vid3 = './dataset/handwaving/'+vid3
    frames = []
    cap = cv2.VideoCapture(vid3)
    fps = cap.get(5)
    print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))

    for k in range(15):
        ret, frame = cap.read()
        frame=cv2.resize(frame,(img_rows,img_cols),interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frames.append(gray)

        #plt.imshow(gray, cmap = plt.get_cmap('gray'))
        #plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
        #plt.show()
        #cv2.imshow('frame',gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    input=np.array(frames)

    print(input.shape)
    ipt=np.rollaxis(np.rollaxis(input,2,0),2,0)
    print(ipt.shape)

    X_tr.append(ipt)



# listing4 = os.listdir('kth dataset/jogging')

# for vid4 in listing4:
#     vid4 = 'kth dataset/jogging/'+vid4
#     frames = []
#     cap = cv2.VideoCapture(vid4)
#     fps = cap.get(5)
#     print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))

#     for k in xrange(15):
#         ret, frame = cap.read()
#         frame=cv2.resize(frame,(img_rows,img_cols),interpolation=cv2.INTER_AREA)
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         frames.append(gray)

#         #plt.imshow(gray, cmap = plt.get_cmap('gray'))
#         #plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#         #plt.show()
#         #cv2.imshow('frame',gray)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     cap.release()
#     cv2.destroyAllWindows()
#     input=np.array(frames)

#     print(input.shape)
#     ipt=np.rollaxis(np.rollaxis(input,2,0),2,0)
#     print(ipt.shape)

#     X_tr.append(ipt)


 
listing5 = os.listdir('./dataset/running')

for vid5 in listing5:
    vid5 = './dataset/running/'+vid5
    frames = []
    cap = cv2.VideoCapture(vid5)
    fps = cap.get(5)
    print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))

    for k in range(15):
        ret, frame = cap.read()
        frame=cv2.resize(frame,(img_rows,img_cols),interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frames.append(gray)

        #plt.imshow(gray, cmap = plt.get_cmap('gray'))
        #plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
        #plt.show()
        #cv2.imshow('frame',gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    input=np.array(frames)

    print(input.shape)
    ipt=np.rollaxis(np.rollaxis(input,2,0),2,0)
    print(ipt.shape)

    X_tr.append(ipt)
 



listing6 = os.listdir('./dataset/walking')

for vid6 in listing6:
    vid6 = './dataset/walking/'+vid6
    frames = []
    cap = cv2.VideoCapture(vid6)
    fps = cap.get(5)
    print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))

    for k in range(15):
        ret, frame = cap.read()
        frame=cv2.resize(frame,(img_rows,img_cols),interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frames.append(gray)

        #plt.imshow(gray, cmap = plt.get_cmap('gray'))
        #plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
        #plt.show()
        #cv2.imshow('frame',gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    input=np.array(frames)

    print(input.shape)
    ipt=np.rollaxis(np.rollaxis(input,2,0),2,0)
    print(ipt.shape)

    X_tr.append(ipt)



X_tr_array = np.array(X_tr)   # convert the frames read into array

num_samples = len(X_tr_array)
print(num_samples)


label=np.ones((num_samples,),dtype = int)
label[0:100]= 0
label[100:199] = 1
label[199:299] = 2
label[299:399] = 3
label[399:499]= 4
label[499:] = 5


train_data = [X_tr_array,label]

(X_train, y_train) = (train_data[0],train_data[1])
print('X_Train shape:', X_train.shape)

train_set = np.zeros((num_samples, 1, img_rows,img_cols,img_depth))

for h in range(num_samples):
    train_set[h][0][:][:][:]=X_train[h,:,:,:]
 

patch_size = 15   

print(train_set.shape, 'train samples')



batch_size = 2
nb_classes = 6
nb_epoch =50


Y_train = np_utils.to_categorical(y_train, nb_classes)



nb_filters = [32, 32]


nb_pool = [3, 3]

nb_conv = [5,5]



train_set = train_set.astype('float32')

train_set -= np.mean(train_set)

train_set /=np.max(train_set)




model = Sequential()
model.add(Convolution3D(nb_filters[0], nb_depth=nb_conv[0], nb_row=nb_conv[0], nb_col=nb_conv[0], input_shape=(1, img_rows, img_cols, patch_size), activation='relu'))
model.add(MaxPooling3D(pool_size=(nb_pool[0], nb_pool[0], nb_pool[0])))
model.add(Dropout(0.5))

model.add(Flatten())

model.add(Dense(128, init='normal', activation='relu'))

model.add(Dropout(0.5))

model.add(Dense(nb_classes,init='normal'))

model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='RMSprop')

 


X_train_new, X_val_new, y_train_new,y_val_new =  train_test_split(train_set, Y_train, test_size=0.2, random_state=4)




hist = model.fit(X_train_new, y_train_new, validation_data=(X_val_new,y_val_new),
          batch_size=batch_size,nb_epoch = nb_epoch,show_accuracy=True,shuffle=True)


#hist = model.fit(train_set, Y_train, batch_size=batch_size,
#         nb_epoch=nb_epoch,validation_split=0.2, show_accuracy=True,
#           shuffle=True)


score = model.evaluate(X_val_new, y_val_new, batch_size=batch_size, show_accuracy=True)
print('Test score:', score[0])
print('Test accuracy:', score[1])



# Plot the results
train_loss=hist.history['loss']
val_loss=hist.history['val_loss']
train_acc=hist.history['acc']
val_acc=hist.history['val_acc']
xc=range(100)

plt.figure(1,figsize=(7,5))
plt.plot(xc,train_loss)
plt.plot(xc,val_loss)
plt.xlabel('num of Epochs')
plt.ylabel('loss')
plt.title('train_loss vs val_loss')
plt.grid(True)
plt.legend(['train','val'])
print(plt.style.available) 
plt.style.use(['classic'])

plt.figure(2,figsize=(7,5))
plt.plot(xc,train_acc)
plt.plot(xc,val_acc)
plt.xlabel('num of Epochs')
plt.ylabel('accuracy')
plt.title('train_acc vs val_acc')
plt.grid(True)
plt.legend(['train','val'],loc=4)

plt.style.use(['classic'])