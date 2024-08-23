import os
import sys
import subprocess
import tkinter as tk
from tkinter import filedialog

# ffmpegのパスを指定
ffmpeg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ffmpeg", "ffmpeg.exe")
print(f"FFmpeg : {ffmpeg_path}")

while True:

    print("一括圧縮したいフォルダーを選択してください")

    def compress_videos(input_folder):
        i = 0

        # 入力フォルダー内の全ての動画ファイルを処理
        for filename in os.listdir(input_folder):
            i += 1
            print(i,"個目の動画を圧縮します")

            if filename.endswith((".mp4", ".avi", ".mov", ".mkv", "MP4", "MOV")):  #対応させる拡張子
                subfolder_name = "圧縮済み"

                # 元動画を読み込む
                input_file = os.path.join(input_folder, filename)

                # 出力先サブディレクトリを作成
                output_subfolder = os.path.join(input_folder, subfolder_name)
                os.makedirs(output_subfolder, exist_ok=True)  # サブディレクトリが存在しない場合は作成

                # 圧縮後のファイルパスを設定
                output_file = os.path.join(output_subfolder, f"{os.path.splitext(filename)[0]}.mp4")

                # FFmpegで動画を圧縮
                subprocess.run([
                    ffmpeg_path, '-i', input_file, '-c:v', codec, 
                    '-profile:v', profile, '-pix_fmt', 'yuv420p', qpcrf, crf, 
                    '-c:a', 'aac', '-b:a', audio_bitrate, output_file
                ], check=True)

                # 圧縮後の動画ファイルに対して、作成日時と更新日時を元動画と同じに設定
                os.utime(output_file, (os.path.getctime(input_file), os.path.getmtime(input_file)))

    if __name__ == "__main__":
        # フォルダ選択ダイアログの表示
        root = tk.Tk()
        root.withdraw()  # メインウィンドウを隠す
        folder_selected = filedialog.askdirectory()
        root.destroy()




    if folder_selected:
        os.system('cls')
        print(f"選択されたフォルダ: {folder_selected}\n")

        enc = input("エンコード方式を選択してください\n1:libx264,crf20 2:libx264,crf15 3:h264_nvenc,qp24 4:h264_nvenc,qp19\n")
        if enc == "1":
            print("libx264 crf20でエンコードします")

            # FFmpegの圧縮設定
            codec = 'libx264' #コーデックの選択
            qpcrf = '-crf' #品質パラメータ選択
            crf = '20' #品質の数値
            audio_bitrate = '128k' #オーディオビットレート
            profile = 'high' #風呂入るプロファイル

            compress_videos(folder_selected)
            print("全ての動画ファイルの圧縮が完了しました")
        elif enc == "2":
            print("libx264 crf15でエンコードします")

            # FFmpegの圧縮設定
            codec = 'libx264' #コーデックの選択
            qpcrf = '-qp' #品質パラメータ選択
            crf = '15' #品質の数値
            audio_bitrate = '128k' #オーディオビットレート
            profile = 'high' #風呂入るプロファイル

            compress_videos(folder_selected)
            print("全ての動画ファイルの圧縮が完了しました")
        elif enc == "3":
            print("h264_nvenc qp24でエンコードします")

            # FFmpegの圧縮設定
            codec = 'h264_nvenc' #コーデックの選択
            qpcrf = '-qp' #品質パラメータ選択
            crf = '24' #品質の数値
            audio_bitrate = '128k' #オーディオビットレート
            profile = 'high' #風呂入るプロファイル

            compress_videos(folder_selected)
            print("全ての動画ファイルの圧縮が完了しました")
        elif enc == "4":
            print("h264_nvenc4 qp19でエンコードします")

            # FFmpegの圧縮設定
            codec = 'h264_nvenc' #コーデックの選択
            qpcrf = '-qp' #品質パラメータ選択
            crf = '19' #品質の数値
            audio_bitrate = '128k' #オーディオビットレート
            profile = 'high' #風呂入るプロファイル

            compress_videos(folder_selected)
            print("全ての動画ファイルの圧縮が完了しました")
        else:
            print("範囲外の数字が選択されました")
            
    else:
        print("フォルダが選択されませんでした")

    q = 0
    while q != "y" or "n":
        q = input("他のフォルダーの動画も圧縮しますか？[y/n]\n")
        if q == "y":
            break
        elif q == "n":
            print("プログラムを終了します")
            sys.exit()
        else:
            print("y、n以外の文字が入力されました")
