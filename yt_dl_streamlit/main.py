# Some Steamlit testing...
import pytube
import re
import streamlit as st
from pytube import YouTube


def main():
    st.title("YouTube Video Downloader")
    with st.form("download_form"):
        download_link = st.text_input("Enter the YouTube video URL")
        submitted = st.form_submit_button("Download Video")
        if submitted:
            try:
                yt_video = YouTube(download_link)
                stream = yt_video.streams.get_highest_resolution()
                stream.download()
                st.success(f"Video downloaded successfully: {stream.title}")
            except pytube.exceptions.RegexMatchError:
                st.error("Not a good URL - TRY AGAIN")


if __name__ == "__main__":
    main()
