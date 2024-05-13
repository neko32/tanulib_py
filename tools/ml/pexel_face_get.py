from tlib.web.pexels import PexelDownloader


def main():
    pexel = PexelDownloader()
    cnt = pexel.download(
        dataset_name="faces_pexels",
        category_name="human",
        keyword="face",
        page_st = 1,
        page_end = 30
    )
    print(f"downloaded face images from pexels are {cnt}.")


if __name__ == "__main__":
    main()
