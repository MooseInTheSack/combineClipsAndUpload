from moviepy.editor import *
import os
from natsort import natsorted

#Clips must be the same dimension or else the output is corrupted
L =[]

for root, dirs, files in os.walk("/Users/tylerkirkpatrick/projects/combineClipsAndUpload/clips"):

    #files.sort()
    files = natsorted(files)
    for file in files:
        if os.path.splitext(file)[1] == '.mp4':
            filePath = os.path.join(root, file)
            video = VideoFileClip(filePath)
            L.append(video)

final_clip = concatenate_videoclips(L)
final_clip.to_videofile("output.mp4", fps=30, remove_temp=False)