from TikTokApi import TikTokApi
from moviepy.editor import VideoFileClip


def tiktok_video_to_gif(url: str):
    api = TikTokApi()
    video_as_bytes = api.video(url=url).bytes()

    with open('saved_video.mp4', 'wb') as output:
        output.write(video_as_bytes)

    video_clip = VideoFileClip('saved_video.mp4')  # name of saved video
    video_clip.write_gif('my-life.gif')  # name of future gif


TIKTOK_VIDEO_URL = ''  # put your url here
tiktok_video_to_gif(TIKTOK_VIDEO_URL)




