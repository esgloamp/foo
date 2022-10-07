import os
import time
formats = (".mkv", ".mp4", ".flv", ".rm", ".rmvb", ".avi", ".mpg", ".mpeg")
dir = "D:/"
st = time.time()
starttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(st))
os.system(f"echo {starttime} begin>{dir}/err.log")
cnt = 0
for root, dirs, files in os.walk(dir):
    for filename in files:
        if filename.endswith(formats):
            cnt += 1
            abs_path = os.path.join(root, filename).replace("\\", "/")
            print(f"processing \"{abs_path}\"")
            os.system(
                f"echo =======================\"{abs_path}\" begin ======================== >>{dir}/err.log")
            os.system(
                f"ffmpeg -v error -i \"{abs_path}\" -map 0:1 -f null - 2>>{dir}/err.log")
            os.system(
                f"echo =======================\"{abs_path}\" end======================== >>{dir}/err.log")
et = time.time()
endtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(et))
usedtime = round(et - st, 3)
os.system(
    f"echo {endtime} end, used {usedtime}s, processed {cnt} files.>>{dir}/err.log")
print("used {usedtime}s, processed {cnt} files.")
