from acrcloud.recognizer import ACRCloudRecognizer
from acrcloud.recognizer import ACRCloudRecognizeType

def setup():
    config = {
        'host': 'identify-ap-southeast-1.acrcloud.com',
        'access_key': '450adec73c812fc14e6596f48dd95f70',
        'access_secret': 'KJwFL18C9UhO7xgqftDAmVGMThieQMdtlDCrU5da',
        'recognize_type': ACRCloudRecognizeType.ACR_OPT_REC_AUDIO,
    # you can replace it with [ACR_OPT_REC_AUDIO,ACR_OPT_REC_HUMMING,ACR_OPT_REC_BOTH], The     SDK decide which type fingerprint to create accordings to "recognize_type".
        'debug': False,
        'timeout': 10  # seconds
    }
    re = ACRCloudRecognizer(config)
    return re

def getMeta(sampleName,duration=5):
    return (setup().recognize_by_file(sampleName, 0, duration))
