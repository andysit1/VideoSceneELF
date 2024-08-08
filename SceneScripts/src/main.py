import pygame
from pyvidplayer2 import Video
import cv2
import os
import glob
# create video object

tmp = "E:\Projects/2024\VideoSceneELF\SceneScripts\src/tmp_frame"
output_video_p = "E:\Projects/2024\VideoSceneELF\output-video"
# win = pygame.display.set_mode(vid.current_size)
# pygame.display.set_caption(vid.name)

def combine_output_frames_into_video(frame_rate : int = 60):

  fourcc = cv2.VideoWriter_fourcc(*'mp4v')

  if not os.path.exists(tmp):
    raise TypeError("Input Frame Path does not exists")

  if not os.path.exists(output_video_p):
    raise TypeError("Output Frame Path does not exists")

  frames = sorted(glob.glob(os.path.join(tmp, "*png")), key=os.path.getmtime)
  next_index_for_processed_videos = len(os.listdir(output_video_p))
  frame = cv2.imread(frames[0])
  height, width, _ = frame.shape

  output_video_path = '{}/test{}.mp4'.format(output_video_p, next_index_for_processed_videos)
  video = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (width, height))

  for frame in frames:
    frame = cv2.imread(frame)
    video.write(frame)

  video.release()


# vid = Video("E:\Projects/2024\Video-Content-Pipeline\processed-output-videos/test7.mp4")
# win = pygame.display.set_mode(vid.current_size)
# pygame.display.set_caption(vid.name)

# c = 0
# while vid.active:
#     key = None
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             vid.stop()
#         elif event.type == pygame.KEYDOWN:
#             key = pygame.key.name(event.key)

#     if key == "r":
#         vid.restart()           #rewind video to beginning
#     elif key == "p":
#         vid.toggle_pause()      #pause/plays video
#     elif key == "m":
#         vid.toggle_mute()       #mutes/unmutes video
#     elif key == "right":
#         vid.seek(15)            #skip 15 seconds in video
#     elif key == "left":
#         vid.seek(-15)           #rewind 15 seconds in video
#     elif key == "up":
#         vid.set_volume(1.0)     #max volume
#     elif key == "down":
#         vid.set_volume(0.0)     #min volume

#     # only draw new frames, and only update the screen if something is drawn

#     if vid.draw(win, (0, 0), force_draw=False):
#         c += 1
#         print(c)
#         if c < 10:
#           pygame.image.save(win, "{}/screenshot0{}.png".format(tmp,c))
#         else:
#           pygame.image.save(win, "{}/screenshot{}.png".format(tmp, c))

#         pygame.display.update()

#     pygame.time.wait(16) # around 60 fps

# # close video when done

# vid.close()
# pygame.quit()




combine_output_frames_into_video()