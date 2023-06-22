import cv2
import os

def extract_frames(video_path, output_dir, frame_interval):
    # 检查输出目录是否存在，如果不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 打开视频文件
    video = cv2.VideoCapture(video_path)
    frame_count = 0
    success = True

    while success:
        success, frame = video.read()

        # 按指定的间隔抽取帧
        if frame_count % frame_interval == 0:
            # 构造输出帧文件名
            output_path = os.path.join(output_dir, f"frame_{frame_count}.jpg")

            # 保存帧为图像文件
            cv2.imwrite(output_path, frame)
            print(f"Saved frame {frame_count}: {output_path}")

        frame_count += 1

    video.release()
if __name__ == "__main__":
    # 示例用法
    video_path = "./video/badapple.mp4"  # 输入视频文件路径
    output_dir = "./output"  # 输出帧目录路径
    frame_interval = 2  # 抽帧间隔，每隔30帧抽取一帧

    extract_frames(video_path, output_dir, frame_interval)
