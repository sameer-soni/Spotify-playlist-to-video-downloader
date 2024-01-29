from pytube import Search, YouTube
from pytube.cli import on_progress


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100

    print("\r" + "▌" * int(percentage_of_completion) + " " * (100 - int(percentage_of_completion)) + " {}%".format(
        int(percentage_of_completion)), end='')
def download_video(name, artist):
    try:
        s = Search(name + '' + artist)
        # print(f"{s.results[0].title}\n{s.results[0].watch_url}\n")
        file_name = s.results[0].title
        stream_url = s.results[0].watch_url

        # Create a YouTube object
        yt = YouTube(stream_url, on_progress_callback=on_progress)

        # Get the highest resolution video stream
        stream = yt.streams.get_highest_resolution()

        print(file_name)
        print("size of file", stream.filesize_mb, "mb")
        print("downloading....")
        stream.download()

        print(f"\n{file_name} Video downloaded successfully!")
        return file_name

    except KeyError:
        print("Error: Video is not available or cannot be downloaded")
    except ValueError:
        print("Error: Invalid URL")
    except Exception as e:
        print("Error downloading video:", str(e))


# Example usage
# download_video('save me', 'ramy zero')
