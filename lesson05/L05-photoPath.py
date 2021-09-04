import os
backupPhotoPath = "/Users/chilly/Desktop/python/yequ/崩溃的阿文"
os.chdir(backupPhotoPath)
photoPath = "backup"
for photo in os.listdir(photoPath):
    print(photo)
