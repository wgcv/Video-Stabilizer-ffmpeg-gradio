import ffmpeg
from transformers import Tool

class VideoStabilizationTool(Tool):
    name = "video_stabilization_tool"
    description = """
    This tool stabilizes a video.
    Inputs are input_path, output_path, smoothing, zoom.
    Output is the output_path.
    """
    inputs = { "input_path":{"type": "text"},"output_path":{"type": "text"},"smoothing":{"type": "text"},"zoom":{"type": "text"},"zoom":{"type": "text"} }
    # outputs = ["text"]
    output_type =  "text"
    def __call__(
        self,
        input_path: str,
        output_path: str,
        smoothing: str = "10",
        zoom: str = "0",
        shakiness: str = "5",
    ):
        (print(input_path))
        (
            ffmpeg.input(input_path)
            .output("null", vf="vidstabdetect=shakiness=10:accuracy=15".format(int(shakiness)), f="null")
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
        (
            ffmpeg.input(input_path)
            .output(
                output_path,
                vf="vidstabtransform=smoothing={}:zoom={}:input={}".format(
                    int(smoothing), int(zoom), "transforms.trf"
                ),
            )
            .overwrite_output()
            .run()
        )
        return output_path
