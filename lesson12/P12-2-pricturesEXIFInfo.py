import os
import ezexif
import openpyxl

wb = openpyxl.load_workbook("照片参数.xlsx", data_only=True)
workSheet = wb["示例"]

sourcePath = "photo"
allItems = os.listdir(sourcePath)
titleList = ["file_name", "Image ExifOffset", "EXIF ExposureProgram", "EXIF DateTimeOriginal", "EXIF MeteringMode", "EXIF Flash", "EXIF ExposureMode"]
for item in allItems:
    filePath = os.path.join(sourcePath, item)
    EXIFInfo = ezexif.process_file(filePath)
    EXIFInfo["file_name"] = item
    infoList = []
    for info in titleList:
        infoList.append(EXIFInfo[info])
    workSheet.append(infoList)

wb.save("照片参数-新.xlsx")

# 阿文担任一场摄影大赛组委会成员，她需要将参赛者的摄影作品的EXIF信息，统计在一张Excel文档里，方便后期进行评选。
# 需要统计照片的文件名("file_name")，和"Image ExifOffset","EXIF ExposureProgram","EXIF DateTimeOriginal","EXIF MeteringMode","EXIF Flash","EXIF ExposureMode"这6个EXIF信息。
# 照片在路径"/Users/Desktop/photo"的文件夹下。
# Excel文档的路径是"/Users/Desktop/照片参数.xlsx"。
# 文档的标题行已经有相应的信息，需要在后面对应的位置，填入对应文件对应EXIF信息的参数值。
# 写入后保存成相同路径下的"照片参数-新.xlsx"的文档。
