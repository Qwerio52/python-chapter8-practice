# 8.3 you-get 视频下载演示
import subprocess
import shutil

def download_video(url):
    # 先检查系统能不能找到 you-get 命令
    if shutil.which("you-get") is None:
        print("❌ 错误：系统找不到 you-get 命令！")
        print("解决方案：安装后把 python 的 Scripts 目录加到系统PATH，或者在PyCharm终端运行")
        return
    cmd = ["you-get", url]
    try:
        subprocess.run(cmd, check=True)
        print("✅ 下载命令执行完成")
    except subprocess.CalledProcessError as e:
        print(f"❌ 命令执行失败: {e}")
    except Exception as e:
        print(f"❌ 其他错误：{e}")

if __name__ == "__main__":
    print("【重要提醒】you-get仅用于课程学习，严禁侵权下载资源！")
    link = input("请输入视频网址：")
    download_video(link)