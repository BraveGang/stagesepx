import os

from stagesepx.api import cut, classify, one_step, train
from stagesepx.reporter import Reporter
from stagesepx.video import VideoObject

PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
VIDEO_PATH = os.path.join(PROJECT_PATH, "demo.mp4")


def test_one_step():
    one_step(VIDEO_PATH)


def test_cut_and_classify():
    model_name = "model1.pkl"
    report_name = "report.html"

    # test cut
    res, data_home = cut(VIDEO_PATH)

    # test train
    train(data_home, model_name)

    # test classify
    classify_result = classify(VIDEO_PATH, data_home)
    classify_result_1 = classify(VIDEO_PATH, data_home, model=model_name)

    # --- draw ---
    r = Reporter()
    r.draw(
        classify_result,
        report_path=os.path.join(data_home, report_name),
        cut_result=res,
    )
    r.draw(
        classify_result_1,
        report_path=os.path.join(data_home, report_name),
        cut_result=res,
    )


def test_boost():
    video = VideoObject(VIDEO_PATH)
    video.load_frames()
    # test cut
    res, data_home = cut(video)

    # test classify
    classify_result = classify(video, data_home)

    # --- draw ---
    r = Reporter()
    r.draw(
        classify_result,
        report_path=os.path.join(data_home, "report.html"),
        cut_result=res,
    )