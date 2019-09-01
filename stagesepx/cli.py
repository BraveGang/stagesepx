import fire
import os

from stagesepx.cutter import VideoCutter
from stagesepx.classifier import SVMClassifier
from stagesepx.reporter import Reporter
from stagesepx import toolbox


class TerminalCli(object):
    """
    this is a client for stagesepx, for easier usage.
    for flexible usage, you 'd better use the script way.
    """

    @toolbox.arg_printer
    def one_step(self,
                 video_path: str,
                 output_path: str = None,
                 frame_count: int = 5,
                 compress_rate: float = 0.2,
                 limit: int = None):
        """
        one step => cut, classifier, draw

        :param video_path: your video path
        :param output_path: output path (dir)
        :param frame_count: default to 5, and finally you will get 5 frames for each range
        :param compress_rate: before_pic * compress_rate = after_pic. default to 0.2
        :param limit: ignore some ranges which are too short, 5 means ignore stable ranges which length < 5
        :return:
        """

        # --- cutter ---
        cutter = VideoCutter()
        res = cutter.cut(video_path, compress_rate=compress_rate)
        stable, unstable = res.get_range(limit=limit)

        data_home = res.pick_and_save(
            stable,
            frame_count,
            to_dir=output_path)

        # --- classify ---
        cl = SVMClassifier(compress_rate=compress_rate)
        cl.load(data_home)
        cl.train()
        classify_result = cl.classify(video_path, stable)

        # --- draw ---
        r = Reporter()
        r.add_dir_link(data_home)
        r.draw(
            classify_result,
            report_path=os.path.join(data_home, 'report.html'),
            cut_result=res,
        )


def main():
    fire.Fire(TerminalCli)


if __name__ == '__main__':
    main()