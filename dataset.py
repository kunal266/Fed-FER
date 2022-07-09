def Dataset(client):
    import os
    import random,shutil
    labels = ["angry","disgust","fear","happy","neutral","sad","surprise"]
    for i in range(200):
        emo = random.choice(labels)
        path = "/workspace/Fed-FER/train/"+emo
        files=os.listdir(path)
        d=random.choice(files)
        print(d,emo,"/workspace/Fed-FER/Dataset/"+client+"/"+ emo)
        if (os.path.exists("/workspace/Fed-FER/Dataset/"+client+"/"+ emo)):
            shutil.copy(path+"/"+d, "/workspace/Fed-FER/Dataset/"+client+"/"+ emo+"/"+d)
        else:
            os.mkdir("/workspace/Fed-FER/Dataset/"+client+"/"+ emo)


Dataset("client2")
Dataset("client3")
Dataset("client4")
Dataset("client5")
